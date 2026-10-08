"""
optimizer.py
============
Two-level optimisation for the rocket engine designer.

Strategy
--------
Level 1 (Discrete):   Iterate over all feasible engine cycles.
Level 2 (Continuous): For each cycle, use scipy.optimize.differential_evolution
                      to search the continuous design space:
                        x = [Pc, O/F, epsilon, dP_fraction]

The optimizer maximises the objective_score by minimising its negative.
After convergence, injector elements are sized from the final (Pc, O/F, mdot).

This approach handles the mixed-integer nature of the problem cleanly without
needing dedicated MINLP solvers.

Design variable bounds
----------------------
Variable        Symbol      Bounds
────────────────────────────────────────────────────────
Chamber pressure  Pc       [Pc_min_cycle, Pc_max_cycle] (MPa)
Mixture ratio     O/F      [OF_min, OF_max]
Expansion ratio   ε        [2, 200]
ΔP fraction       fΔP      [0.10, 0.30]
"""

from __future__ import annotations
import numpy as np
from scipy.optimize import differential_evolution, minimize
from typing import Any

import warnings
import numpy as np

from propellants import PropellantCombination, get_propellant
from thermodynamics import (
    compute_nozzle_state,
    mass_flow_from_thrust,
    split_mass_flow,
    throat_area,
    exit_area,
    throat_diameter,
    exit_diameter,
)
from cycle_selector import (
    EngineCycle,
    CYCLES,
    get_all_feasible_cycles,
    cycle_Isp_efficiency,
    is_cycle_feasible,
)
from injector_model import design_injectors, best_injector_type_for_propellant
from objective_function import objective_score


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

G0 = 9.80665      # m/s²
MIN_FEASIBLE_SCORE = -900.0   # scores below this indicate infeasible design


# ---------------------------------------------------------------------------
# Evaluate a complete design point
# ---------------------------------------------------------------------------

def evaluate_design(propellant: PropellantCombination,
                    cycle: EngineCycle,
                    F: float,
                    Pa: float,
                    priority: str,
                    Pc: float,
                    OF: float,
                    epsilon: float,
                    dP_fraction: float) -> dict[str, Any]:
    """
    Evaluate the full engine design at a specific set of continuous variables.

    Returns a dict with all computed parameters and the objective score.
    Returns None-valued dict with low score if the point is infeasible.
    """
    # --- Quick feasibility gate ---
    if not propellant.validate_OF(OF):
        return {"score": -1e6}
    if not is_cycle_feasible(cycle, propellant, Pc, priority):
        return {"score": -1e6}
    if not (0.08 <= dP_fraction <= 0.32):
        return {"score": -1e6}
    if epsilon < 1.5:
        return {"score": -1e6}

    # --- Thermodynamics ---
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", RuntimeWarning)
            thermo = compute_nozzle_state(
                propellant=propellant,
                OF=OF,
                Pc=Pc,
                Pa=Pa,
                epsilon=epsilon,
            )
    except Exception:
        return {"score": -1e6}

    # Apply cycle efficiency (GG losses, etc.)
    eta_cycle = cycle_Isp_efficiency(cycle)
    Isp_eff   = thermo["Isp"] * eta_cycle
    ve_eff    = Isp_eff * G0

    # --- Mass flow and geometry ---
    mdot_total = mass_flow_from_thrust(F, ve_eff)
    mdot_ox, mdot_fuel = split_mass_flow(mdot_total, OF)

    c_star = thermo["c_star"]
    A_t    = throat_area(mdot_total, c_star, Pc)
    A_e    = exit_area(A_t, thermo["epsilon"])

    # Cylindrical chamber (L* burn criterion → assume chamber L* = 1.0–1.2 m)
    # Chamber diameter ≈ 2.5–3.5 × throat diameter (contraction ratio ~6–10)
    contraction_ratio = max(5.0, min(10.0, 8.0 - Pc / 10e6))
    A_chamber = A_t * contraction_ratio

    # --- Injector sizing ---
    inj_type_name = best_injector_type_for_propellant(propellant.fuel_name)
    injector = design_injectors(
        propellant=propellant,
        OF=OF,
        mdot_total=mdot_total,
        Pc=Pc,
        A_chamber=A_chamber,
        injector_type_name=inj_type_name,
        dP_fraction=dP_fraction,
    )

    # --- Objective score ---
    score = objective_score(
        Isp=Isp_eff,
        Pc=Pc,
        OF=OF,
        epsilon=thermo["epsilon"],
        dP_fraction=dP_fraction,
        n_elements=injector.n_elements,
        cycle=cycle,
        propellant=propellant,
        priority=priority,
    )

    return {
        "score": score,
        "cycle": cycle.name,
        "propellant": propellant.name,
        "priority": priority,
        # Thermodynamics
        "Tc":       thermo["Tc"],
        "gamma":    thermo["gamma"],
        "M_mol":    thermo["M_mol"],
        "c_star":   c_star,
        "Cf":       thermo["Cf"],
        "Isp":      Isp_eff,
        "ve":       ve_eff,
        "Me":       thermo["Me"],
        "Pe":       thermo["Pe"],
        # Operating conditions
        "Pc":       Pc,
        "Pa":       Pa,
        "OF":       OF,
        "epsilon":  thermo["epsilon"],
        "dP_fraction": dP_fraction,
        # Mass flow
        "mdot_total": mdot_total,
        "mdot_ox":    mdot_ox,
        "mdot_fuel":  mdot_fuel,
        # Geometry
        "A_t":         A_t,
        "A_e":         A_e,
        "d_throat":    throat_diameter(A_t),
        "d_exit":      exit_diameter(A_e),
        "A_chamber":   A_chamber,
        "contraction_ratio": contraction_ratio,
        # Injector
        "injector_type":     injector.injector_type,
        "n_injectors":       injector.n_elements,
        "d_fuel_orifice":    injector.d_fuel_orifice,
        "d_ox_orifice":      injector.d_ox_orifice,
        "dP_fuel":           injector.dP_fuel,
        "dP_ox":             injector.dP_ox,
        "v_fuel_orifice":    injector.v_fuel,
        "v_ox_orifice":      injector.v_ox,
        "injector_face_util":injector.face_area_util,
        "stability_margin":  injector.stability_margin,
    }


