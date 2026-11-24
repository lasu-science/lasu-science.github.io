"""
main.py
=======
Rocket Engine Designer — main entry point.

Public API
----------
    design_engine(F, Pa, propellant_name, priority) → dict

    print_report(design) → None

Usage example
-------------
    from main import design_engine, print_report

    design = design_engine(
        F=1_000_000,          # 1 MN thrust
        Pa=101_325,           # sea level
        propellant_name="LOX-CH4",
        priority="efficiency",
    )
    print_report(design)

The returned dictionary is the complete engine design specification,
ready for further analysis, CFD boundary conditions, or mass estimation.
"""

from __future__ import annotations
import sys
import time
import numpy as np
from typing import Any

# Ensure local modules take precedence over any installed packages
import os
sys.path.insert(0, os.path.dirname(__file__))

from propellants import get_propellant, PROPELLANT_REGISTRY
from optimizer import run_optimisation
from objective_function import score_breakdown


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

G0 = 9.80665    # standard gravity [m/s²]


# ---------------------------------------------------------------------------
# Validation helpers
# ---------------------------------------------------------------------------

VALID_PRIORITIES = ("efficiency", "simplicity", "mass")


def _validate_inputs(F: float, Pa: float,
                     propellant_name: str, priority: str) -> None:
    if F <= 0:
        raise ValueError(f"Thrust F must be positive, got {F} N")
    if Pa < 0:
        raise ValueError(f"Ambient pressure Pa must be ≥ 0, got {Pa} Pa")
    if propellant_name.upper().replace("_", "-") not in PROPELLANT_REGISTRY:
        raise ValueError(f"Unknown propellant '{propellant_name}'. "
                         f"Available: {list(PROPELLANT_REGISTRY.keys())}")
    if priority not in VALID_PRIORITIES:
        raise ValueError(f"priority must be one of {VALID_PRIORITIES}, got '{priority}'")


# ---------------------------------------------------------------------------
# Main public function
# ---------------------------------------------------------------------------

def design_engine(F: float,
                  Pa: float,
                  propellant_name: str,
                  priority: str = "efficiency",
                  verbose: bool = True) -> dict[str, Any]:
    """
    Automatically design and optimise a liquid rocket engine.

    Parameters
    ----------
    F               : Required sea-level (or vacuum) thrust [N]
    Pa              : Ambient pressure at nozzle exit plane [Pa]
                      (101325 Pa = sea level; 0 Pa = vacuum)
    propellant_name : Propellant combination string.
                      Supported: "LOX-LH2", "LOX-CH4", "LOX-RP1"
    priority        : Design optimisation priority.
                      "efficiency"  → maximise Isp and specific performance
                      "simplicity"  → minimise complexity, part count, Pc
                      "mass"        → minimise propulsion system mass
    verbose         : Print optimisation progress to stdout

    Returns
    -------
    dict containing the full engine specification:
        cycle_type, Pc, OF, c_star, Cf, Isp, ve,
        mdot_total, mdot_ox, mdot_fuel,
        A_t, A_e, d_throat, d_exit, epsilon,
        n_injectors, injector_type, d_fuel_orifice, d_ox_orifice,
        dP_fuel, dP_ox, dP_fraction,
        Tc, gamma, M_mol, Me, Pe,
        score, score_breakdown
    """
    _validate_inputs(F, Pa, propellant_name, priority)
    propellant = get_propellant(propellant_name)

    if verbose:
        print("=" * 65)
        print("  🚀  LIQUID ROCKET ENGINE DESIGNER")
        print("=" * 65)
        print(f"  Thrust required : {F/1e3:,.1f} kN")
        print(f"  Ambient pressure: {Pa/1e5:.4f} bar")
        print(f"  Propellant      : {propellant.name}")
        print(f"  Design priority : {priority.upper()}")
        print(f"  Heritage engines: {propellant.heritage}")
        print("-" * 65)
        print("  Running two-level optimisation …")

    t0 = time.time()
    design = run_optimisation(propellant, F, Pa, priority, verbose=verbose)
    elapsed = time.time() - t0

    if verbose:
        print(f"\n  Optimisation complete in {elapsed:.1f}s")

    # Augment with score breakdown
    from cycle_selector import CYCLES
    cycle_obj = CYCLES[design["cycle"]]
    breakdown = score_breakdown(
        Isp=design["Isp"],
        Pc=design["Pc"],
        OF=design["OF"],
        epsilon=design["epsilon"],
        dP_fraction=design["dP_fraction"],
        n_elements=design["n_injectors"],
        cycle=cycle_obj,
        propellant=propellant,
        priority=priority,
    )
    design["score_breakdown"] = breakdown
    design["optimisation_time_s"] = elapsed

    return design


