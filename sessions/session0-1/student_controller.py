
def controller(hk, vk, hbar, drone_parms):
    height_error = hbar - hk
    weight = drone_parms['m'] * drone_parms['g']
    tau = weight + 10 * height_error

    if vk > 0.0 and (hbar - hk) < 0:
        tau = 0

    if vk < 0.0 and (hbar - hk) > 0.15:
        tau = drone_parms['tau_max']

    if tau < 0.0:
        tau = 0.0

    return tau
