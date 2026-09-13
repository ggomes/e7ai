"""Student starter file for the Natural Language Controller exercise."""

import matplotlib.pyplot as plt

import tank_system


desired_level = 70.0
current_level = 10.0
tolerance = 1.5
required_settling_step = 15
number_of_steps = 30

levels = [current_level]

for step in range(1, number_of_steps + 1):
    # Replace these examples with your own precise control rules.
    # If the water level is substantially above the desired level, ...
    # If the water level is substantially below the desired level, ...
    # Otherwise, ...
    # Also account for the fact that the tank has a persistent leak.
    #
    # Describe the rules first, then place the cursor in this block and press
    # Tab to ask Copilot for an if/elif/else completion.
    if current_level > desired_level * 1.10:
        control_target = desired_level
    else:
        control_target = desired_level

    valve_position = tank_system.set_valve_position(
        current_level, control_target
    )
    current_level = tank_system.advance(current_level, valve_position)
    levels.append(current_level)

    print(
        f"step={step:02d}  level={current_level:6.2f}%  "
        f"valve={valve_position:6.2f}%"
    )


within_tolerance = [
    abs(level - desired_level) <= tolerance for level in levels
]
settling_step = None
for step in range(len(levels)):
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
        "FAIL: the tank did not remain within the tolerance band "
        f"by step {required_settling_step}"
    )

steps = range(number_of_steps + 1)
plt.figure()
plt.plot(steps, levels, label="tank level")
plt.axhline(desired_level, color="black", linestyle="--", label="desired level")
plt.fill_between(
    steps,
    desired_level - tolerance,
    desired_level + tolerance,
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
plt.xlabel("Step (s)")
plt.ylabel("Tank level (%)")
plt.title("Tank response")
plt.legend()
plt.tight_layout()
plt.savefig("tank_response.png", dpi=150)
plt.show()


# After running and testing your controller, add a short explanation here:
# - What did Copilot suggest?
# - What did you change?
# - How did you verify that the controller follows your rules?
