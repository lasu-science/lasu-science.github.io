"""
injector_model.py
=================
Injector element sizing for bipropellant liquid rocket engines.

Physics basis
-------------
Each injector element (orifice pair for unlike-doublet, triplet, etc.) is modelled
as a sharp-edged orifice using the incompressible Bernoulli equation with an
empirical discharge coefficient Cd:

    ṁ = Cd · A_orifice · √(2 · ρ · ΔP)

where:
    Cd         — discharge coefficient (0.6–0.85 for sharp-edged, 0.7–0.9 for
                 recessed/showerhead; default 0.72 for sharp-edged unlike-doublet)
    A_orifice  — cross-sectional area of a single orifice [m²]
    ρ          — propellant liquid density [kg/m³]
    ΔP         — pressure drop across injector face [Pa]

Design constraints
------------------
  - ΔP_injector ≈ 10–30% of Pc  (too low → combustion instability; too high → pump penalty)
  - Velocity of propellant through orifice: v = ṁ/(ρ·A) ≈ √(2ΔP/ρ) · Cd
  - Number of elements n ≥ n_min (minimum combustion-face coverage)
  - Element diameter ≥ d_min (manufacturing, clogging) and ≤ d_max (jet penetration)

Injector types modelled
-----------------------
  unlike_doublet   — One fuel + one oxidiser orifice aimed to impinge.  Standard,
                     well-characterised.  Cd ≈ 0.72.
  showerhead       — Non-impinging parallel jets.  Simple but less efficient mixing.
                     Cd ≈ 0.80.  Used for upper-stage engines and expander cycles.
  coaxial_swirl    — Oxidiser through centre annulus, fuel as swirling outer sheet.
                     Common for LH2/LOX (e.g. Vulcain, SSME).  More complex to model;
                     treated here as a modified doublet with Cd ≈ 0.68.
"""

from __future__ import annotations
import numpy as np
from dataclasses import dataclass
from propellants import PropellantCombination


# ---------------------------------------------------------------------------
# Injector element types
# ---------------------------------------------------------------------------

@dataclass
class InjectorType:
    name: str
    Cd_fuel: float        # discharge coefficient for fuel orifices
    Cd_ox: float          # discharge coefficient for oxidiser orifices
    # n_orifices_per_element: how many orifices (fuel+ox) per element
    n_fuel_per_element: int
    n_ox_per_element: int
    complexity: int       # 1–5
    description: str


INJECTOR_TYPES: dict[str, InjectorType] = {
    "unlike_doublet": InjectorType(
        name="unlike_doublet",
        Cd_fuel=0.72,
        Cd_ox=0.72,
        n_fuel_per_element=1,
        n_ox_per_element=1,
        complexity=2,
        description="One fuel + one oxidiser jet impinge at an angle.  Classic, versatile.",
    ),
    "showerhead": InjectorType(
        name="showerhead",
        Cd_fuel=0.80,
        Cd_ox=0.80,
        n_fuel_per_element=1,
        n_ox_per_element=1,
        complexity=1,
        description="Parallel non-impinging jets.  Simple, lower mixing efficiency.",
    ),
    "coaxial_swirl": InjectorType(
        name="coaxial_swirl",
        Cd_fuel=0.68,
        Cd_ox=0.68,
        n_fuel_per_element=1,
        n_ox_per_element=1,
        complexity=3,
        description="Coaxial jets with swirl.  Excellent for cryogenic combinations.",
    ),
}


# ---------------------------------------------------------------------------
# Injector sizing result
# ---------------------------------------------------------------------------

