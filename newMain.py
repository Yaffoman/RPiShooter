#initialize everything
from IOpins import *
import lightDetection as detection
from Launcher import *
from motor_control import *
from tfmini import *
import cv2

myLaunch = Launcher(WaterPin, AirPin, 1, .4)
threshold = 40
height = 720
width = 1280
"""
1. initialize camera and lidar
2. initialize tensorflow files
3. execute main loop (ending on keypress/pin connected to button)
"""
try:
    while True:
        if cv2.waitKey(1) == ord('q'):
            break
        print("Searching...")
        detection.detect()
        if detection.detected:
            x,y = detection.xtarg,detection.ytarg
            print("Target seen at",x,y)
            while detection.detected and abs(y-height/2) > threshold:
               
                if x > (width/2 + threshold):
                    print("Moving right")
                    right()
                elif x < (width/2 - threshold):
                    print("Moving left")
                    left()
                
                if y > (height/2 + threshold):
                    down()
                    print("Moving down")
                elif y < (height/2 - threshold):
                    up()
                    print("Moving up")

                detection.detected = False
                sleep(.1)
                print("Calibrating...")
                detection.detect()
                x,y = detection.xtarg,detection.ytarg
                print("New position at",x,y)
            print("Target centered")
            dist = getTFminiData()      # get distance to target
            print("Distance", dist)
            # TODO move to firing position
            print("FIRING!!!!")
            up()
            up()
            up()
            up()
            up()
            up()
            up()
            up()
            up()
            up()
            up()
            up()
            up()
            myLaunch.fire()
            print("TARGET NEUTRALIZED")
        else:
            print("none found")
except:
    motorsoff()
    raise
