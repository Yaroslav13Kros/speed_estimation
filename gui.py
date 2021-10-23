import numpy as np
from tkinter import *
import tkinter.font
from motor import Motor
from optical_sensor import OpticalSensor
import matplotlib.pyplot as plt
import datetime as dt
import matplotlib.animation as animation
import random
import time

opt_sensor_front_right_counter = 0
opt_sensor_back_right_counter = 0
opt_sensor_front_left_counter = 0
opt_sensor_back_left_counter = 0


def opt_sensor_front_right_cb(key):
    print("opt_sensor_front_right_cb")
    opt_sensor_front_right_counter+= 1

def opt_sensor_back_right_cb(key):
    print("opt_sensor_back_right_cb")
    opt_sensor_back_right_counter+= 1

def opt_sensor_front_left_cb(key):
    print("opt_sensor_front_left_cb")
    opt_sensor_front_left_counter+= 1

def opt_sensor_back_left_cb(key):
    print("opt_sensor_back_left_cb")
    opt_sensor_back_left_counter+= 1

motor_front_right = Motor(22, 27, 17)
opt_sensor_front_right = OpticalSensor(5)

motor_back_right  = Motor(2, 4, 3)
opt_sensor_back_right = OpticalSensor(10)

motor_front_left  = Motor(25, 24, 23)
opt_sensor_front_left = OpticalSensor(11)

motor_back_left   = Motor(14, 15, 18)
opt_sensor_back_left = OpticalSensor(9)

btn_width = 14
btn_height = 1
window = Tk()  
window.title("Car control")  
window.geometry('800x600')
myFont = tkinter.font.Font(family = "Hevvetica", size = 12, weight = "bold")

def close_win():
    window.destroy()
    
## EVENT FUNCTION ##

def frHendlMotor():
    if motor_front_right.get_status() == 1:
        motor_front_right.stop()
        MotorFrontRightBtn["text"] = "Motor fr On"
    else:
        motor_front_right.moveF()
        MotorFrontRightBtn["text"] = "Motor fr Off"
              
def flHendlMotor():
    if motor_front_left.get_status() == 1:
        motor_front_left.stop()
        MotorFrontLeftBtn["text"] = "Motor fl On"
    else:
        motor_front_left.moveF()
        MotorFrontLeftBtn["text"] = "Motor fl Off"

def brHendlMotor():
    if motor_back_right.get_status() == 1:
        motor_back_right.stop()
        MotorBackRightBtn["text"] = "Motor br On"
    else:
        motor_back_right.moveF()
        MotorBackRightBtn["text"] = "Motor br Off"
              
def blHendlMotor():
    if motor_back_left.get_status() == 1:
        motor_back_left.stop()
        MotorBackLeftBtn["text"] = "Motor bl On"
    else:
        motor_back_left.moveF()
        MotorBackLeftBtn["text"] = "Motor bl Off"
## Front Car ##
MotorFrontRightBtn = Button(window, text = "Motor fr On", font = myFont, command = frHendlMotor, bg = 'bisque2', height = btn_height, width = btn_width)
MotorFrontRightBtn.grid(row = 0, column = 0)

label_front = tkinter.Label(master=window, text="FRONT CAR", bg="red")
label_front.grid(row = 0, column = 1)

MotorFrontLeftBtn = Button(window, text = "Motor fl On", font = myFont, command = flHendlMotor, bg = 'bisque2', height = btn_height, width = btn_width)
MotorFrontLeftBtn.grid(row = 0, column = 2)

## Body Car ##
frame1 = tkinter.Frame(window, width=100, height=100, bg="red")
frame1.grid(row = 1, column = 1)

## Back Car ##
MotorBackRightBtn = Button(window, text = "Motor br On", font = myFont, command = brHendlMotor, bg = 'bisque2', height = btn_height, width = btn_width)
MotorBackRightBtn.grid(row = 2, column = 0)

label_front = tkinter.Label(master=window, text="BACK CAR", bg="red")
label_front.grid(row = 2, column = 1)

MotorBackLeftBtn = Button(window, text = "Motor bl On", font = myFont, command = blHendlMotor, bg = 'bisque2', height = btn_height, width = btn_width)
MotorBackLeftBtn.grid(row = 2, column = 2)

frame2 = tkinter.Frame(window, width=200, height=50, bg="red")
frame2.grid(row = 3, column = 1)

def HendlFront():
    motor_front_right.moveF()
    motor_back_right.moveF()
    motor_front_left.moveF()
    motor_back_left.moveF()
    
def HendlStop():
    motor_front_right.stop()
    motor_back_right.stop()
    motor_front_left.stop()
    motor_back_left.stop()

