import RPi.GPIO as GPIO
from time import sleep

delay = .05


class NewMotor:

    GPIO.setmode(GPIO.BCM)

    def __init__(self, enable, direction, pulse):
        self.enable = enable
        self.direction = direction
        self.pulse = pulse
        GPIO.setmode(self.enable, GPIO.OUT)
        GPIO.setmode(self.direction, GPIO.OUT)
        GPIO.setmode(self.pulse, GPIO.OUT)
        GPIO.output(self.enable, 1)
        GPIO.output(self.direction, 0)
        GPIO.output(self.pulse, 0)

    def inc(self):
        GPIO.output(self.direction, 1)
        GPIO.output(self.pulse, 1)
        sleep(.05)
        GPIO.output(self.pulse, 0)

    def dec(self):
        GPIO.output(self.direction, 0)
        GPIO.output(self.pulse, 1)
        sleep(.05)
        GPIO.output(self.pulse, 0)

    def off(self):
        GPIO.output(self.enable, 0)