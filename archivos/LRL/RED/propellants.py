"""
propellants.py
==============
Propellant thermochemical property database for the rocket engine designer.

Properties are derived from NASA CEA curve-fits and open literature data.
Each propellant combination stores:
  - Characteristic adiabatic flame temperature T_c as a function of O/F
  - Effective ratio of specific heats (gamma) as a function of O/F
  - Mean molecular weight of combustion products (g/mol) as a function of O/F
  - Liquid densities for fuel and oxidizer (kg/m³) — used for injector sizing
  - Nominal O/F range valid for the curve fits
  - Stoichiometric O/F (reference for off-ratio penalties)

All T_c(OF), gamma(OF), Mmol(OF) are modelled as piecewise polynomials fitted
to CEA output at Pc ≈ 10 MPa.  At design time the thermodynamics module scales
these slightly with chamber pressure using simplified corrections.
"""

from __future__ import annotations
import numpy as np
from dataclasses import dataclass, field
from typing import Callable


# ---------------------------------------------------------------------------
# Helper: build a quadratic peak function centred at OF_peak
# ---------------------------------------------------------------------------

def _quadratic_peak(OF_peak: float, T_peak: float, T_low: float, T_high: float,
                    OF_min: float, OF_max: float) -> Callable[[float], float]:
    """
    Return a callable T(OF) that is a quadratic (inverted parabola) with:
      T(OF_peak) = T_peak
      T(OF_min)  = T_low
      T(OF_max)  = T_high
    Outside [OF_min, OF_max] the function is clamped to a linear extrapolation
    to discourage the optimiser from wandering off-range.
    """
    # Fit a quadratic through three points: (OF_min,T_low),(OF_peak,T_peak),(OF_max,T_high)
    A = np.array([
        [OF_min**2, OF_min, 1],
        [OF_peak**2, OF_peak, 1],
        [OF_max**2, OF_max, 1],
    ])
    b = np.array([T_low, T_peak, T_high])
    coeffs = np.linalg.solve(A, b)

    def T_of_OF(OF: float) -> float:
        OF_clamped = float(np.clip(OF, OF_min, OF_max))
        return float(np.polyval(coeffs, OF_clamped))

    return T_of_OF


# ---------------------------------------------------------------------------
# Dataclass for a propellant combination
# ---------------------------------------------------------------------------

@dataclass
class PropellantCombination:
    """Full thermochemical description of a bipropellant combination."""

    name: str                          # e.g. "LOX-CH4"
    fuel_name: str
    oxidizer_name: str

    # O/F range [min, stoich, max] — hard bounds for the optimiser
    OF_min: float
    OF_stoich: float
    OF_max: float
    OF_optimal_Isp: float              # O/F that maximises vacuum Isp

    # Liquid densities [kg/m³] for injector pressure-drop calculation
    rho_fuel: float                    # kg/m³  (saturated liquid at typical inlet T)
    rho_oxidizer: float                # kg/m³

    # Vapour pressure of fuel (Pa) — used for cavitation margin check
    Pv_fuel: float

    # Callable thermochemical property curves (functions of O/F)
    _Tc_func:     Callable[[float], float] = field(repr=False)
    _gamma_func:  Callable[[float], float] = field(repr=False)
    _Mmol_func:   Callable[[float], float] = field(repr=False)

    # Cycle suitability flags (used by cycle_selector.py)
    suitable_cycles: list[str] = field(default_factory=list)

    # Approximate boiling points (K) — relevant for expander-cycle feasibility
    Tbp_fuel: float = 0.0
    Tbp_oxidizer: float = 0.0

    # Engine heritage note (informational)
    heritage: str = ""

    # -----------------------------------------------------------------------
    # Public interface
    # -----------------------------------------------------------------------

    def T_c(self, OF: float) -> float:
        """Adiabatic flame temperature [K] at given O/F (Pc ≈ 10 MPa reference)."""
        return float(self._Tc_func(OF))

    def gamma(self, OF: float) -> float:
        """Ratio of specific heats [-] of combustion products at given O/F."""
        return float(self._gamma_func(OF))

    def M_mol(self, OF: float) -> float:
        """Mean molecular weight of products [kg/mol] at given O/F."""
        return float(self._Mmol_func(OF)) * 1e-3   # convert g/mol → kg/mol

    def validate_OF(self, OF: float) -> bool:
        return self.OF_min <= OF <= self.OF_max


# ---------------------------------------------------------------------------
# LOX / LH2  (Liquid Oxygen + Liquid Hydrogen)
# ---------------------------------------------------------------------------

_lh2_Tc   = _quadratic_peak(5.5, 3533.0, 2700.0, 2900.0, 3.5, 8.0)
_lh2_gamma = lambda OF: float(np.interp(OF, [3.5, 5.0, 5.5, 6.0, 8.0],
                                             [1.22, 1.24, 1.26, 1.26, 1.27]))
