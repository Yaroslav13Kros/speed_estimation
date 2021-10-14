import RPi.GPIO as GPIO
from time import sleep
from enum import Enum

class SpeedSensor():
    def __init__(self, intr):
        self.__intr = intr
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.__intr,GPIO.IN,GPIO.PUD_UP)
        GPIO.add_event_detect(self.__intr,GPIO.FALLING,MyInterrupt,200)

