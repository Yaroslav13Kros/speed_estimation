import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.pylab import *
import random
import time

fig = figure(num = 0, figsize = (20,20))
fig.suptitle("Wheel speeds", fontsize=12)

ax_1 = fig.add_subplot(2, 2, 1)
ax_2 = fig.add_subplot(2, 2, 2)
ax_3 = fig.add_subplot(2, 2, 3)
ax_4 = fig.add_subplot(2, 2, 4)
yWheel_speed_1 = []
yWheel_speed_2 = []
yWheel_speed_3 = []
yWheel_speed_4 = []
xWheel_time    = []

ax_1.set_title("Wheel speed #1")
ax_2.set_title("Wheel speed #2")
ax_3.set_title("Wheel speed #3")
ax_4.set_title("Wheel speed #4")

ax_1.grid(True)
ax_2.grid(True)
ax_3.grid(True)
ax_4.grid(True)

ax_1.set_xlabel("time")
ax_1.set_ylabel("RPM")
ax_2.set_xlabel("time")
ax_2.set_ylabel("RPM")
ax_3.set_xlabel("time")
ax_3.set_ylabel("RPM")
ax_4.set_xlabel("time")
ax_4.set_ylabel("RPM")


# This function is called periodically from FuncAnimation
def animate(i, yWheel_speed_1, yWheel_speed_2, yWheel_speed_3, yWheel_speed_4, xWheel_time):

    # Read temperature (Celsius) from TMP102
    rpm = random.randint(0, 20)
    # Add x and y to lists
    xWheel_time.append(time.process_time())
    yWheel_speed_1.append(random.randint(0, 20))
    yWheel_speed_2.append(random.randint(0, 20))
    yWheel_speed_3.append(random.randint(0, 20))
    yWheel_speed_4.append(random.randint(0, 20))

    # Limit x and y lists to 20 items
    yWheel_speed_1 = yWheel_speed_1[-200:]
    yWheel_speed_2 = yWheel_speed_2[-200:]
    yWheel_speed_3 = yWheel_speed_3[-200:]
    yWheel_speed_4 = yWheel_speed_4[-200:]
    xWheel_time = xWheel_time[-200:]
    

    # Draw x and y lists
    ax_1.clear()
    ax_2.clear()
    ax_3.clear()
    ax_4.clear()
    ax_1.plot(xWheel_time, yWheel_speed_1)
    ax_2.plot(xWheel_time, yWheel_speed_2)
    ax_3.plot(xWheel_time, yWheel_speed_3)
    ax_4.plot(xWheel_time, yWheel_speed_4)
    ax_1.grid(True)
    ax_2.grid(True)
    ax_3.grid(True)
    ax_4.grid(True)

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)

ani = animation.FuncAnimation(fig, animate, fargs=(yWheel_speed_1, yWheel_speed_2, yWheel_speed_3, yWheel_speed_4, xWheel_time), interval=100)
plt.show()