# ---------------------------------------------------------------------------
# Report formatter
# ---------------------------------------------------------------------------

def print_report(design: dict[str, Any]) -> None:
    """
    Print a formatted engineering report to stdout.
    """
    sep  = "=" * 65
    sep2 = "-" * 65

    print()
    print(sep)
    print("  ENGINE DESIGN REPORT")
    print(sep)

    # --- Overview ---
    print(f"\n  Propellant   : {design['propellant']}")
    print(f"  Cycle        : {design['cycle'].replace('_', ' ').title()}")
    print(f"  Priority     : {design['priority'].upper()}")
    print(f"  Objective    : {design['score']:.2f} pts")

    # --- Performance ---
    print(f"\n{'  PERFORMANCE':}")
    print(sep2)
    print(f"  Specific Impulse (Isp)  : {design['Isp']:.1f}  s")
    print(f"  Exhaust velocity (ve)   : {design['ve']:.1f}  m/s")
    print(f"  Char. velocity   (c*)   : {design['c_star']:.1f}  m/s")
    print(f"  Thrust coefficient (Cf) : {design['Cf']:.4f}")
    print(f"  Adiabatic flame Tc      : {design['Tc']:.0f}  K")
    print(f"  Exit Mach number (Me)   : {design['Me']:.2f}")
    print(f"  Exit pressure  (Pe)     : {design['Pe']/1e3:.2f}  kPa")
    print(f"  Ambient pressure (Pa)   : {design['Pa']/1e3:.2f}  kPa")

    # --- Operating conditions ---
    print(f"\n  OPERATING CONDITIONS")
    print(sep2)
    print(f"  Chamber pressure (Pc)   : {design['Pc']/1e6:.3f}  MPa")
    print(f"  Mixture ratio (O/F)     : {design['OF']:.3f}")
    print(f"  Expansion ratio (ε)     : {design['epsilon']:.2f}")
    print(f"  Mean mol. weight (M)    : {design['M_mol']*1e3:.2f}  g/mol")
    print(f"  Gamma (γ)               : {design['gamma']:.4f}")

    # --- Mass flow ---
    print(f"\n  MASS FLOW")
    print(sep2)
    print(f"  Total propellant ṁ      : {design['mdot_total']:.3f}  kg/s")
    print(f"  Oxidiser ṁ_ox           : {design['mdot_ox']:.3f}  kg/s")
    print(f"  Fuel ṁ_fuel             : {design['mdot_fuel']:.3f}  kg/s")

    # --- Nozzle geometry ---
    print(f"\n  NOZZLE GEOMETRY")
    print(sep2)
    print(f"  Throat area   (A_t)     : {design['A_t']*1e4:.4f}  cm²")
    print(f"  Throat diameter (d_t)   : {design['d_throat']*1e3:.2f}  mm")
    print(f"  Exit area     (A_e)     : {design['A_e']*1e4:.3f}  cm²")
    print(f"  Exit diameter  (d_e)    : {design['d_exit']*1e3:.1f}  mm")
    print(f"  Contraction ratio       : {design['contraction_ratio']:.1f}")

    # --- Injector ---
    print(f"\n  INJECTOR DESIGN")
    print(sep2)
    inj_name = design["injector_type"].replace("_", " ").title()
    print(f"  Type                    : {inj_name}")
    print(f"  Number of elements      : {design['n_injectors']}")
    print(f"  Fuel orifice diameter   : {design['d_fuel_orifice']*1e3:.3f}  mm")
    print(f"  Oxidiser orifice diam.  : {design['d_ox_orifice']*1e3:.3f}  mm")
    print(f"  Fuel orifice velocity   : {design['v_fuel_orifice']:.1f}  m/s")
    print(f"  Oxidiser orif. velocity : {design['v_ox_orifice']:.1f}  m/s")
    print(f"  ΔP_fuel / Pc            : {design['dP_fraction']*100:.1f}  %")
    print(f"  ΔP_ox   / Pc            : {design['dP_fraction']*100:.1f}  %")
    print(f"  ΔP_fuel                 : {design['dP_fuel']/1e3:.1f}  kPa")
    print(f"  ΔP_ox                   : {design['dP_ox']/1e3:.1f}  kPa")
    print(f"  Face area utilisation   : {design['injector_face_util']*100:.1f}  %")
    print(f"  Stability margin        : {design['stability_margin']:.2f}  "
          f"(>0 = stable, Hewitt criterion)")

    # --- Score breakdown ---
    print(f"\n  OBJECTIVE SCORE BREAKDOWN")
    print(sep2)
    bd = design["score_breakdown"]
    for k, v in bd.items():
        print(f"  {k:<30s}: {v:+.2f}")
    print(f"  {'TOTAL':30s}: {design['score']:+.2f}")

    print(f"\n  Optimisation time: {design['optimisation_time_s']:.1f}s")
    print(sep)
    print()


