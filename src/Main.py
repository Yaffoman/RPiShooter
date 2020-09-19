#initialize everything
import contextlib
from src import lightDetection as detection
from src.Shooter import Shooter
import sys
import termios


@contextlib.contextmanager
def raw_mode(file):
    """
    Magic function that allows key presses.
    :param file:
    :return:
    """
    old_attrs = termios.tcgetattr(file.fileno())
    new_attrs = old_attrs[:]
    new_attrs[3] = new_attrs[3] & ~(termios.ECHO | termios.ICANON)
    try:
        termios.tcsetattr(file.fileno(), termios.TCSADRAIN, new_attrs)
        yield
    finally:
        termios.tcsetattr(file.fileno(), termios.TCSADRAIN, old_attrs)


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
    with raw_mode(sys.stdin):
        ch = sys.stdin.read(1)

        if ch == "i":
            print("Interactive mode enabled")
            print("Move using wasd, k to fire, l to read LiDAR, q to end, h to show these commands again")
            while True:
                ch = sys.stdin.read(1)
                if ch == "w":
                    shooter.up()
                if ch == "a":
                    shooter.left()
                if ch == "s":
                    shooter.down()
                if ch == "d":
                    shooter.right()
                if ch == "k":
                    shooter.fire()
                if ch == "l":
                    print("Distance: ", shooter.ready())
                if ch == "h":
                    print("Move using wasd, k to fire, l to read LiDAR, q to end, h to show these commands again")

        elif ch == "a":
            while True:
                ch = sys.stdin.read(1)
                if not ch or ch == "q":
                    break
                print("Searching...")
                y, x = detection.detect()
                print("Target seen at: (X:" + x + ", Y:", y + ")")

                ydiff, xdiff = y - height/2, x-width/2
                print("Aiming...")

                if abs(ydiff) > threshold or abs(xdiff) > threshold:
                    print("Moving down and right:", ydiff/2, xdiff/2)
                    shooter.move(xdiff/2, ydiff/2)
                else:
                    print("Found Target, eliminating...")
                    distance = shooter.ready()
                    print("Distance:", distance)
                    angle = shooter.aim()
                    print("Angle:", angle)
                    shooter.fire()
                    print("Firing!")

finally:
    print("Shutting down...")
    shooter.off()
