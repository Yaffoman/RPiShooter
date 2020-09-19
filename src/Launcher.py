import RPi.GPIO as GPIO
from time import sleep

delay = .2


class Launcher:
    GPIO.setmode(GPIO.BCM)

    def __init__(self, waterpin, airpin, water_del=1, air_del=.2):
        self.water = waterpin
        self.air = airpin
        self.water_delay = water_del
        self.air_delay = air_del
        GPIO.setup(self.water, GPIO.OUT)
        GPIO.setup(self.air, GPIO.OUT)
        GPIO.output(self.air, 1)
        GPIO.output(self.water, 1)

    def fire(self):
        GPIO.output(self.air, 1)
        GPIO.output(self.water, 1)
        sleep(delay)                # allow to settle
        GPIO.output(self.water, 0)  # open water
        sleep(self.water_delay)
        GPIO.output(self.water, 1)
        sleep(delay)                # allow to settle
        GPIO.output(self.air, 0)    # open air
        sleep(self.air_delay)
        GPIO.output(self.air, 1)