# ---------------------------------------------------------------------------
# CLI runner / demo
# ---------------------------------------------------------------------------

def run_demo() -> None:
    """
    Run three canonical design cases to demonstrate the system.
    """
    cases = [
        # (F [N],      Pa [Pa],    propellant,   priority,       label)
        (1_000_000,  101_325,    "LOX-CH4",    "efficiency",  "1 MN LOX-CH4 sea-level booster"),
        (  200_000,       0,    "LOX-LH2",    "efficiency",  "200 kN LOX-LH2 vacuum upper stage"),
        (  500_000,   50_000,   "LOX-RP1",    "simplicity",  "500 kN LOX-RP1 simplicity priority"),
    ]

    for F, Pa, prop, pri, label in cases:
        print(f"\n{'#'*65}")
        print(f"#  CASE: {label}")
        print(f"{'#'*65}")
        try:
            design = design_engine(F=F, Pa=Pa,
                                   propellant_name=prop,
                                   priority=pri,
                                   verbose=True)
            print_report(design)
        except Exception as exc:
            print(f"  [ERROR] {exc}")


if __name__ == "__main__":
    # Parse optional CLI arguments
    import argparse

    parser = argparse.ArgumentParser(description="Liquid Rocket Engine Designer")
    parser.add_argument("--thrust",      type=float, default=1_000_000,
                        help="Required thrust [N] (default: 1 000 000 N = 1 MN)")
    parser.add_argument("--Pa",          type=float, default=101_325,
                        help="Ambient pressure [Pa] (default: 101325 = sea level)")
    parser.add_argument("--propellant",  type=str,   default="LOX-CH4",
                        help="Propellant: LOX-LH2 | LOX-CH4 | LOX-RP1")
    parser.add_argument("--priority",    type=str,   default="efficiency",
                        help="Priority: efficiency | simplicity | mass")
    parser.add_argument("--demo",        action="store_true",
                        help="Run the built-in demo with three canonical cases")

    args = parser.parse_args()

    if args.demo:
        run_demo()
    else:
        design = design_engine(
            F=args.thrust,
            Pa=args.Pa,
            propellant_name=args.propellant,
            priority=args.priority,
            verbose=True,
        )
        print_report(design)
