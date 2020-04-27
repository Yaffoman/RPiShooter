#initialize everything
from IOpins import *
from myDetection import *
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
    x, y = detect()           # midpt of detection box
    while abs(x - 320) > threshold or abs(y-200) > threshold:
        delay(.3)
        if x > 320 + threshold:
            left()
        elif x < 320 - threshold:
            right()

        if y > 200 + threshold:
            down()
        elif y < 200 - threshold:
            up()
        x, y = detect()

    # move((x, y), (640, 400))    # moves barrel so that camera is centered on box
    dist = getTFminiData()      # get distance to target
    # TODO move to firing position
    myLaunch.fire()

