#!/bin/sh
LED1=/sys/class/leds/ev3\:left\:green\:ev3dev\brightness
while true;
   do 
   echo "255" > $LED1
   sleep 1
   echo "0" > $LED1
done
