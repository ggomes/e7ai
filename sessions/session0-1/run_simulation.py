import matplotlib.pyplot as plt
import numpy as np
from feedback_controller import C

# parameters of the drone ...................
drone_parms = {
    'vmax' : 3.5,      # [m/s] maximum upward velocity
    'm' : 0.7,         # [kg] mass of the drone 
    'g' : 9.81,        # [m/s2] acceleration of gravity
    'nu' : 0.8,        # [kg/s] friction coefficient
    'max_thrust' : 10  # [N] maximum thrust
}

# parameters of the simulation .................
hbar =  5.0                 # [m] target height
h_tolerance = 0.15          # [m] settling tolerance
target_settling_time = 3.5  # [s] target settline time
dt = 0.01                   # [s] simulation time step
T = 7                       # [s] total simulation time


# allocate and initialize .........................
K = round(T/dt)
h = np.zeros(K)
v = np.zeros(K)
tau_c = np.zeros(K)
h[0] = 0
v[0] = 0

# auxiliary variables .....................
m = drone_parms['m']
nu = drone_parms['nu']
g = drone_parms['g']
vmax = drone_parms['vmax'] 

# step through time ........................
for k in range(K-1):

    # get upward thrust from controller
    tau = C(h[k], v[k], hbar, drone_parms)

    # clipped upward thrust 
    tau_c[k] = max(0.0,min(tau,drone_parms['max_thrust']))

    # speed and height update 
    v_next = v[k] + dt*(tau_c[k] - m*g - nu*v[k])/m
    v_next = min(v_next,vmax)
    h_next = h[k] + v_next * dt

    # hit the floor
    if h_next<0:
        break

    # store
    h[k+1] = h_next
    v[k+1] = v_next

# find settling time  .................
not_converged = np.abs(h-hbar)>h_tolerance
if np.all(not_converged):
    settledat = None
else:
    settledat = np.where(not_converged)[0][-1]

# check success ...........................
t = np.arange(0,T,dt)
success = settledat is not None and t[settledat]<=target_settling_time
if success:
    print(f"✅ Settled after {t[settledat]:.2f} seconds")
else:
    print("❌ Failed to settle.")

# plot .....................................
fig, axs = plt.subplots(nrows=2,sharex=True)

ax = axs[0]
ax.plot(t, h, linewidth=2,label="drone height")
ax.axhline(hbar, color="black", linewidth=1,linestyle="--",label="target height")
ax.fill_between(
    t,
    hbar - h_tolerance,
    hbar + h_tolerance,
    color="green",
    alpha=0.15,
    label="allowed band",
)
if settledat is not None:
    ax.axvline(
        t[settledat],
        color="green",
        linestyle=":",
        linewidth=2,
        label="settling time",
    )

ax.axvline(
    target_settling_time,
    color="red",
    linestyle=":",
    linewidth=2,
    label="settling deadline",
)
ax.set_ylabel("Height (m)")
ax.set_xlim(0,T)
ax.grid()
ax.legend(fontsize=12)

ax = axs[1]
ax.plot(t, tau_c)
ax.set_xlabel("time [s]",fontsize=12)
ax.set_ylabel("Thrust",fontsize=12)
ax.set_xlim(0,T)
ax.grid()

fig.savefig("drone_response.png", dpi=150)
plt.show()
