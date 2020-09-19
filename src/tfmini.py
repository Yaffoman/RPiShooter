# -*- coding: utf-8 -*
import serial

ser = serial.Serial("/dev/ttyS0", 115200)

def getTFminiData():
    while True:
        count = ser.in_waiting
        if count > 8:
            recv = ser.read(9)
            ser.reset_input_buffer()
            if recv[0] == 0x59 and recv[1] == 0x59: # 0x59 is 'Y'
                dist = recv[2] + recv[3]*256
                strength = recv[4] + recv[5]*256
                return dist


if __name__ == '__main__':
    try:
        if ser.is_open == False:
            ser.open()
        getTFminiData()
    except KeyboardInterrupt:   # Ctrl+C
        if ser != None:
            ser.close()
