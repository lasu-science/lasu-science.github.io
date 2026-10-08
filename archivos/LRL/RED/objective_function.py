"""
objective_function.py
=====================
Multi-objective scoring function for the rocket engine design optimiser.

The objective function maps a design point (Pc, O/F, ε, ΔP_fraction, n_elements)
to a scalar score that captures engineering trade-offs according to the user's
declared design priority:

    "efficiency"  — maximise specific impulse; accept complexity, mass
    "simplicity"  — minimise part count, complexity, Pc; accept modest Isp
    "mass"        — minimise propulsion system mass (high Pc → smaller chamber)

Score breakdown (approximate weights, priority-dependent):
  +  Isp contribution            (always dominant)
  -  Chamber pressure penalty    (beyond a soft threshold)
  -  Injector count penalty      (fewer = simpler)
  -  Cycle complexity penalty    (priority-weighted)
  -  Off-optimal OF penalty      (peak Tc deviation)
  -  Injector ΔP out-of-window   (stability vs. pump power)
  -  Expansion ratio penalty     (very high ε → heavy nozzle)
  -  Constraint violations       (hard penalties, large magnitude)
"""

from __future__ import annotations
import numpy as np
from propellants import PropellantCombination
from cycle_selector import EngineCycle


# ---------------------------------------------------------------------------
# Weight sets per priority
# ---------------------------------------------------------------------------

# Each dict: keys match the score components below; values are multipliers.
WEIGHTS: dict[str, dict[str, float]] = {
    "efficiency": {
        "Isp":            1.00,
        "Pc_penalty":     0.10,   # low: high Pc is acceptable for performance
        "n_inj_penalty":  0.20,
        "complexity":     0.10,
        "OF_deviation":   0.60,
        "dP_penalty":     0.30,
        "epsilon_penalty":0.10,
    },
    "simplicity": {
        "Isp":            0.50,
        "Pc_penalty":     0.60,   # high: prefer lower, simpler systems
        "n_inj_penalty":  0.80,
        "complexity":     1.00,
        "OF_deviation":   0.40,
        "dP_penalty":     0.30,
        "epsilon_penalty":0.40,
    },
    "mass": {
        "Isp":            0.70,
        "Pc_penalty":     0.20,   # moderate: high Pc = small chamber = light
        "n_inj_penalty":  0.30,
        "complexity":     0.30,
        "OF_deviation":   0.50,
        "dP_penalty":     0.30,
        "epsilon_penalty":0.60,   # large nozzle is heavy
    },
}


# ---------------------------------------------------------------------------
# Individual scoring sub-functions
# ---------------------------------------------------------------------------

def score_Isp(Isp: float) -> float:
    """
    Isp score, normalised so Isp = 300 s → 50 pts and Isp = 450 s → 100 pts.
    Linear interpolation beyond these anchors.
    Scaled to be the dominant term.
    """
    return float(np.interp(Isp, [200, 300, 360, 430, 500],
                                 [0,   50,  70,  90,  100]))


def score_chamber_pressure(Pc: float, Pc_soft_limit: float = 15e6) -> float:
    """
    Penalty for very high chamber pressure.
    Pc ≤ soft_limit  → 0 penalty
    Pc > soft_limit  → linearly increasing penalty up to -30 pts at 30 MPa
    """
    if Pc <= Pc_soft_limit:
        return 0.0
    excess = (Pc - Pc_soft_limit) / (30e6 - Pc_soft_limit)
    return -30.0 * float(np.clip(excess, 0.0, 1.0))


def score_injector_count(n_elements: int, n_ref: int = 100) -> float:
    """
    Reward fewer injector elements.
    n ≤ 20   → +10 pts (very few → good atomisation challenge, but simple)
    n = 100  →   0 pts (reference)
    n > 300  → -20 pts
    """
    return float(np.interp(n_elements, [20, 100, 200, 500],
                                       [10,   0, -10, -20]))


def score_complexity(cycle: EngineCycle) -> float:
    """Penalty for cycle complexity (1 = simple, 5 = very complex)."""
    return -(cycle.complexity - 1) * 10.0   # 0 for simplest, -40 for most complex


def score_OF_deviation(OF: float, propellant: PropellantCombination) -> float:
    """
    Penalise operation far from optimal O/F for Isp.
    ±10% from OF_optimal → 0 penalty
    ±25% → -15 pts
    ±50% → -40 pts
    """
    OF_opt = propellant.OF_optimal_Isp
    rel_dev = abs(OF - OF_opt) / OF_opt
    return float(np.interp(rel_dev, [0.0, 0.10, 0.25, 0.50, 1.00],
                                     [0.0, 0.0, -15.0, -40.0, -80.0]))


def score_dP_fraction(dP_fraction: float) -> float:
    """
    Score for injector pressure drop fraction.
    0.15–0.25 is the engineering sweet spot (stability + reasonable pump work).
    """
    return float(np.interp(dP_fraction,
                            [0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.40],
                            [-40,  -10,    5,   10,    5,   -5,  -20]))


