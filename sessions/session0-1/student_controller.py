
def controller(hk, vk, hbar, drone_parms):
    if hk < hbar:
        tau = drone_parms['tau_max']
    else:
        tau = 0.0
    return tau
