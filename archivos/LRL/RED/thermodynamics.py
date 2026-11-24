"""
thermodynamics.py
=================
Rocket nozzle thermodynamics and isentropic flow relations.

All equations are standard compressible-flow / rocket-propulsion theory from:
  - Sutton & Biblarz, "Rocket Propulsion Elements" (8th ed.)
  - Anderson, "Modern Compressible Flow"
  - NASA SP-8120 (Liquid Rocket Engine Turbopump Inducers)

Key quantities computed here:
  c*   — characteristic velocity [m/s]
  Cf   — thrust coefficient [-]
  Isp  — specific impulse [s]
  ve   — effective exhaust velocity [m/s]
  A_t  — nozzle throat area [m²]
  A_e  — nozzle exit area [m²]
  Pe   — exit static pressure [Pa]
  Me   — exit Mach number [-]
"""

from __future__ import annotations
import numpy as np
from scipy.optimize import brentq
from propellants import PropellantCombination

# Standard gravity [m/s²]
G0: float = 9.80665
# Universal gas constant [J/(mol·K)]
R_UNIV: float = 8314.46261815324   # J/(kmol·K) → we use kg/mol so 8.314 J/(mol·K)
R_UNIV_JMOL: float = 8.314462618   # J/(mol·K)


# ---------------------------------------------------------------------------
# Isentropic flow helpers
# ---------------------------------------------------------------------------

def area_mach_ratio(M: float, gamma: float) -> float:
    """
    Area ratio A/A* as a function of Mach number M and gamma.
    Valid for M ≥ 0 (subsonic branch gives same ratio as supersonic).
    """
    t = 1.0 + (gamma - 1.0) / 2.0 * M**2
    exp = (gamma + 1.0) / (2.0 * (gamma - 1.0))
    return (1.0 / M) * ((2.0 / (gamma + 1.0)) * t) ** exp


def mach_from_area_ratio_supersonic(epsilon: float, gamma: float) -> float:
    """
    Solve A/A* = epsilon for supersonic Mach number (M > 1).
    Uses Brent's method.
    """
    if epsilon <= 1.0:
        return 1.0  # at throat
    func = lambda M: area_mach_ratio(M, gamma) - epsilon
    # Supersonic solution is in [1, ~100]; upper bound is generous
    return brentq(func, 1.0 + 1e-8, 200.0, xtol=1e-8, maxiter=200)


def isentropic_pressure_ratio(M: float, gamma: float) -> float:
    """Return p0/p (total-to-static pressure ratio) for given M and gamma."""
    return (1.0 + (gamma - 1.0) / 2.0 * M**2) ** (gamma / (gamma - 1.0))


def exit_pressure(Pc: float, Me: float, gamma: float) -> float:
    """
    Static exit pressure [Pa] assuming Pc ≈ P0 (stagnation pressure in chamber).
    Pe = Pc / (p0/p)(Me)
    """
    return Pc / isentropic_pressure_ratio(Me, gamma)


# ---------------------------------------------------------------------------
# Combustion & characteristic velocity c*
# ---------------------------------------------------------------------------

def gamma_function(gamma: float) -> float:
    """
    Vandenkerckhove function Γ(γ).
    Γ = √γ · (2/(γ+1))^((γ+1)/(2(γ-1)))
    Appears in the ideal mass flow and c* formulae.
    """
    exp = (gamma + 1.0) / (2.0 * (gamma - 1.0))
    return np.sqrt(gamma) * (2.0 / (gamma + 1.0)) ** exp


def characteristic_velocity(Tc: float, M_mol: float, gamma: float) -> float:
    """
    Ideal characteristic velocity c* [m/s].

    c* = (1/Γ) · √(R_spec · Tc)

    where R_spec = R_univ / M_mol  [J/(kg·K)]
    and   Γ = Vandenkerckhove function.

    c* is the figure of merit for the combustion process, independent of nozzle
    geometry.  Higher Tc and lower M_mol both increase c*.

    Args:
        Tc    : adiabatic flame temperature [K]
        M_mol : mean molecular weight of products [kg/mol]
        gamma : ratio of specific heats [-]
    """
    R_spec = R_UNIV_JMOL / M_mol        # specific gas constant [J/(kg·K)]
    Gamma  = gamma_function(gamma)
    return np.sqrt(R_spec * Tc) / Gamma


