import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.pylab import *
from itertools import count
import random
import time

plt.style.use('fivethirtyeight')
index = count()
x_vals = [0]
y_vals_1 = [0]
y_vals_2 = [0]
y_vals_3 = [0]
y_vals_4 = [0]
def animate(i):
    x_vals.append(next(index))
    y_vals_1.append(random.randint(0,5))
    y_vals_2.append(random.randint(0,5))
    y_vals_3.append(random.randint(0,5))
    y_vals_4.append(random.randint(0,5))
    
    plt.cla()
    plt.plot(x_vals, y_vals_1, label='Chennel 1')
    plt.plot(x_vals, y_vals_2, label='Chennel 2')
    plt.plot(x_vals, y_vals_3, label='Chennel 3')
    plt.plot(x_vals, y_vals_4, label='Chennel 4')
    plt.legend(loc='upper left')
    plt.tight_layout()


ani = animation.FuncAnimation(plt.gcf(), animate, interval=100)
plt.tight_layout()
plt.show()