#Code skeleton
"""
1. initialize camera and lidar
2. initialize tensorflow files
3. execute main loop (ending on keypress/pin connected to button)


Main loop:
    (x,y) = xy coords of middle of detection box
    angle = calcAngle(x,y)
    move gun to that angle (w lidar on barrel)
    dist = read lidar
    angle = calcTraj(x,y,dist)
    move gun to angle
    fire projectile
        open water valve (.5s)
        close water valve
        open air valv(1s)
        close water valve
"""