@dataclass
class InjectorDesign:
    injector_type: str
    n_elements: int           # number of injector element pairs
    d_fuel_orifice: float     # fuel orifice diameter [m]
    d_ox_orifice: float       # oxidiser orifice diameter [m]
    dP_fuel: float            # pressure drop across fuel side [Pa]
    dP_ox: float              # pressure drop across oxidiser side [Pa]
    dP_fraction_fuel: float   # dP_fuel / Pc [-]
    dP_fraction_ox: float     # dP_ox  / Pc [-]
    v_fuel: float             # fuel orifice velocity [m/s]
    v_ox: float               # oxidiser orifice velocity [m/s]
    mdot_per_element: float   # total propellant flow per element pair [kg/s]
    face_area_util: float     # fraction of injector face area used by orifices
    stability_margin: float   # simplified Hewitt stability parameter estimate


# ---------------------------------------------------------------------------
# Core injector design function
# ---------------------------------------------------------------------------

def design_injectors(propellant: PropellantCombination,
                     OF: float,
                     mdot_total: float,
                     Pc: float,
                     A_chamber: float,
                     injector_type_name: str = "unlike_doublet",
                     dP_fraction: float = 0.20,
                     n_elements_hint: int | None = None) -> InjectorDesign:
    """
    Size the injector elements for the given mass flow conditions.

    Args:
        propellant         : propellant combination (for liquid densities)
        OF                 : oxidiser-to-fuel mixture ratio
        mdot_total         : total propellant mass flow rate [kg/s]
        Pc                 : chamber pressure [Pa]
        A_chamber          : chamber cross-sectional area [m²]
                             (used to estimate combustion face utilisation)
        injector_type_name : one of the keys in INJECTOR_TYPES
        dP_fraction        : ΔP as a fraction of Pc (0.10–0.30)
        n_elements_hint    : if given, start from this element count; otherwise auto

    Returns:
        InjectorDesign dataclass
    """
    inj_type = INJECTOR_TYPES[injector_type_name]
    dP_fraction = float(np.clip(dP_fraction, 0.10, 0.30))

    dP_fuel = dP_fraction * Pc    # Pa
    dP_ox   = dP_fraction * Pc    # Pa — same fraction assumed for both circuits

    rho_fuel = propellant.rho_fuel
    rho_ox   = propellant.rho_oxidizer

    # --- Mass flows per stream ---
    mdot_fuel = mdot_total / (1.0 + OF)
    mdot_ox   = mdot_total - mdot_fuel

    # --- Orifice velocity from Bernoulli ---
    # v = Cd · √(2·ΔP/ρ)
    v_fuel = inj_type.Cd_fuel * np.sqrt(2.0 * dP_fuel / rho_fuel)
    v_ox   = inj_type.Cd_ox  * np.sqrt(2.0 * dP_ox   / rho_ox)

    # --- Single-orifice area ---
    # Starting point: aim for n_target elements for good face coverage
    # Empirical: combustion face should have ~40–70% orifice packing
    # Use a target orifice diameter range [d_min, d_max]
    d_min = 0.5e-3    # 0.5 mm — manufacturing limit
    d_max = 4.0e-3    # 4.0 mm — jet penetration / atomisation limit

    if n_elements_hint is not None:
        n_elements = max(4, int(n_elements_hint))
        # Back-calculate orifice diameter from this element count
        mdot_fuel_per_el = mdot_fuel / (n_elements * inj_type.n_fuel_per_element)
        mdot_ox_per_el   = mdot_ox   / (n_elements * inj_type.n_ox_per_element)
        A_fuel = mdot_fuel_per_el / (inj_type.Cd_fuel * rho_fuel * v_fuel / inj_type.Cd_fuel)
        # Simpler: A = mdot / (rho * v) where v is from Bernoulli
        A_fuel = mdot_fuel_per_el / (rho_fuel * v_fuel)
        A_ox   = mdot_ox_per_el   / (rho_ox   * v_ox)
        d_fuel = np.sqrt(4.0 * A_fuel / np.pi)
        d_ox   = np.sqrt(4.0 * A_ox   / np.pi)
    else:
        # Auto-size: target fuel orifice diameter at d_target = 1.5 mm
        d_target_fuel = float(np.clip(1.5e-3, d_min, d_max))
        A_fuel_single = np.pi * d_target_fuel**2 / 4.0
        # Mass flow per single fuel orifice
        mdot_fuel_per_orifice = rho_fuel * v_fuel * A_fuel_single
        # Number of fuel orifices total (rounded up)
        n_fuel_orifices = max(4, int(np.ceil(mdot_fuel / mdot_fuel_per_orifice)))
        # Elements = n_fuel_orifices / n_fuel_per_element
        n_elements = max(4, int(np.ceil(n_fuel_orifices / inj_type.n_fuel_per_element)))

        # Recalculate diameters with rounded n_elements
        mdot_fuel_per_el = mdot_fuel / (n_elements * inj_type.n_fuel_per_element)
        mdot_ox_per_el   = mdot_ox   / (n_elements * inj_type.n_ox_per_element)
        A_fuel = mdot_fuel_per_el / (rho_fuel * v_fuel)
        A_ox   = mdot_ox_per_el   / (rho_ox   * v_ox)
        d_fuel = np.sqrt(4.0 * A_fuel / np.pi)
        d_ox   = np.sqrt(4.0 * A_ox   / np.pi)

    # Clamp diameters to practical range
    d_fuel = float(np.clip(d_fuel, d_min, d_max))
    d_ox   = float(np.clip(d_ox,   d_min, d_max))

    # --- Injector face utilisation ---
    # Fraction of chamber face covered by orifice openings
    A_fuel_total = n_elements * inj_type.n_fuel_per_element * np.pi * d_fuel**2 / 4.0
    A_ox_total   = n_elements * inj_type.n_ox_per_element   * np.pi * d_ox**2   / 4.0
    face_util    = (A_fuel_total + A_ox_total) / A_chamber if A_chamber > 0 else 0.0

    # --- Hewitt stability parameter (simplified) ---
    # Rupe (1953) / Hewitt (1962): stability improves with dP/Pc > 0.10
    # Here we compute a simple margin metric: (dP/Pc) / 0.10 - 1
    stability_margin = dP_fraction / 0.10 - 1.0   # 0 = at stability limit

    return InjectorDesign(
        injector_type=injector_type_name,
        n_elements=n_elements,
        d_fuel_orifice=d_fuel,
        d_ox_orifice=d_ox,
        dP_fuel=dP_fuel,
        dP_ox=dP_ox,
        dP_fraction_fuel=dP_fuel / Pc,
        dP_fraction_ox=dP_ox / Pc,
        v_fuel=v_fuel,
        v_ox=v_ox,
        mdot_per_element=mdot_total / n_elements,
        face_area_util=float(np.clip(face_util, 0.0, 1.0)),
        stability_margin=stability_margin,
    )


def best_injector_type_for_propellant(fuel_name: str) -> str:
    """
    Return the recommended injector type for a given fuel.
    Based on industry practice.
    """
    if fuel_name == "LH2":
        return "coaxial_swirl"
    elif fuel_name in ("LCH4",):
        return "unlike_doublet"    # or coaxial; doublet common for Raptor-class
    else:
        return "unlike_doublet"    # standard for RP-1 engines


def injector_pressure_drop_penalty(dP_fraction: float) -> float:
    """
    Compute a score penalty for injector pressure drop fraction.

    Optimal range: 0.15–0.25
      - Below 0.10: combustion instability risk (+large penalty)
      - 0.10–0.15:  acceptable but marginal
      - 0.15–0.25:  optimal window
      - 0.25–0.30:  acceptable, small pump power penalty
      - Above 0.30: pump oversizing penalty

    Returns a negative penalty value (0 = no penalty).
    """
    if dP_fraction < 0.10:
        return -50.0 * (0.10 - dP_fraction) / 0.10   # severe instability penalty
    elif dP_fraction <= 0.25:
        return 0.0    # optimal range
    else:
        return -20.0 * (dP_fraction - 0.25) / 0.05   # pump oversizing penalty
