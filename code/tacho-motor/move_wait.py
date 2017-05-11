#!/usr/bin/env python3

from ev3dev.ev3 import *
from time import sleep

# declare motor port 
left_motor = LargeMotor('outB')
right_motor = LargeMotor('outC')

print("move forward")
# move forward
left_motor.run_timed(time_sp=3000, speed_sp=+750)
right_motor.run_timed(time_sp=3000, speed_sp=+750)
# wait for the motor rotate complete
left_motor.wait_while('running')
right_motor.wait_while('running')

# print the giving speed
print("set left motor speed (speed_sp) = " + str(left_motor.speed_sp))
print("set right motor speed (speed_sp) = " + str(right_motor.speed_sp))
# print the actual speed
print("left motor actual speed = " + str(left_motor.speed))
print("right motor actual speed = " + str(left_motor.speed))


Sound.beep()
sleep(0.5)

print("move backward")
# move forward
left_motor.run_timed(time_sp=3000, speed_sp=-750)
right_motor.run_timed(time_sp=3000, speed_sp=-750)
# wait for the motor rotate complete
left_motor.wait_while('running')
right_motor.wait_while('running')

# print the giving speed
print("set left motor speed (speed_sp) = " + str(left_motor.speed_sp))
print("set right motor speed (speed_sp) = " + str(right_motor.speed_sp))
# print the actual speed
print("left motor actual speed = " + str(left_motor.speed))
print("right motor actual speed = " + str(left_motor.speed))


Sound.beep()
sleep(0.5)


print("move left")
# move left
left_motor.run_timed(time_sp=100, speed_sp=-750)
right_motor.run_timed(time_sp=100, speed_sp=+750)
# wait for the motor rotate complete
left_motor.wait_while('running')
right_motor.wait_while('running')

# print the giving speed
print("set left motor speed (speed_sp) = " + str(left_motor.speed_sp))
print("set right motor speed (speed_sp) = " + str(right_motor.speed_sp))

print("left motor actual speed = " + str(left_motor.speed))
print("right motor actual speed = " + str(left_motor.speed))

Sound.beep()
sleep(0.5)

print("move right")
# move left
left_motor.run_timed(time_sp=100, speed_sp=-750)
right_motor.run_timed(time_sp=100, speed_sp=+750)
# wait for the motor rotate complete
left_motor.wait_while('running')
right_motor.wait_while('running')

# print the giving speed
print("set left motor speed (speed_sp) = " + str(left_motor.speed_sp))
print("set right motor speed (speed_sp) = " + str(right_motor.speed_sp))

print("left motor actual speed = " + str(left_motor.speed))
print("right motor actual speed = " + str(left_motor.speed))

Sound.beep()
sleep(0.5)