def score_expansion_ratio(epsilon: float, priority: str) -> float:
    """
    Penalty for extreme expansion ratios.
    Very high ε is fine for vacuum but heavy for sea-level stages.
    """
    if priority == "mass":
        # Heavy nozzle is a concern
        return float(np.interp(epsilon, [2, 10, 30, 80, 200],
                                         [0,  5,  2, -5, -25]))
    else:
        # Efficiency / simplicity: high ε is generally fine in vacuum
        return float(np.interp(epsilon, [2, 10, 50, 150, 200],
                                         [0,  5,  5,   0,  -5]))


# ---------------------------------------------------------------------------
# Hard constraint violations
# ---------------------------------------------------------------------------

def hard_constraint_penalty(OF: float,
                             Pc: float,
                             dP_fraction: float,
                             epsilon: float,
                             propellant: PropellantCombination,
                             cycle: EngineCycle) -> float:
    """
    Return a very large negative score if hard physical constraints are violated.
    These are non-negotiable bounds (unlike the soft penalties above).

    Checked:
      - O/F within propellant's valid range
      - Pc within cycle's valid range
      - dP_fraction in [0.08, 0.32]
      - expansion ratio ε in [1.5, 250]
    """
    penalty = 0.0
    large = 1000.0

    if not propellant.validate_OF(OF):
        penalty -= large * 2

    if not (cycle.Pc_min * 0.9 <= Pc <= cycle.Pc_max * 1.1):
        penalty -= large

    if not (0.08 <= dP_fraction <= 0.32):
        penalty -= large * 0.5

    if not (1.5 <= epsilon <= 250.0):
        penalty -= large * 0.5

    return penalty


# ---------------------------------------------------------------------------
# Main objective function
# ---------------------------------------------------------------------------

def objective_score(Isp: float,
                    Pc: float,
                    OF: float,
                    epsilon: float,
                    dP_fraction: float,
                    n_elements: int,
                    cycle: EngineCycle,
                    propellant: PropellantCombination,
                    priority: str) -> float:
    """
    Compute the total weighted objective score for a design point.

    Args:
        Isp          : specific impulse [s]
        Pc           : chamber pressure [Pa]
        OF           : oxidiser/fuel mass ratio
        epsilon      : nozzle expansion ratio
        dP_fraction  : injector ΔP / Pc
        n_elements   : number of injector elements
        cycle        : selected engine cycle
        propellant   : propellant combination
        priority     : "efficiency" | "simplicity" | "mass"

    Returns:
        scalar score (higher = better design)
    """
    w = WEIGHTS.get(priority, WEIGHTS["efficiency"])

    # Component scores
    s_isp        = score_Isp(Isp)
    s_Pc         = score_chamber_pressure(Pc)
    s_inj        = score_injector_count(n_elements)
    s_complex    = score_complexity(cycle)
    s_OF         = score_OF_deviation(OF, propellant)
    s_dP         = score_dP_fraction(dP_fraction)
    s_eps        = score_expansion_ratio(epsilon, priority)
    s_hard       = hard_constraint_penalty(OF, Pc, dP_fraction, epsilon,
                                           propellant, cycle)

    total = (
        w["Isp"]            * s_isp
        + w["Pc_penalty"]   * s_Pc
        + w["n_inj_penalty"]* s_inj
        + w["complexity"]   * s_complex
        + w["OF_deviation"] * s_OF
        + w["dP_penalty"]   * s_dP
        + w["epsilon_penalty"] * s_eps
        + s_hard            # hard constraints always applied at full magnitude
    )
    return float(total)


def score_breakdown(Isp: float,
                    Pc: float,
                    OF: float,
                    epsilon: float,
                    dP_fraction: float,
                    n_elements: int,
                    cycle: EngineCycle,
                    propellant: PropellantCombination,
                    priority: str) -> dict[str, float]:
    """
    Return a breakdown of score components (useful for diagnostics / reporting).
    """
    w = WEIGHTS.get(priority, WEIGHTS["efficiency"])
    return {
        "Isp_score":        w["Isp"]            * score_Isp(Isp),
        "Pc_penalty":       w["Pc_penalty"]     * score_chamber_pressure(Pc),
        "injector_score":   w["n_inj_penalty"]  * score_injector_count(n_elements),
        "complexity_score": w["complexity"]     * score_complexity(cycle),
        "OF_score":         w["OF_deviation"]   * score_OF_deviation(OF, propellant),
        "dP_score":         w["dP_penalty"]     * score_dP_fraction(dP_fraction),
        "epsilon_score":    w["epsilon_penalty"]* score_expansion_ratio(epsilon, priority),
        "hard_penalties":   hard_constraint_penalty(OF, Pc, dP_fraction, epsilon,
                                                    propellant, cycle),
    }