_lh2_Mmol  = lambda OF: float(np.interp(OF, [3.5, 5.0, 5.5, 6.0, 8.0],
                                             [8.5, 9.5, 10.0, 10.8, 12.5]))

LOX_LH2 = PropellantCombination(
    name="LOX-LH2",
    fuel_name="LH2",
    oxidizer_name="LOX",
    OF_min=3.5,
    OF_stoich=8.0,
    OF_max=8.0,
    OF_optimal_Isp=5.5,
    rho_fuel=71.0,           # liquid H₂ at 20 K
    rho_oxidizer=1141.0,     # liquid O₂ at 90 K
    Pv_fuel=101325.0,        # essentially at boiling point
    _Tc_func=_lh2_Tc,
    _gamma_func=_lh2_gamma,
    _Mmol_func=_lh2_Mmol,
    suitable_cycles=["expander", "staged_combustion", "gas_generator"],
    Tbp_fuel=20.3,
    Tbp_oxidizer=90.2,
    heritage="SSME, RL-10, Vulcain, J-2",
)


# ---------------------------------------------------------------------------
# LOX / CH4  (Liquid Oxygen + Liquid Methane)
# ---------------------------------------------------------------------------

_ch4_Tc   = _quadratic_peak(3.5, 3553.0, 2900.0, 3100.0, 2.0, 5.0)
_ch4_gamma = lambda OF: float(np.interp(OF, [2.0, 3.0, 3.5, 4.0, 5.0],
                                             [1.21, 1.23, 1.23, 1.24, 1.25]))
_ch4_Mmol  = lambda OF: float(np.interp(OF, [2.0, 3.0, 3.5, 4.0, 5.0],
                                             [16.0, 18.5, 20.0, 21.5, 23.5]))

LOX_CH4 = PropellantCombination(
    name="LOX-CH4",
    fuel_name="LCH4",
    oxidizer_name="LOX",
    OF_min=2.0,
    OF_stoich=4.0,
    OF_max=5.0,
    OF_optimal_Isp=3.5,
    rho_fuel=422.6,          # liquid CH₄ at 111 K
    rho_oxidizer=1141.0,
    Pv_fuel=101325.0,
    _Tc_func=_ch4_Tc,
    _gamma_func=_ch4_gamma,
    _Mmol_func=_ch4_Mmol,
    suitable_cycles=["staged_combustion", "gas_generator", "expander"],
    Tbp_fuel=111.7,
    Tbp_oxidizer=90.2,
    heritage="Raptor (SpaceX), BE-4 (Blue Origin), Prometheus (ArianeGroup)",
)


# ---------------------------------------------------------------------------
# LOX / RP-1  (Liquid Oxygen + Refined Petroleum)
# ---------------------------------------------------------------------------

_rp1_Tc   = _quadratic_peak(2.7, 3670.0, 3000.0, 3200.0, 1.8, 4.0)
_rp1_gamma = lambda OF: float(np.interp(OF, [1.8, 2.4, 2.7, 3.0, 4.0],
                                             [1.22, 1.24, 1.24, 1.245, 1.25]))
_rp1_Mmol  = lambda OF: float(np.interp(OF, [1.8, 2.4, 2.7, 3.0, 4.0],
                                             [20.0, 22.5, 23.5, 24.5, 26.0]))

LOX_RP1 = PropellantCombination(
    name="LOX-RP1",
    fuel_name="RP-1",
    oxidizer_name="LOX",
    OF_min=1.8,
    OF_stoich=3.4,
    OF_max=4.0,
    OF_optimal_Isp=2.7,
    rho_fuel=820.0,          # RP-1 at 298 K
    rho_oxidizer=1141.0,
    Pv_fuel=300.0,           # negligible vapour pressure at room temp
    _Tc_func=_rp1_Tc,
    _gamma_func=_rp1_gamma,
    _Mmol_func=_rp1_Mmol,
    suitable_cycles=["gas_generator", "staged_combustion"],
    Tbp_fuel=490.0,          # approximate mid-cut boiling point
    Tbp_oxidizer=90.2,
    heritage="F-1, Merlin, RD-180, NK-33",
)


# ---------------------------------------------------------------------------
# Registry — extend here to add new propellant combinations
# ---------------------------------------------------------------------------

PROPELLANT_REGISTRY: dict[str, PropellantCombination] = {
    "LOX-LH2":  LOX_LH2,
    "LOX-CH4":  LOX_CH4,
    "LOX-RP1":  LOX_RP1,
}


def get_propellant(name: str) -> PropellantCombination:
    """Look up a propellant combination by name (case-insensitive)."""
    key = name.upper().replace("_", "-")
    if key not in PROPELLANT_REGISTRY:
        available = list(PROPELLANT_REGISTRY.keys())
        raise ValueError(f"Unknown propellant '{name}'. Available: {available}")
    return PROPELLANT_REGISTRY[key]
