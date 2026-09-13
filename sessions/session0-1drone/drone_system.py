"""Black-box hovering-drone model for the Natural Language Controller exercise.

This file represents an external engineering package. Students should use
``advance`` and ``V_MAX`` but should not modify the implementation.
"""


V_MAX = 100.0
TIME_STEP = 0.1
MASS = 1.0
GRAVITY = 9.81
VISCOUS_DAMPING = 0.8
MAX_THRUST = 20.0


def advance(
    current_position: float, current_velocity: float, voltage: float
) -> tuple[float, float]:
    """Advance the drone by one time step and return position and velocity.

    Position is measured upward from the floor in metres and velocity is
    measured in metres per second. The motors provide upward thrust only:
    zero voltage means that the drone is in free fall. Motor thrust is
    proportional to voltage and is limited to ``MAX_THRUST``.

    The net force is the upward propulsive force, minus gravity and viscous
    damping. A floor contact prevents the drone from moving below height zero.
    """
    if current_position < 0:
        raise ValueError("current_position must be non-negative")
    if not 0 <= voltage <= V_MAX:
        raise ValueError(f"voltage must be between 0 and {V_MAX}")

    thrust = MAX_THRUST * voltage / V_MAX
    damping_force = VISCOUS_DAMPING * current_velocity
    acceleration = (thrust - MASS * GRAVITY - damping_force) / MASS
    next_velocity = current_velocity + acceleration * TIME_STEP
    next_position = current_position + next_velocity * TIME_STEP

    if next_position < 0:
        return 0.0, max(0.0, next_velocity)
    return next_position, next_velocity
