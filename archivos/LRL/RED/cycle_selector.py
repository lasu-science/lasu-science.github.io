"""
cycle_selector.py
=================
Engine thermodynamic cycle selection for liquid rocket engines.

Supported cycles
----------------
gas_generator      — Separate gas generator bleeds propellant to drive turbopumps.
                     Exhaust gas is dumped overboard → modest Isp penalty.
                     Widely used, well-understood, relatively simple.
                     Best for: moderate Pc, hydrocarbon fuels, first generation.

staged_combustion  — Preburner drives turbine, exhaust recombines in main chamber.
                     Full propellant enthalpy recovered → highest performance.
                     High Pc capable.  Complex turbopump architecture.
                     Best for: high-performance, LOX-CH4, LOX-LH2.

expander           — Fuel is heated through regenerative cooling jacket to drive turbine.
                     Thermally self-limited to lower Pc (fuel heat capacity is the limit).
                     No preburner → very clean, simple.
                     Only feasible for high-specific-heat fuels: LH2 (primary),
                     LCH4 (marginal, bleed variant possible).
                     NOT suitable for RP-1 (too high molecular weight, would cokeup).

Each cycle is described by:
  - complexity score (1 = simplest … 5 = most complex)
  - Pc ceiling [Pa] — above this the cycle becomes impractical
  - turbine efficiency fraction for c* (GG bleeds ~1.5–2% total propellant)
  - relative Isp loss fraction w.r.t. ideal (0 = no loss)
"""

from __future__ import annotations
from dataclasses import dataclass
from propellants import PropellantCombination


# ---------------------------------------------------------------------------
# Cycle descriptor dataclass
# ---------------------------------------------------------------------------

@dataclass
class EngineCycle:
    name: str
    complexity: int              # 1 (simplest) … 5 (most complex)
    Pc_max: float                # practical upper chamber pressure [Pa]
    Pc_min: float                # practical lower chamber pressure [Pa]
    Isp_loss_fraction: float    # fractional Isp penalty vs. ideal (0–0.05)
    description: str
    # List of fuel types this cycle supports; empty list = any fuel
    supported_fuels: list[str]


# ---------------------------------------------------------------------------
# Cycle catalogue
# ---------------------------------------------------------------------------

CYCLES: dict[str, EngineCycle] = {
    "gas_generator": EngineCycle(
        name="gas_generator",
        complexity=2,
        Pc_max=20.0e6,
        Pc_min=2.0e6,
        Isp_loss_fraction=0.015,   # ~1.5% Isp loss from GG bleed
        description=(
            "Conventional gas-generator cycle: a fraction of propellant is "
            "burned in a separate low-temperature gas generator to drive the "
            "turbopumps.  Turbine exhaust is dumped overboard, causing a small "
            "but unavoidable Isp penalty.  Well-characterised and robust."
        ),
        supported_fuels=[],        # compatible with all fuels
    ),
    "staged_combustion": EngineCycle(
        name="staged_combustion",
        complexity=4,
        Pc_max=30.0e6,
        Pc_min=5.0e6,
        Isp_loss_fraction=0.005,   # ~0.5% loss (seal leakage, turbine inefficiency)
        description=(
            "Full-flow or oxidiser-rich/fuel-rich staged combustion: all "
            "propellant passes through the preburner turbine, then is fully "
            "combusted in the main chamber.  No propellant is dumped → near-ideal "
            "Isp.  Requires very high-pressure turbopumps and tight sealing.  "
            "Highest performance for any propellant combination."
        ),
        supported_fuels=[],
    ),
    "expander": EngineCycle(
        name="expander",
        complexity=3,
        Pc_max=6.0e6,            # heat transfer limit of cooling jacket
        Pc_min=2.0e6,
        Isp_loss_fraction=0.002,  # very small: fuel re-enters chamber
        description=(
            "Expander (closed) cycle: cryogenic fuel is heated by the "
            "regenerative cooling jacket and drives the turbopumps before "
            "being injected into the chamber.  No separate combustor.  "
            "Thermally limited to moderate Pc (LH2 only in closed cycle; "
            "LCH4 feasible in bleed variant).  Excellent for upper stages."
        ),
        supported_fuels=["LH2", "LCH4"],   # RP-1 would coke and has low cp
    ),
}


# ---------------------------------------------------------------------------
# Feasibility & scoring
# ---------------------------------------------------------------------------

