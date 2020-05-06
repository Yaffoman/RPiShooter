from Motor import *
from NewMotor import *
from IOpins import *
import time
import keyboard

m1 = Motor(M2A1, M2A2, M2B1, M2B2)
m2 = NewMotor(enable=en2, direction=dirpin2, pulse=pul2)
m1.off()
m2.off()
m1.inc()
for i in range(0, 130):
    m2.dec()
    print("HERE")
    time.sleep(.001)
for i in range(0, 10):
#    m2.inc()
    #m1.dec()
    time.sleep(.5)
m1.off()
m2.off()
'''
while True:
    if keyboard.is_pressed('w'):
        m1.inc()
    if keyboard.is_pressed('a'):
        m2.inc()
    if keyboard.is_pressed('s'):
        m1.dec()
    if keyboard.is_pressed('d'):
        m2.dec()
    if keyboard.is_pressed('q'):
        break
    time.sleep(.01)
m1.off()
m2.off()
'''
