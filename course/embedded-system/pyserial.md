## pyserial

pyserial is a python serial port extension. This course use pyserial to access uart of esp8266 for ev3dev.


## installation

    sudo apt-get install python3-pip -y
    sudo pip3 install pyserial

## prepare 

`./course/esp8266.md`
  
## Read string from uart 

A  baisc python serial program for reading string from serial

`./code/pyserial/readSerial.py`

    #!/bin/python3

    import serial
    import time

    # open serial port 
    ser = serial.Serial('/dev/ttyUSB0')

    while True:
	    
        # read a line from serial port
        line = ser.readline()
        # when line is not empty
        if (line != ""):
            # use [:-2] to exclude /r/n 
            print(line[:-2].decode())
		
        # delay 1 second
	    time.sleep(1)
	    
	    
### split uart string into list     
    
`/code/pyserial/serialToList.py`

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

***
	

### Read serial and write to ev3 lcd

Use temperture and humidty value read from serial update to lego ev3 brick LCD.
	    
`./code/pyserial/serialToEv3LCD.py`


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

***

### Useful Link

https://pypi.python.org/pypi/pyserial