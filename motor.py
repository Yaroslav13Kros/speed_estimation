import RPi.GPIO as GPIO
from time import sleep
from enum import Enum

class Motor():
    def __init__(self, ena, in1, in2):
        if isinstance(ena, int) and isinstance(in1, int) and isinstance(in2, int):
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            self.__Ena = ena
            self.__In1 = in1
            self.__In2 = in2
            GPIO.setup(self.__Ena, GPIO.OUT)
            GPIO.setup(self.__In1, GPIO.OUT)
            GPIO.setup(self.__In2, GPIO.OUT)
            self.__pwm = GPIO.PWM(self.__Ena, 100)
            self.__pwm.start(0)
        else:
            print("Error: ena, in1, int2 should be int")

    def moveF(self, speed = 50):
        GPIO.output(self.__In1, GPIO.LOW)
        GPIO.output(self.__In2, GPIO.HIGH)
        self.__pwm.ChangeDutyCycle(speed)

    def moveB(self, speed = 50):
        GPIO.output(self.__In1, GPIO.HIGH)
        GPIO.output(self.__In2, GPIO.LOW)
        self.__pwm.ChangeDutyCycle(speed)

    def stop(self):
        self.__pwm.ChangeDutyCycle(0)
