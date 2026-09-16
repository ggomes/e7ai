
def C(h, v, hbar, drone_params):


    if h<hbar:
        thrust = drone_params['max_thrust']
    else:
        thrust = 0

    return thrust
