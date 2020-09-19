#initialize everything
from src import lightDetection as detection
import cv2
from src.Shooter import Shooter

threshold = 10
height = 600
width = 640
shooter = Shooter()
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
        y, x = detection.detect()
        print("Target seen at: (X:" + x + ", Y:",y + ")")

        ydiff, xdiff = y - height/2, x-width/2
        print("Aiming...")

        if abs(ydiff) > threshold or abs(xdiff) > threshold:
            print("Moving down and right:", ydiff/2, xdiff/2)
            shooter.move(xdiff/2, ydiff/2)
        else:
            print("Found Target, eliminating...")
            distance = shooter.ready()
            print("Distance:", distance)

            shooter.move(0, 10)
            angle = shooter.aim()
            print(angle)
            shooter.fire()

finally:
    shooter.off()
    print("Shutting down...")
