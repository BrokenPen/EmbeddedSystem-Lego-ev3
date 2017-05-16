#!/bin/python3
#*******************************************************************************
# Sources      : 
# Link         :
# File         : key_robot.py
# Title        : Use ssh to remote LEGO EV3
# Author       : github.com/BrokenPen
# Code version : 0.1
# create date  : 2017 May 10, 16:59 UTD+8
#******************************************************************************/

#*******************************************************************************
# Last Modifited : 2017 May 10, 15:30, change for python3, BrokenPen
#******************************************************************************/



# import curses and ev3
import curses
from ev3dev.ev3 import *

# declare motor port
left_motor = LargeMotor('outB')
right_motor = LargeMotor('outC')


# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
screen = curses.initscr()
curses.noecho() 
curses.cbreak()
screen.keypad(True)

try:
        while True:   
            char = screen.getch()
            if char == ord('q'):
                break
            elif char == curses.KEY_UP:
                left_motor.run_timed(time_sp=50, speed_sp=+750)
                right_motor.run_timed(time_sp=50, speed_sp=+750)
            elif char == curses.KEY_DOWN:
                left_motor.run_timed(time_sp=50, speed_sp=-750)
                right_motor.run_timed(time_sp=50, speed_sp=-750)
            elif char == curses.KEY_RIGHT:
                left_motor.run_timed(time_sp=50, speed_sp=-750)
                right_motor.run_timed(time_sp=50, speed_sp=+750)                
            elif char == curses.KEY_LEFT:
                left_motor.run_timed(time_sp=50, speed_sp=+750)
                right_motor.run_timed(time_sp=50, speed_sp=-750)
            elif char == 10:
               pritn("nothing")
             
finally:
    #Close down curses properly, inc turn echo back on!
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    Sound.beep()
    

