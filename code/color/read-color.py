
#!/usr/bin/env python3
# so that script can be run from Brickman

# title   : Example 7: EV3 color sensor in COL-COLOR mode and touch sensor
# sources : https://sites.google.com/site/ev3python/learn_ev3_python/using-sensors

from ev3dev.ev3 import *
from time   import sleep

# Connect EV3 color sensor to any sensor port
# and check it is connected.

cl = ColorSensor() 
assert cl.connected, "Connect a single EV3 color sensor to any sensor port"


# Put the color sensor into COL-COLOR mode.
cl.mode='COL-COLOR'

colors=('unknown','black','blue','green','yellow','red','white','brown')
while True:    # Stop program by pressing touch sensor button
    print(colors[cl.value()])
    Sound.speak(colors[cl.value()]).wait()
    sleep(1)
Sound.beep()
