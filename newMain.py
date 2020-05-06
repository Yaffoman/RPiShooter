#initialize everything
from IOpins import *
import newDetection
from Launcher import *
from motor_control import *
from tfmini import *
import cv2

myLaunch = Launcher(WaterPin, AirPin, 1, .4)
threshold = 10
"""
1. initialize camera and lidar
2. initialize tensorflow files
3. execute main loop (ending on keypress/pin connected to button)
"""

while True:
    if cv2.waitKey(1) == ord('q'):
        break
    print("Searching...")
    newDetection.detect()
    if newDetection.detected:
        x,y = newDetection.xtarg,newDetection.ytarg
        print("Target seen at",x,y)
        while newDetection.detected and (abs(x - 320) > threshold or abs(y-240) > threshold):

            if x > (320 + threshold):
                print("Moving right")
                right()
            elif x < (320 - threshold):
                print("Moving left")
                left()

            if y > (200 + threshold):
                print("Moving up")
                up()
            elif y < (200 - threshold):
                print("Moving down")
                down()
            newDetection.detected = False
            sleep(.3)
            print("Calibrating...")
            newDetection.detect()
            x,y = newDetection.xtarg,newDetection.ytarg
            print("New position at",x,y)
        print("Target centered")
        dist = getTFminiData()      # get distance to target
        print("Distance", dist)
        # TODO move to firing position
        print("FIRING!!!!")
        myLaunch.fire()
        print("TARGET NEUTRALIZED")
    else:
        print("none found")

