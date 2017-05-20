## keyboard control

To remote control the Lego EV3 robot in ev3dev as a RC robot, simple use ssh to connect ev3dev and implement python cursos to control the ev3dev.

***

### python cursos

use try, catch, finally to handle error. 

first need to import the python curses library, second init the curses, thirdy config curses, fourlty setup condition when keyboard is pressed, finally close down curses properly.

`./code/keyboard/curses_key_test.py`


    #!/bin/python3
    import curses

    screen = curses.initscr() # Get the curses window
    curses.noecho()           # turn off echoing of keyboard to screen
    curses.cbreak()           # no enter key require
    screen.keypad(True)       # use special vlaues for cursor keys

    try:
        # while loop
        while True:   
            # read a char from the screen 
            char = screen.getch()
            # when q key is pressed, case sensitly! small little of q
            if char == ord('q'):
                break
            # when UP key is pressed
            elif char == curses.KEY_UP:
                print ("up")
            # when DOWN key is pressed
            elif char == curses.KEY_DOWN:
                print ("down")
            # when RIGHT key is pressed
            elif char == curses.KEY_RIGHT:
                print ("right")
            # when LEFT key is pressed
            elif char == curses.KEY_LEFT:
                print ("left")
            elif char == 10:
                print ("stop" )   
    
    catch Exception : 
          pass 
         
    finally:
        # Close down curses properly, inc turn echo back on!
        curses.nocbreak(); screen.keypad(0); curses.echo()
        curses.endwin()


***

change the print statement to ev3 motor control statement to enable control of ev3 as a remote robot



### ev3-python motor control

like a RC car remote, only pressing the joystick then the car is move. To do the same thing in ev3dev motor control use the motor function of `run_timed`, assign a short `time_sp` such as 50ms. (pull down a for 1second and count how many a are echoed, propelry more than 20 or up to 50), since code in run in while loop, the program never will end, a new fetch in curses will update the motor command, always 50ms more before the run_timed is timeout.

To move forward or backward simple change to speed_sp into negative or positive value as different approach(pologitation)

To turn left or turn right combine negative and positive speed_sp value. speed_sp up to 1000 and -1000 as 100% full speed

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
           
### more function           

Add a hammer? Remember in childhood my favourite robot programm is the `Robot Wars: The First Wars`(1998UK BBC, 2003-2005 in my boardcast country...)
 two robot in a flighting game, until one of them is non-functional...

A more motor less in the Lego ev3 box!

***

## Reference Link

Raspberry Pi Zumo Robot
- http://explainingcomputers.com/rasp_pi_robotics.html

## Useful Link

Using Motors - ev3python
- https://sites.google.com/site/ev3python/learn_ev3_python/using-motors

Curses Programming with Python — Python 3.6.1 documentationu
- https://docs.python.org/3/howto/curses.html

Robot Wars: The First Wars | Robot Wars Wiki | Fandom powered by Wikia
- http://robotwars.wikia.com/wiki/Robot_Wars:_The_First_Wars

