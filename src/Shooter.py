from src.Pins import *
from src.Motor import Motor
from src.Launcher import Launcher
from src.tfmini import *
from math import tan, asin
import RPi.GPIO as GPIO


class Shooter:

    def __init__(self):
        self.base = Motor(BASE_EN, BASE_DIR, BASE_PUL, 10)
        self.arm = Motor(ARM_EN, ARM_DIR, ARM_PUL, 10)
        self.launcher = Launcher(V_WATER, V_AIR)
        GPIO.cleanup()
    # MOTOR CONTROLS

    def off(self):
        self.arm.off()
        self.base.off()

    def up(self):
        self.arm.inc()
        return

    def down(self):
        self.arm.dec()
        return

    def left(self):
        self.base.inc()
        return

    def right(self):
        self.base.dec()
        return

    def move(self, x, y):
        while x > 0:
            x -= 1
            self.right()
        while x < 0:
            x += 1
            self.left()
        while y > 0:
            y -= 1
            self.down()
        while y < 0:
            y += 1
            self.up()

    # LAUNCHER CONTROLS

    def fire(self):
        self.launcher.fire()

    def aim(self, dist, phi):
        y = dist * tan(phi)
        g = -9.81
        angle = asin(2 * (y - dist * g) / 100)
        return angle

    def ready(self):
        return getTFminiData()
