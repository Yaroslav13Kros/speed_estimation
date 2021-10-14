import RPi.GPIO as GPIO
import time
import threading

KEY = 10

class SpeedSensor:
    def __init__(self, input_sensor_pin):
        self.__input_sensor_pin = input_sensor_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.____input_sensor_pin,GPIO.IN,GPIO.PUD_UP)
        GPIO.add_event_detect(KEY,GPIO.FALLING,self.__interrupt,200)
        
    def __interrupt(input_sensor_pin):
        print("__interrupt")
