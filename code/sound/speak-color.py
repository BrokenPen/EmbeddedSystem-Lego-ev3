#!/usr/bin/env python3
# so that script can be run from Brickman

from time import sleep   # needed for sleep
from ev3dev.ev3 import *  # needed for Sound

#play a standard beep
Sound.beep()

sleep(2)  # pause for 2 seconds


while True:
  #text to speech
  Sound.speak('Hello, my name is E V 3!').wait()
  sleep(1) # pause for 1 second
