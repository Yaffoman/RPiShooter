import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

A1 = 12
A2 = 16
B1 = 20
B2 = 21
delay = .05
GPIO.setup(A1, GPIO.OUT)
GPIO.setup(A2, GPIO.OUT)
GPIO.setup(B1, GPIO.OUT)
GPIO.setup(B2, GPIO.OUT)

GPIO.setup(6, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

GPIO.output(6,0)
GPIO.output(13,0)
GPIO.output(19,0)
GPIO.output(26,0)


GPIO.output(A1,0)
GPIO.output(A2,0)
GPIO.output(B1,0)
GPIO.output(B2,0)
