#file: python s2310710045.py --mass=1000,--velocity=55, --friction=0.65

# import necessary libraries
import math
import argparse # given
import matplotlib.pyplot as plt # given
import numpy as np  # corrected the numpy import
from scipy.constants import g # acceleration due to gravity
# setup arg parser
arg_parser = argparse.ArgumentParser(description='Simulate braking distance.')
arg_parser.add_argument("mass", type=float, nargs='?', default=1000, help="Mass of the vehicle (kg)")
arg_parser.add_argument("velocity", type=float, nargs='?', default=24.58, help="Initial velocity of the vehicle (m/s)") # transform mph into m/s (55 mph = 24,58 m/s)
arg_parser.add_argument("friction", type=float, nargs='?', default=0.65, help="Friction coefficient of the road")
cmd_call_args = arg_parser.parse_args()
# define variables
mass = cmd_call_args.mass
velocity = cmd_call_args.velocity
friction = cmd_call_args.friction
# calculation of time to zero velocity
g = 9.81  # gravitational acceleration in m/s^2
braketime = velocity / friction / g
brakedistance = velocity * braketime - friction * g * pow(braketime, 2) / 2
print(f'The braking distance is {brakedistance:.2f} m')
print(f'The braking time is {braketime} s')
# simulation parameters
simulation_time = braketime  # as required
time_step = braketime / 30  # as required
# simulation function
taxis = np.arange(0, simulation_time, time_step)
vaxis = velocity - friction * g * taxis
saxis = velocity * taxis - friction * g * pow(taxis, 2) / 2
# create plots
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
# plot (velocity over time)
axs[0].plot(taxis, vaxis)
axs[0].set_title('velocity over time')
axs[0].set_xlabel('time (s)')
axs[0].set_ylabel('velocity (m/s)')
axs[0].grid(True, which='both') # activation grid in both axis
# plot (distance over time)
axs[1].plot(taxis, saxis)  # corrected the plot data
axs[1].set_title('distance over time')
axs[1].set_xlabel('time (s)')
axs[1].set_ylabel('distance (m)')
axs[1].grid(True, which='both')  # activation grid in both axis
# add text
text_content = f'Initial Velocity: {velocity} m/s\nMass: {mass} kg\nFriction Coefficient: {friction}\nStop Time: {braketime:.2f} s\nBraking Distance: {brakedistance:.2f} m'  #
fig.text(0.8, 0.3, text_content, bbox=dict(facecolor='lightgreen', alpha=1), fontsize=9, verticalalignment='center')
# display plots
plt.tight_layout()
plt.show()