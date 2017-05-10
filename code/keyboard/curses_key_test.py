#*******************************************************************************
# Sources     : ExplainingComputers.com: Raspberry Pi Zumo Robot
# Article     : http://explainingcomputers.com/rasp_pi_robotics.html
# Link        : http://explainingcomputers.com/sample_code/key_robot_dance.py
# File        : curses_key_test.py
# access date : 2017 May 10, 16:59 UTD+8
#******************************************************************************/

#*******************************************************************************
# Last Modifited : 2017 May 10, 15:30, change for python3, BrokenPen
#******************************************************************************/

#!/bin/python3
import curses

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
                print ("up")
            elif char == curses.KEY_DOWN:
                print ("down")
            elif char == curses.KEY_RIGHT:
                print ("right")
            elif char == curses.KEY_LEFT:
                print ("left")
            elif char == 10:
                print ("stop" )   
             
finally:
    #Close down curses properly, inc turn echo back on!
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()

