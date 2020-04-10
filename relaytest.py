import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

GPIO.setup(21,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)

for i in range(0,10):
     GPIO.output(21,1)
     print("here")
     time.sleep(.01)
     GPIO.output(21,0)
     time.sleep(.01)