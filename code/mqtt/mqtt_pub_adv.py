

#!/usr/bin/env python3

import paho.mqtt.client as mqtt
from ev3dev.auto import *

# This is the Subscriber

m = MediumMotor(OUTPUT_A)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("topic/motor-A/dt")

def on_message(client, userdata, msg):
    if (msg.payload == 'Q'):
      m.stop()
      client.disconnect()
    elif (-100 <= int(msg.payload) <= 100):
      m.duty_cycle_sp=msg.payload

client = mqtt.Client()
client.connect("localhost",1883,60)

client.on_connect = on_connect
client.on_message = on_message

m.run_direct()
m.duty_cycle_sp=0

client.loop_forever()