def is_cycle_feasible(cycle: EngineCycle,
                      propellant: PropellantCombination,
                      Pc: float,
                      priority: str) -> bool:
    """
    Return True if the cycle is physically and operationally feasible for the
    given propellant and chamber pressure.

    Rules:
      1. Cycle Pc must be within the cycle's validated range.
      2. Expander cycle requires a supported cryogenic fuel.
      3. If priority='simplicity', staged_combustion is never preferred
         (but is still feasible; the objective function penalises complexity).
    """
    # Pressure range check
    if not (cycle.Pc_min <= Pc <= cycle.Pc_max):
        return False

    # Fuel suitability check
    if cycle.supported_fuels:
        if propellant.fuel_name not in cycle.supported_fuels:
            return False

    return True


def score_cycle(cycle: EngineCycle,
                propellant: PropellantCombination,
                Pc: float,
                priority: str) -> float:
    """
    Score a cycle for a given design context on a 0–100 scale.
    Higher = better match to requirements.

    Scoring considers:
      - Isp loss (always penalised)
      - Complexity vs. priority
      - Pc margin (favour cycles with Pc well within their range)
      - Heritage for the specific propellant (informational bonus)
    """
    if not is_cycle_feasible(cycle, propellant, Pc, priority):
        return -1e9   # infeasible → disqualified

    score = 100.0

    # --- Isp penalty (universal) ---
    score -= cycle.Isp_loss_fraction * 1000.0   # 1% loss → -10 pts

    # --- Complexity trade-off ---
    if priority == "simplicity":
        score -= (cycle.complexity - 1) * 15.0  # penalise complexity heavily
    elif priority == "efficiency":
        score -= cycle.Isp_loss_fraction * 500.0  # penalise Isp loss more
        score -= (cycle.complexity - 1) * 3.0     # slight complexity allowance
    elif priority == "mass":
        # mass is complex: GG is lighter turbopump but SC allows higher Pc
        # Higher Pc → smaller (lighter) chamber for same thrust
        score -= (cycle.complexity - 1) * 8.0
        # Reward higher Pc capability
        score += min(Pc / cycle.Pc_max * 10.0, 10.0)

    # --- Pc margin reward (avoid operating near limits) ---
    Pc_margin = min(
        (Pc - cycle.Pc_min) / (cycle.Pc_max - cycle.Pc_min),
        1.0 - (Pc - cycle.Pc_min) / (cycle.Pc_max - cycle.Pc_min)
    )
    score += Pc_margin * 5.0    # up to +5 pts for being near centre of Pc range

    return score


def select_cycle(propellant: PropellantCombination,
                 Pc: float,
                 priority: str) -> EngineCycle:
    """
    Select the best engine cycle for the given propellant, Pc, and design priority.

    If no cycle is feasible at the requested Pc, the Pc is iteratively relaxed
    to the nearest boundary and the best cycle at that adjusted Pc is returned.

    Returns the winning EngineCycle object.
    """
    best_cycle: EngineCycle | None = None
    best_score = -1e10

    for cycle in CYCLES.values():
        s = score_cycle(cycle, propellant, Pc, priority)
        if s > best_score:
            best_score = s
            best_cycle = cycle

    if best_cycle is None or best_score < -1e8:
        # Fallback: find any feasible cycle by relaxing Pc
        Pc_adj = float(Pc)
        for _ in range(500):
            for cycle in CYCLES.values():
                s = score_cycle(cycle, propellant, Pc_adj, priority)
                if s > -1e8:
                    return cycle
            Pc_adj *= 0.95   # try lower Pc
        # Ultimate fallback: gas generator always works
        return CYCLES["gas_generator"]

    return best_cycle


def cycle_Isp_efficiency(cycle: EngineCycle) -> float:
    """
    Return the efficiency multiplier (0–1) on ideal Isp for this cycle.
    ve_real = ve_ideal × cycle_Isp_efficiency
    """
    return 1.0 - cycle.Isp_loss_fraction


def get_all_feasible_cycles(propellant: PropellantCombination,
                             Pc: float,
                             priority: str) -> list[EngineCycle]:
    """Return all feasible cycles sorted by score (best first)."""
    scored = []
    for cycle in CYCLES.values():
        s = score_cycle(cycle, propellant, Pc, priority)
        if s > -1e8:
            scored.append((s, cycle))
    scored.sort(key=lambda x: -x[0])
    return [c for _, c in scored]