def HendlBack():
    motor_front_right.moveB()
    motor_back_right.moveB()
    motor_front_left.moveB()
    motor_back_left.moveB()

MotorFrontBtn = Button(window, text = "Front", font = myFont, command = HendlFront, bg = 'bisque2', height = btn_height, width = btn_width)
MotorFrontBtn.grid(row = 4, column = 1)

MotorStopBtn = Button(window, text = "Stop", font = myFont, command = HendlStop, bg = 'bisque2', height = btn_height, width = btn_width)
MotorStopBtn.grid(row = 5, column = 1)

MotorBackBtn = Button(window, text = "Back", font = myFont, command = HendlBack, bg = 'bisque2', height = btn_height, width = btn_width)
MotorBackBtn.grid(row = 6, column = 1)

#def set_speed(speed):
    
var_scale = IntVar()
def SetSpeed():
    motor_front_right.set_speed(var_scale.get())
    motor_back_right.set_speed(var_scale.get())
    motor_front_left.set_speed(var_scale.get())
    motor_back_left.set_speed(var_scale.get())
    print(var_scale.get())

s = tkinter.Scale(window, variable = var_scale, from_=0, to=100, orient=tkinter.HORIZONTAL, length=200, command=0)
s.grid(row = 7, column = 1)

SetSpeedBtn = Button(window, text = "Set speed", font = myFont, command = SetSpeed, bg = 'bisque2', height = btn_height, width = btn_width)
SetSpeedBtn.grid(row = 7, column = 2)

opt_sensor_front_right_var = StringVar()
opt_sensor_back_right_var = StringVar()
opt_sensor_front_left_var = StringVar()
opt_sensor_back_left_var = StringVar()

opt_sensor_front_right_lable = Label( window, textvariable=opt_sensor_front_right_var, relief=RAISED )
opt_sensor_back_right_lable  = Label( window, textvariable=opt_sensor_back_right_var,  relief=RAISED )
opt_sensor_front_left_lable  = Label( window, textvariable=opt_sensor_front_left_var,  relief=RAISED )
opt_sensor_back_left_lable   = Label( window, textvariable=opt_sensor_back_left_var,   relief=RAISED )

opt_sensor_front_right_var.set("MOTOR fr rpm:")
opt_sensor_back_right_var.set("MOTOR br rpm:")
opt_sensor_front_left_var.set("MOTOR fl rpm:")
opt_sensor_back_left_var.set("MOTOR bl rpm:")

opt_sensor_front_right_lable.grid(row = 4, column = 0)
opt_sensor_back_right_lable.grid(row = 5, column = 0)
opt_sensor_front_left_lable.grid(row = 6, column = 0)
opt_sensor_back_left_lable.grid(row = 7, column = 0)

def update_rpm():
  
    rpm_fr = opt_sensor_front_right.get_rpm()
    rpm_br = opt_sensor_back_right.get_rpm()
    rpm_fl = opt_sensor_front_left.get_rpm()
    rpm_bl = opt_sensor_back_left.get_rpm()
    
    opt_sensor_front_right_var.set(f"MOTOR fr rpm: {str(rpm_fr)}")
    opt_sensor_back_right_var.set(f"MOTOR br rpm:  {str(rpm_br)}")
    opt_sensor_front_left_var.set(f"MOTOR fl rpm:  {str(rpm_fl)}")
    opt_sensor_back_left_var.set(f"MOTOR bl rpm:   {str(rpm_bl)}")
    
    window.after(1000, update_rpm)
    
# Create figure for plotting
x_vals_t  = [0]
y_vals_fr = [0]
y_vals_br = [0]
y_vals_fl = [0]
y_vals_bl = [0]
plt.style.use('fivethirtyeight')
def animate(i):
    # Add x and y to lists
    x_vals_t.append(time.clock())
    y_vals_fr.append(opt_sensor_front_right.get_rpm())
    y_vals_br.append(opt_sensor_back_right.get_rpm())
    y_vals_fl.append(opt_sensor_front_left.get_rpm())
    y_vals_bl.append(opt_sensor_back_left.get_rpm())


    plt.cla()
    plt.plot(x_vals_t, y_vals_fr, label='Chennel fr')
    plt.plot(x_vals_t, y_vals_br, label='Chennel br')
    plt.plot(x_vals_t, y_vals_fl, label='Chennel fl')
    plt.plot(x_vals_t, y_vals_bl, label='Chennel bl')
    plt.legend(loc='upper left')
    plt.tight_layout()

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Wheel speed')
    plt.ylabel('RPM')

# Set up plot to call animate() function periodically

window.after(100, update_rpm)
ani = animation.FuncAnimation(plt.gcf(), animate, interval=10)
plt.show()
window.protocol("WM_DELETE_WINDOW", close_win)
window.mainloop()