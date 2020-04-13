import numpy as np
#idk how to do the actual moter control

def up():
    return

def down():
    return

def left():
    return

def right():
    return

def to_polar(coords, img_shape=(100,100)):
    """
    converts catrisan to polar cootdinats
    assumes coords is a tuple (r,c)
    """
    y,x = coords 
    mid_y, mid_x = .5*img_shape[0], .5*img_shape[1]
    r = np.sqrt((x - mid_x)**2 + (y - mid_y)**2)
    t = np.arctan2([y - mid_y],[x - mid_x]) * (180/np.pi)
    return r, t[0]

def move(coords, img_shape, move_mult=5):
    max_r = np.sqrt((img_shape[0]/2)**2 + (img_shape[1]/2)**2)
    r, t = to_polar(coords, img_shape)
    reps = int(r/max_r) * move_mult
    for _ in range(reps):
        if t > -15 and t <= 15:
            right()
        if t > 15 and t <= 75:
            right()
            up()
        if t > 75 and t < = 105:
            up()
        if t > 105 and t <= 165:
            left()
            up()
        if t > 165 or t <= -165:
            left()
        if t > -165 and t <= -105:
            left()
            down()
        if t > -105 and t <=  -75:
            down()
        if t > -75 and t < -15:
            right()
            down()
    return r/r_max