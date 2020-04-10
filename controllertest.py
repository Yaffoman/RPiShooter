import RPi.GPIO as GPIO
import time
from time import sleep
GPIO.setmode(GPIO.BCM)

A1 = 18
A2 = 22
B1 = 17
B2 = 27
delay = .05
GPIO.setup(A1, GPIO.OUT)
GPIO.setup(A2, GPIO.OUT)
GPIO.setup(B1, GPIO.OUT)
GPIO.setup(B2, GPIO.OUT)

#GPIO.setup(17,GPIO.OUT) #in 3    bl    red
#GPIO.setup(27,GPIO.OUT) #in 4    tl    blue

#GPIO.setup(22,GPIO.OUT) #in 1    tr    green
#GPIO.setup(18,GPIO.OUT) #in 2    br    black

for i in range (0,512):
    GPIO.output(A1,0)
    GPIO.output(A2,1)
    GPIO.output(B1,0)
    GPIO.output(B2,1)
    sleep(delay)
    
    GPIO.output(A1,0)
    GPIO.output(A2,1)
    GPIO.output(B1,0)
    GPIO.output(B2,0)
    sleep(delay)
    
    GPIO.output(A1,0)
    GPIO.output(A2,1)
    GPIO.output(B1,1)
    GPIO.output(B2,0)
    sleep(delay)
    
    GPIO.output(A1,0)
    GPIO.output(A2,0)
    GPIO.output(B1,1)
    GPIO.output(B2,0)
    sleep(delay)
    
    GPIO.output(A1,1)
    GPIO.output(A2,0)
    GPIO.output(B1,1)
    GPIO.output(B2,0)
    sleep(delay)
    
    GPIO.output(A1,1)
    GPIO.output(A2,0)
    GPIO.output(B1,0)
    GPIO.output(B2,0)
    sleep(delay)
    
    GPIO.output(A1,1)
    GPIO.output(A2,0)
    GPIO.output(B1,0)
    GPIO.output(B2,1)
    sleep(delay)
    
    GPIO.output(A1,0)
    GPIO.output(A2,0)
    GPIO.output(B1,0)
    GPIO.output(B2,1)
    sleep(delay)
    
    print(i)
 
GPIO.output(A1,0)
GPIO.output(A2,0)
GPIO.output(B1,0)
GPIO.output(B2,0)
