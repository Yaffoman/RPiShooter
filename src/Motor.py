import RPi.GPIO as GPIO
from time import sleep


class Motor:

    GPIO.setmode(GPIO.BOARD)

    def __init__(self, enable, direction, pulse, speed):
        self.enable = enable
        self.direction = direction
        self.pulse = pulse
        self.delay = 1/speed

        GPIO.setup(self.enable, GPIO.OUT)
        GPIO.setup(self.direction, GPIO.OUT)
        GPIO.setup(self.pulse, GPIO.OUT)
        GPIO.output(self.enable, 0)
        GPIO.output(self.direction, 0)
        GPIO.output(self.pulse, 1)

    def inc(self):
        GPIO.output(self.enable, 0)
        GPIO.output(self.direction, 1)
        GPIO.output(self.pulse, 0)
        sleep(self.delay)
        GPIO.output(self.pulse, 1)

    def dec(self):
        GPIO.output(self.enable, 0)
        GPIO.output(self.direction, 0)
        GPIO.output(self.pulse, 0)
        sleep(self.delay)
        GPIO.output(self.pulse, 1)

    def off(self):
        GPIO.output(self.enable, 1)
