"""Student starter file for the hovering-drone controller exercise."""

import matplotlib.pyplot as plt

import drone_system


def controller(
    target_height: float, current_position: float, current_velocity: float
) -> float:
    """Return the motor voltage for the current measured state."""
    # Replace these examples with your own precise control rules.
    # If the drone is substantially below the target, ...
    # If it is moving upward too quickly, ...
    # If it is close to the target and nearly stationary, ...
    # Remember that zero voltage is free fall and that voltage cannot be
    # negative. The controller must use position and velocity feedback.
    if current_position < target_height:
        voltage = drone_system.V_MAX
    else:
        voltage = 0.0
    return max(0.0, min(drone_system.V_MAX, voltage))


target_height = 10.0
current_position = 0.0
current_velocity = 0.0
tolerance = 0.15
required_settling_step = 70
number_of_steps = 100

positions = [current_position]
velocities = [current_velocity]

for step in range(1, number_of_steps + 1):
    voltage = controller(
        target_height, current_position, current_velocity
    )
    current_position, current_velocity = drone_system.advance(
        current_position, current_velocity, voltage
    )
    positions.append(current_position)
    velocities.append(current_velocity)

    print(
        f"step={step:03d}  position={current_position:7.3f} m  "
        f"velocity={current_velocity:7.3f} m/s  voltage={voltage:6.2f} V"
    )


within_tolerance = [
    abs(position - target_height) <= tolerance for position in positions
]
settling_step = None
for step in range(len(positions)):
    if all(within_tolerance[step:]):
        settling_step = step
        break

meets_specification = (
    settling_step is not None
    and settling_step <= required_settling_step
)
if meets_specification:
    print(f"PASS: settled by step {settling_step}")
else:
    print(
        "FAIL: the drone did not remain within the tolerance band "
        f"by step {required_settling_step}"
    )

steps = range(number_of_steps + 1)
plt.figure()
plt.plot(steps, positions, label="drone height")
plt.axhline(target_height, color="black", linestyle="--",
            label="target height")
plt.fill_between(
    steps,
    target_height - tolerance,
    target_height + tolerance,
    color="green",
    alpha=0.15,
    label="allowed band",
)
plt.axvline(
    required_settling_step,
    color="red",
    linestyle=":",
    label="settling deadline",
)
plt.xlabel("Step (0.1 s)")
plt.ylabel("Height (m)")
plt.title("Hovering drone response")
plt.legend()
plt.tight_layout()
plt.savefig("drone_response.png", dpi=150)
plt.show()


# After running and testing your controller, add a short explanation here:
# - What did Copilot suggest for the position/velocity feedback?
# - What did you change?
# - How did you verify that the controller respects the voltage limits and
#   follows your rules?