def pressure_correction_Tc(Tc_ref: float, Pc: float, Pc_ref: float = 10e6) -> float:
    """
    Approximate chamber-pressure correction to combustion temperature.
    At higher Pc, three-body recombination is more complete → slightly higher Tc.
    Correction is small (~1–2% over typical Pc range) but physically motivated.
    Uses a log scaling based on CEA sensitivity data.
    """
    delta = 0.02 * np.log10(Pc / Pc_ref)   # ±2% per decade of Pc
    return Tc_ref * (1.0 + delta)


# ---------------------------------------------------------------------------
# Thrust coefficient Cf
# ---------------------------------------------------------------------------

def thrust_coefficient(Pc: float, Pe: float, Pa: float,
                       epsilon: float, gamma: float) -> float:
    """
    Ideal thrust coefficient Cf [-].

    Cf = √[ 2γ²/(γ-1) · (2/(γ+1))^((γ+1)/(γ-1)) · (1-(Pe/Pc)^((γ-1)/γ)) ]
         + (Pe - Pa)/Pc · ε

    The first term is the momentum thrust component; the second is the
    pressure thrust component.  At sea-level optimum expansion Pe = Pa,
    the pressure term vanishes and Cf is maximised for a given ε.

    Args:
        Pc      : chamber pressure [Pa]
        Pe      : exit static pressure [Pa]
        Pa      : ambient pressure [Pa]
        epsilon : nozzle area ratio A_e/A_t [-]
        gamma   : ratio of specific heats [-]
    """
    A = 2.0 * gamma**2 / (gamma - 1.0)
    B = (2.0 / (gamma + 1.0)) ** ((gamma + 1.0) / (gamma - 1.0))
    C = 1.0 - (Pe / Pc) ** ((gamma - 1.0) / gamma)
    momentum_term = np.sqrt(A * B * C)
    pressure_term = (Pe - Pa) / Pc * epsilon
    return momentum_term + pressure_term


# ---------------------------------------------------------------------------
# Nozzle geometry
# ---------------------------------------------------------------------------

def throat_area(mdot: float, c_star: float, Pc: float) -> float:
    """
    Nozzle throat area [m²] from continuity and the definition of c*.
    A_t = mdot · c* / Pc
    """
    return mdot * c_star / Pc


def exit_area(A_t: float, epsilon: float) -> float:
    """Exit area [m²] = expansion ratio × throat area."""
    return A_t * epsilon


def throat_diameter(A_t: float) -> float:
    """Throat diameter [m] from circular throat area."""
    return np.sqrt(4.0 * A_t / np.pi)


def exit_diameter(A_e: float) -> float:
    """Exit diameter [m] from circular exit area."""
    return np.sqrt(4.0 * A_e / np.pi)


# ---------------------------------------------------------------------------
# Optimal expansion ratio (maximises vacuum Isp)
# ---------------------------------------------------------------------------

