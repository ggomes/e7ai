"""Single-function solver for the Automated Parameter Sweeps exercise."""

import math


def truss_stress(load_kN: float, beam_diameter_mm: float) -> float:
    """Return axial stress in MPa for a circular beam.

    ``load_kN`` is the applied load in kilonewtons and
    ``beam_diameter_mm`` is the beam diameter in millimeters.
    """
    load_N = load_kN * 1_000.0
    diameter_m = beam_diameter_mm / 1_000.0
    cross_section_m2 = math.pi * diameter_m**2 / 4.0
    stress_Pa = load_N / cross_section_m2
    return stress_Pa / 1_000_000.0
