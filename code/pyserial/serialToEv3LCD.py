#!/usr/bin/env python3
from time import sleep
from ev3dev.ev3 import *
import serial

# use ev3 brick lcd screen
lcd = Screen()

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
        #print("temp : ",temp)
        #print("humi : ",humi)
        #print("------------------")
        
        lcd.draw.rectangle((0,0,177,40), fill='black')
        lcd.draw.text((48,13),'TEMP : '+temp, fill='white')
        lcd.draw.text((36,80),'HUMI : '+humi)
        lcd.update()
        
    # delay 1 second
    sleep(1)
