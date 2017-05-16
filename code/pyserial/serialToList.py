#!/bin/python3

import serial
import time

# open serial port 
ser = serial.Serial('/dev/ttyUSB0')

# inital global variable
temp = ""
humi = ""

while True:
    
    # read a line from serial port
    line = ser.readline()
    # when line is not empty
    if (line != ""):
		# use [:-2] to exclude /r/n 
        # print(line[:-2].decode())
        
        temp, humi = line[:-2].decode().split(",");
        print("temp : ",temp)
        print("humi : ",humi)
        print("------------------")
        
    # delay 1 second
    time.sleep(1)
