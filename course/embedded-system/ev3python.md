# EV3 Python

Using the EV3 Python programming lanuage to control their robot.(#ev3-python)

## Installation

   sudo apt-get update -y && sudo apt-get install python3-ev3dev

## Control Lego EV3 tacho-motor

https://sites.google.com/site/ev3python/learn_ev3_python/using-motors

## move forward

use nano to create a new python file in tacho directory 

    cd /home/robot
    mkdir tacho-motor
    nano move_forward.py
    # type the follow code # or copy and paste

include the python3 language that we use in the code

`from ev3dev.ev3 improt` which mean improt everything from ev3dev.ev3 package

`from time import sleep` which mean improt sleep from time package

  from ev3dev.ev3 import *
  from time import sleep

`left_motor = LargeMotor('outB')` assign left_motor as the tacho-motor connected as `outB` port


  left_motor = LargeMotor('outB')
  right_motor = LargeMotor('outC')

`left_motor.run_timed(time_sp=3000,speed_sp=750)` giving the command to left_motor on run time.

`time_sp=3000` which mean 3s, unit as millisecond
`speed_sp=750` which mean 750/1000 full speed, 1000 as maximum forward speed, -1000 as maxinum backward speed.

  left_motor.run_timed(time_sp=3000, speed_sp=750)
  right_motor.run_timed(time_sp=3000, speed_sp=750)

`Sound.beep()` indictaed the program end by a a beep sound

  Sound.beep()

### execute the python code

ev3.python require root premssion to execute it, so need to use sudo to do so.

method 1, use sudo python3 to execute it

     sudo python3 move_forward.py

method 2, use giving wrapper to execute it

     sudo chmod +x move_forward.py

method 3, use the brickman gui interface

     sudo chmod +x move_forward.py

     Main-Page->File Browser->tacho-motor->move_forward.py


## Useful link

[ev3-python]:
- https://sites.google.com/site/ev3python/
