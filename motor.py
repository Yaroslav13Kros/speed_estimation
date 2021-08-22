import RPi.GPIO as GPIO
from time import sleep
from enum import Enum


class DirectionType(Enum):
    NO_DIRECTION = 0
    FORWARD = 1
    REVERSE = 2


class Motor:
    def __init__(self, ena, in1, in2):
        if isinstance(ena, int) and isinstance(in1, int) and isinstance(in2, int):
            self.__Ena = ena
            self.__In1 = in1
            self.__In2 = in2
            GPIO.setup(self.__Ena, GPIO.OUT)
            GPIO.setup(self.__In1, GPIO.OUT)
            GPIO.setup(self.__In2, GPIO.OUT)
            self.__pwm = GPIO.PWM(self.__Ena, 100)
            self.pwm.start(0)
        else:
            print("Error: ena, in1, int2 should be int")