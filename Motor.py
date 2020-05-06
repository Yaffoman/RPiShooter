import RPi.GPIO as GPIO

pattern = [(0, 1, 0, 1), (0, 1, 0, 0), (0, 1, 1, 0), (0, 0, 1, 0), (1, 0, 1, 0), (1, 0, 0, 0), (1, 0, 0, 1),
           (0, 0, 0, 1)]  # halfstep pattern
patternfull = [(0, 1, 0, 1), (0, 1, 1, 0), (1, 0, 1, 0), (1, 0, 0, 1)]
delay = .05


class Motor:

    import time
    from time import sleep
    GPIO.setmode(GPIO.BCM)

    def __init__(self, pin1, pin2, pin3, pin4):
        self.A1 = pin1
        self.A2 = pin2
        self.B1 = pin3
        self.B2 = pin4
        GPIO.setup(self.A1, GPIO.OUT)
        GPIO.setup(self.A2, GPIO.OUT)
        GPIO.setup(self.B1, GPIO.OUT)
        GPIO.setup(self.B2, GPIO.OUT)
        self.state = 0
        self.move(pattern[self.state])

    def inc(self):
        self.state = (self.state + 1) % len(pattern)
        self.move(pattern[self.state])

    def dec(self):
        self.state = (self.state - 1) % len(pattern)
        self.move(pattern[self.state])

    def off(self):
        self.move((0, 0, 0, 0))

    def move(self, inpt):
        GPIO.output(self.A1, inpt[0])
        GPIO.output(self.A2, inpt[1])
        GPIO.output(self.B1, inpt[2])
        GPIO.output(self.B2, inpt[3])
