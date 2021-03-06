import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)

water = 23

air = 24
water_delay = 1 
air_delay = .3
delay = .2
GPIO.setup(water,GPIO.OUT)
GPIO.setup(air,GPIO.OUT)
GPIO.output(air,1)
GPIO.output(water,1)

#turn both off
def fire():
    GPIO.output(air,1)
    GPIO.output(water,1)
    sleep(1)
    GPIO.output(water,0) #open water
    sleep(water_delay)
    GPIO.output(water,1)
    sleep(delay)
    GPIO.output(air,0)
    sleep(air_delay)
    GPIO.output(air,1)


