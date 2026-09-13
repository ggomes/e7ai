"""Black-box tank model for the Natural Language Controller exercise.

This file represents an external engineering package. Students should use its
public functions but should not modify its implementation.
"""


def set_valve_position(current_level: float, target_level: float) -> float:
    """Return a valve command that moves ``current_level`` toward ``target_level``.

    Levels are percentages from 0 to 100. The returned valve command is also
    expressed as a percentage:

    * a negative command opens the drain valve;
    * a positive command opens the fill valve;
    * zero leaves both valves closed.

    The internal control law is intentionally hidden from the exercise. The
    command is limited to the safe range [-100, 100].
    """
    if not 0 <= current_level <= 100:
        raise ValueError("current_level must be between 0 and 100")
    if not 0 <= target_level <= 100:
        raise ValueError("target_level must be between 0 and 100")

    error = target_level - current_level
    command = 8 * error
    return max(-100.0, min(100.0, command))


def advance(current_level: float, valve_position: float) -> float:
    """Advance the tank by one time step and return its new level.

    This simple model includes a small leak toward an ambient level. The
    dynamics are supplied so that students can focus on the controller.
    """
    if not 0 <= current_level <= 100:
        raise ValueError("current_level must be between 0 and 100")
    if not -100 <= valve_position <= 100:
        raise ValueError("valve_position must be between -100 and 100")

    ambient_level = 20.0
    leak = 0.02 * (ambient_level - current_level)
    valve_effect = 0.08 * valve_position
    next_level = current_level + leak + valve_effect
    return max(0.0, min(100.0, next_level))
