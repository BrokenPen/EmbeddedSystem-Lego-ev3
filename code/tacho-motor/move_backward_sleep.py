#!/usr/bin/env python3

from ev3dev.ev3 import *
from time import sleep

left_motor = LargeMotor('outB')
right_motor = LargeMotor('outC')

left_motor.run_timed(time_sp=3000, speed_sp=-750)
right_motor.run_timed(time_sp=3000, speed_sp=-750)

print("set left motor speed (speed_sp) = " + str(left_motor.speed_sp))
print("set right motor speed (speed_sp) = " + str(right_motor.speed_sp))
sleep(1)  # it takes a moment for the motor to start moving

print("left motor actual speed = " + str(left_motor.speed))
print("right motor actual speed = " + str(left_motor.speed))

sleep(4)

Sound.beep()
