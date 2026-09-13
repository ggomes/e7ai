"""Projectile trajectory starter with an intentional unit mismatch."""
import math
# The solver expects distance_m in meters; the caller supplies feet below.
def trajectory_at_distance(distance_m, speed_mps, angle_deg, gravity=9.81):
    angle_rad = math.radians(angle_deg)
    horizontal_speed = speed_mps * math.cos(angle_rad)
    flight_time = distance_m / horizontal_speed
    height_m = speed_mps * math.sin(angle_rad) * flight_time
    height_m -= 0.5 * gravity * flight_time**2
    return flight_time, height_m
launch_speed_mps = 30.0
launch_angle_deg = 45.0
target_distance_ft = 300.0
time_s, height_m = trajectory_at_distance(target_distance_ft, launch_speed_mps, launch_angle_deg)
print(f"At {target_distance_ft:.0f} ft: t={time_s:.2f} s, height={height_m:.2f} m")