def optimal_expansion_ratio(Pc: float, Pa: float, gamma: float,
                             epsilon_min: float = 2.0,
                             epsilon_max: float = 300.0) -> float:
    """
    Find the expansion ratio that achieves Pe = Pa (optimum expansion).
    Solve:  exit_pressure(Pc, Me(ε), γ) = Pa  for ε.

    If Pa = 0 (vacuum), returns epsilon_max (unbounded; caller must cap it).
    """
    if Pa <= 0.0:
        return epsilon_max

    def residual(eps):
        Me = mach_from_area_ratio_supersonic(eps, gamma)
        Pe_calc = exit_pressure(Pc, Me, gamma)
        return Pe_calc - Pa

    # Check feasibility: at epsilon_min, Pe should be > Pa; at epsilon_max, Pe < Pa
    Me_min = mach_from_area_ratio_supersonic(epsilon_min, gamma)
    Pe_min_val = exit_pressure(Pc, Me_min, gamma)
    if Pe_min_val <= Pa:
        return epsilon_min   # under-expanded even at min epsilon

    Me_max = mach_from_area_ratio_supersonic(epsilon_max, gamma)
    Pe_max_val = exit_pressure(Pc, Me_max, gamma)
    if Pe_max_val >= Pa:
        return epsilon_max   # over-expanded even at max epsilon (vacuum-like)

    return brentq(residual, epsilon_min, epsilon_max, xtol=1e-6, maxiter=200)


# ---------------------------------------------------------------------------
# High-level thermodynamic state
# ---------------------------------------------------------------------------

def compute_nozzle_state(propellant: PropellantCombination,
                         OF: float,
                         Pc: float,
                         Pa: float,
                         epsilon: float | None = None,
                         epsilon_min: float = 2.0,
                         epsilon_max: float = 200.0) -> dict:
    """
    Compute the full nozzle thermodynamic state for given operating conditions.

    Args:
        propellant  : PropellantCombination instance
        OF          : oxidiser-to-fuel mixture ratio [-]
        Pc          : chamber pressure [Pa]
        Pa          : ambient pressure [Pa]
        epsilon     : expansion ratio A_e/A_t; if None, optimal expansion is used
        epsilon_min : minimum allowed expansion ratio
        epsilon_max : maximum allowed expansion ratio

    Returns:
        dict with keys: Tc, gamma, M_mol, R_spec, c_star, Me, Pe, epsilon,
                        Cf, Isp, ve
    """
    # --- Thermochemical properties at this O/F ---
    Tc_ref = propellant.T_c(OF)
    gamma  = propellant.gamma(OF)
    M_mol  = propellant.M_mol(OF)          # [kg/mol]

    # Apply chamber-pressure correction to Tc
    Tc = pressure_correction_Tc(Tc_ref, Pc)

    R_spec = R_UNIV_JMOL / M_mol           # specific gas constant [J/(kg·K)]
    c_star = characteristic_velocity(Tc, M_mol, gamma)

    # --- Nozzle expansion ---
    if epsilon is None:
        epsilon = optimal_expansion_ratio(Pc, Pa, gamma,
                                          epsilon_min=epsilon_min,
                                          epsilon_max=epsilon_max)
    epsilon = float(np.clip(epsilon, epsilon_min, epsilon_max))

    Me = mach_from_area_ratio_supersonic(epsilon, gamma)
    Pe = exit_pressure(Pc, Me, gamma)
    Cf = thrust_coefficient(Pc, Pe, Pa, epsilon, gamma)

    # Specific impulse and effective exhaust velocity
    Isp = Cf * c_star / G0       # [s]
    ve  = Isp * G0               # effective exhaust velocity [m/s]

    return {
        "Tc":      Tc,
        "gamma":   gamma,
        "M_mol":   M_mol,
        "R_spec":  R_spec,
        "c_star":  c_star,
        "Me":      Me,
        "Pe":      Pe,
        "epsilon": epsilon,
        "Cf":      Cf,
        "Isp":     Isp,
        "ve":      ve,
    }


def mass_flow_from_thrust(F: float, ve: float) -> float:
    """
    Total propellant mass flow rate [kg/s] from thrust and exhaust velocity.
    F = mdot · ve  (momentum equation, with pressure thrust included in ve)
    """
    return F / ve


def split_mass_flow(mdot_total: float, OF: float) -> tuple[float, float]:
    """
    Split total mass flow into oxidiser and fuel streams.
    Returns (mdot_ox, mdot_fuel) in [kg/s].
    """
    mdot_fuel = mdot_total / (1.0 + OF)
    mdot_ox   = mdot_total - mdot_fuel
    return mdot_ox, mdot_fuel
