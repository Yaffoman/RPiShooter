import RPi.GPIO as GPIO
import time
from time import sleep
GPIO.setmode(GPIO.BCM)

A1 = 16 #red
A2 = 12 # blue
B1 = 20 # black
B2 = 21

A1 = 20
A2 = 21
B1 = 16
B2 = 12

A1 = 19
A2 = 26
B1 = 13
B2 = 6
delay = .05
GPIO.setup(A1, GPIO.OUT)
GPIO.setup(A2, GPIO.OUT)
GPIO.setup(B1, GPIO.OUT)
GPIO.setup(B2, GPIO.OUT)

#GPIO.setup(17,GPIO.OUT) #in 3    bl    red
#GPIO.setup(27,GPIO.OUT) #in 4    tl    blue

#GPIO.setup(22,GPIO.OUT) #in 1    tr    green
#GPIO.setup(18,GPIO.OUT) #in 2    br    black

for i in range (0,8):
    GPIO.output(A1,0)
    GPIO.output(A2,1)
    GPIO.output(B1,0)
    GPIO.output(B2,1)
    sleep(delay)
    ''' 
    GPIO.output(A1,0)
    GPIO.output(A2,1)
    GPIO.output(B1,0)
    GPIO.output(B2,0)
    sleep(delay)
    '''
    GPIO.output(A1,0)
    GPIO.output(A2,1)
    GPIO.output(B1,1)
    GPIO.output(B2,0)
    sleep(delay)
    '''
    GPIO.output(A1,0)
    GPIO.output(A2,0)
    GPIO.output(B1,1)
    GPIO.output(B2,0)
    sleep(delay)
    '''
    GPIO.output(A1,1)
    GPIO.output(A2,0)
    GPIO.output(B1,1)
    GPIO.output(B2,0)
    sleep(delay)
    '''
    GPIO.output(A1,1)
    GPIO.output(A2,0)
    GPIO.output(B1,0)
    GPIO.output(B2,0)
    sleep(delay)
    '''
    GPIO.output(A1,1)
    GPIO.output(A2,0)
    GPIO.output(B1,0)
    GPIO.output(B2,1)
    sleep(delay)
    '''
    GPIO.output(A1,0)
    GPIO.output(A2,0)
    GPIO.output(B1,0)
    GPIO.output(B2,1)
    sleep(delay)
    '''
    print(i)
sleep(3) 
GPIO.output(A1,0)
GPIO.output(A2,0)
GPIO.output(B1,0)
GPIO.output(B2,0)
