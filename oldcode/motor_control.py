import numpy as np
# idk how to do the actual motor control
from oldcode.NewMotor import *
from oldcode.IOpins import *

motor2 = Motor(M2A1, M2A2, M2B1, M2B2)
motor1 = NewMotor(enable=en2, direction=dirpin2,pulse=pul2)

def motorsoff():
    motor2.off()
    motor1.off()
def up():
    motor1.inc()
    return


def down():
    motor1.dec()
    return


def left():
    motor2.inc()
    return


def right():
    motor2.dec()
    return


def to_polar(coords, img_shape=(100, 100)):
    """
    converts catrisan to polar cootdinats
    assumes coords is a tuple (r,c)
    """
    y, x = coords
    mid_y, mid_x = .5 * img_shape[0], .5 * img_shape[1]
    r = np.sqrt((x - mid_x) ** 2 + (y - mid_y) ** 2)
    t = np.arctan2([y - mid_y], [x - mid_x]) * (180 / np.pi)
    return r, t[0]


def move(coords, img_shape, move_mult=5):
    max_r = np.sqrt((img_shape[0] / 2) ** 2 + (img_shape[1] / 2) ** 2)
    r, t = to_polar(coords, img_shape)
    reps = int(r / max_r) * move_mult
    for _ in range(reps):
        if -15 < t <= 15:
            right()
        if 15 < t <= 75:
            right()
            up()
        if 75 < t <= 105:
            up()
        if 105 < t <= 165:
            left()
            up()
        if t > 165 or t <= -165:
            left()
        if -165 < t <= -105:
            left()
            down()
        if -105 < t <= -75:
            down()
        if -75 < t < -15:
            right()
            down()
    return r / max_r