# ---------------------------------------------------------------------------
# Optimisation for a single cycle
# ---------------------------------------------------------------------------

def optimise_for_cycle(propellant: PropellantCombination,
                       cycle: EngineCycle,
                       F: float,
                       Pa: float,
                       priority: str,
                       seed: int = 42) -> dict[str, Any]:
    """
    Use SciPy differential_evolution to find the optimal (Pc, OF, epsilon, dP_fraction)
    for a fixed cycle.

    Differential evolution is a global optimizer that handles non-convex, noisy
    landscapes — suitable because our objective has many local optima
    (especially near the OF optimum and across the ΔP range).
    """
    # --- Bounds ---
    Pc_lo  = max(cycle.Pc_min, 2.0e6)
    Pc_hi  = min(cycle.Pc_max, 20.0e6)
    OF_lo  = propellant.OF_min
    OF_hi  = propellant.OF_max
    eps_lo = 2.0
    eps_hi = 150.0    # cap at 150: beyond that nozzle mass dominates
    dP_lo  = 0.10
    dP_hi  = 0.30

    bounds = [(Pc_lo, Pc_hi), (OF_lo, OF_hi), (eps_lo, eps_hi), (dP_lo, dP_hi)]

    def neg_score(x):
        Pc, OF, eps, dP = x
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", RuntimeWarning)
            result = evaluate_design(propellant, cycle, F, Pa, priority,
                                     Pc=Pc, OF=OF, epsilon=eps, dP_fraction=dP)
        return -result["score"]   # minimise negative score

    # Global search with differential evolution
    de_result = differential_evolution(
        neg_score,
        bounds=bounds,
        seed=seed,
        maxiter=300,
        popsize=12,
        tol=1e-5,
        polish=True,            # final local polish with L-BFGS-B
        workers=1,
        mutation=(0.5, 1.5),
        recombination=0.7,
    )

    Pc_opt, OF_opt, eps_opt, dP_opt = de_result.x
    result = evaluate_design(propellant, cycle, F, Pa, priority,
                              Pc=Pc_opt, OF=OF_opt, epsilon=eps_opt, dP_fraction=dP_opt)
    result["optimiser_success"]  = de_result.success
    result["optimiser_nfev"]     = de_result.nfev
    result["optimiser_message"]  = de_result.message
    return result


# ---------------------------------------------------------------------------
# Top-level optimiser
# ---------------------------------------------------------------------------

def run_optimisation(propellant: PropellantCombination,
                     F: float,
                     Pa: float,
                     priority: str,
                     verbose: bool = True) -> dict[str, Any]:
    """
    Run the full two-level optimisation over all feasible cycles.

    For each feasible cycle:
      1. Determine Pc range (cycle-limited)
      2. Run differential_evolution over (Pc, OF, ε, ΔP/Pc)
      3. Collect the best result

    Return the globally best design dict.

    Args:
        propellant  : PropellantCombination from propellants.py
        F           : required thrust [N]
        Pa          : ambient pressure [Pa]
        priority    : "efficiency" | "simplicity" | "mass"
        verbose     : print progress
    """
    # Use a representative initial Pc to filter feasible cycles
    Pc_initial_guess = 10e6   # 10 MPa starting point
    feasible_cycles = get_all_feasible_cycles(propellant, Pc_initial_guess, priority)

    if not feasible_cycles:
        raise RuntimeError(
            f"No feasible cycle found for {propellant.name} at Pc≈10 MPa "
            f"with priority='{priority}'."
        )

    best_result: dict[str, Any] = {"score": -1e9}

    for cycle in feasible_cycles:
        if verbose:
            print(f"  ↳ Optimising for cycle: {cycle.name:20s} ", end="", flush=True)

        try:
            result = optimise_for_cycle(propellant, cycle, F, Pa, priority)
        except Exception as exc:
            if verbose:
                print(f"[FAILED: {exc}]")
            continue

        if verbose:
            print(f"→ score={result['score']:7.2f}  Isp={result.get('Isp', 0):.1f}s  "
                  f"Pc={result.get('Pc', 0)/1e6:.1f}MPa  "
                  f"OF={result.get('OF', 0):.2f}")

        if result["score"] > best_result["score"]:
            best_result = result

    if best_result["score"] < MIN_FEASIBLE_SCORE:
        raise RuntimeError(
            "Optimisation converged to an infeasible region.  "
            "Try relaxing thrust requirements or changing propellant combination."
        )

    return best_result
