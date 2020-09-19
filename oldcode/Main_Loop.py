#initialize everything
from oldcode.myDetection import *
from oldcode.Launcher import *
from oldcode.motor_control import *
from oldcode.tfmini import *
import cv2

myLaunch = Launcher(WaterPin, AirPin, 1, .4)
threshold = 10
"""
1. initialize camera and lidar
2. initialize tensorflow files
3. execute main loop (ending on keypress/pin connected to button)
"""

sleep(15)
while True:
    if cv2.waitKey(1) == ord('q'):
        break
    (x, y) = detect()           # midpt of detection box
    while abs(x - 320) > threshold or abs(y-240) > threshold:
        

        if x > (320 + threshold):
            right()
        elif x < (320 - threshold):
            left()

        if y > (200 + threshold):
            up()
        elif y < (200 - threshold):
            down()
        (x, y) = detect()
        print(x,y)
        sleep(.3)

    # move((x, y), (640, 400))    # moves barrel so that camera is centered on box
    dist = getTFminiData()      # get distance to target
    # TODO move to firing position
    myLaunch.fire()

