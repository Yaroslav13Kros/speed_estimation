import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import time

from motor import Motor
from optical_sensor import OpticalSensor

motor_front_left  = Motor(25, 24, 23)
opt_sensor_front_left = OpticalSensor(11)


# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []


set_rpm = 160

# This function is called periodically from FuncAnimation
def animate(i, xs, ys):

    # Read temperature (Celsius) from TMP102
    rpm = opt_sensor_front_left.get_rpm()
    rpm_reg = 0 + (set_rpm - set_rpm)*0.5
    # Add x and y to lists
    xs.append(time.process_time())
    ys.append(rpm)

    # Limit x and y lists to 20 items
    xs = xs[-200:]
    ys = ys[-200:]

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('TMP102 Temperature over Time')
    plt.ylabel('RPM')
    


# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=100)
motor_front_left.moveF(20)
plt.show()