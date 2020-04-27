from Motor import *
from IOpins import *
import time

m1 = Motor(M1A1, M1A2, M1B1, M1B2)
m2 = Motor(M2A1, M2A2, M2B1, M2B2)
m1.off()
m2.off()
for i in range(0, 10):
    m1.inc()
    m2.dec()
    time.sleep(.05)
for i in range(0, 10):
    m2.inc()
    m1.dec()
    time.sleep(.05)


