import RPi.GPIO as GPIO
from time import sleep
from enum import Enum
import time
from threading import Thread


class OpticalSensor():
    def __init__(self, sensor_pin):
        if isinstance(sensor_pin, int):
            self.__sensor_pin = sensor_pin
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(self.__sensor_pin,GPIO.IN,GPIO.PUD_UP)
            self.__timetaken = 0
            self.__pevtime   = 0
            self.__counter = 0
            self.__rpm = 0
            self.__previous_millis = 0
            GPIO.add_event_detect(self.__sensor_pin,GPIO.RISING, self.__func_interrupt__)

            #self.__th = Thread(target = self.__func_thread__)
            #self.__th.start()          
        else:
            print("Error: sensor_pin should be int")
            
    def __func_interrupt__(self, key):
        self.__counter = self.__counter + 1
        
        if(self.__counter >= 20):
            self.__timetaken = (time.clock()*1000) - self.__pevtime
            self.__rpm = (1000/self.__timetaken)*60
            self.__pevtime = (time.clock()*1000)
            self.__counter = 0
            print(self.__rpm)
            
            
            
            
        
    def __func_thread__(self):
        while True:
            #print(f"Thread ",self.__sensor_pin, ":",(time.clock()))
            if((time.clock()*1000 - self.__previous_millis) >= 1000):
                self.__rpm = (self.__counter / 20);
                print(self.__counter)
                self.__counter = 0
                self.__previous_millis+= 1000
                
                
    def get_rpm(self):
        return self.__rpm;
            

        
        
               
    