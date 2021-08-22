import numpy as np
from motor import Motor
from tkinter import *
import tkinter.font
######################################################################################
# L298N Module 1
# front motor right En1 = Gpio 22, In1 =  Gpio 27, In2 = Gpio 17 Speed sensor = 5 +
# back  motor right En2 = Gpio 2,  In1 =  Gpio 3,  In2 = Gpio 4  Speed sensor = 10 +
######################################################################################

######################################################################################
# L298N Module 2
# front motor left En1 = Gpio 14, In1 =  Gpio 15, In2 = Gpio 18 Speed sensor = 11
# back  motor left En2 = Gpio 25, In1 =  Gpio 24, In2 = Gpio 23 Speed sensor = 9
######################################################################################
front_right = Motor(22, 27, 17)
back_right  = Motor(2, 3, 4)

front_left  = Motor(25, 24, 23)
back_left   = Motor(14, 15, 18)
win = Tk()
win.title("Motor control")
myFont = tkinter.font.Font(family = "Hevvetica", size = 12, weight = "bold")
#
code = Entry(win, font = myFont, width = 10)
code.grid(row = 2, column = 1)

def motorEnable():
    setSpeed = int(code.get())
    front_right.moveF(setSpeed)

def motorDisable():
    front_right.stop()

def close_win():
    front_right.stop()
    win.destroy()

def main():
    print("main function")


    EnableMotorBtn = Button(win, text = "Motor On", font = myFont, command = motorEnable, bg = 'bisque2', height = 1, width = 24)
    EnableMotorBtn.grid(row = 0, column = 1)

    DisableMotorBtn = Button(win, text = "Motor Off", font = myFont, command = motorDisable, bg = 'bisque2', height = 1, width = 24)
    DisableMotorBtn.grid(row = 1, column = 1)



    win.protocol("WM_DELETE_WINDOW", close_win)
    win.mainloop()



if __name__ == "__main__":
    main()