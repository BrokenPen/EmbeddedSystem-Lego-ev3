

import paho.mqtt.client as paho
import time
import string
import random
import threading
import ctypes # to stop thread
import sys
import Matrix.GPIO as GPIO

LED_PIN = 18
COUNT = 0

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def on_connect(client, userdata, flags, rc):
    print("CONNACK received with code %d." % (rc))

def on_publish(client, userdata, mid):
    #print("mid: " +str(mid))
    pass
   
def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))
 
def on_message(client, userdata, msg):
    global COUNT
    COUNT += 1
    #print "Received count : " + str(COUNT); 
    print "Received count : " + str(COUNT) + "       QOS : " +str(msg.qos); 
    print(msg.topic+" : "+str(msg.payload)) 


def on_message_led(client, userdata, msg):
   client.on_message(client, userdata, msg)
   if (str(msg.payload) == "on") :
     GPIO.output(LED_PIN, GPIO.HIGH)
     #client.publish(nanopim1_led_topic[0], "on", 0, False)
     client.publish(nanopim1_led_status_topic[0], "LED is ON now", 0, False)
   elif (str(msg.payload) == "off") :
     GPIO.output(LED_PIN, GPIO.LOW)
     #client.publish(nanopim1_led_topic[0], "off", 0, False)
     client.publish(nanopim1_led_status_topic[0], "LED is OFF now", 0, False)

def on_message_led_status(client, userdata, msg):
   client.on_message(client, userdata, msg)
   if (str(msg.payload) == "ask"):
     if(GPIO.input(LED_PIN) == GPIO.HIGH): 
       client.publish(nanopim1_led_status_topic[0], "LED is ON now", 0, False)
     elif(GPIO.input(LED_PIN) == GPIO.LOW): 
       client.publish(nanopim1_led_status_topic[0], "LED is OFF now", 0, False)

def program_exit():
    pass  

nanopim1_led_topic = ("/sbc/nanopim1/led", 1)
nanopim1_led_status_topic =  ("/sbc/nanopim1/led/status", 0)  
        
try:
    #gpio inital

    GPIO.setmode(GPIO.BOARD)
    GPIO.cleanup(LED_PIN)
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.output(LED_PIN, GPIO.LOW)
    

    # mqtt connection variable
    broker = "192.168.42.1"
    clientId = "nanopim1_" + id_generator()
    username = "nanopim1"
    password = "formosa"
        
    lwt_topic = "/sbc/nanopim1/led/status"
    lwt_messenage = "offline"
    lwt_qos = 1
    lwt_retain = False
    
    subscribe_topic = [nanopim1_led_topic, nanopim1_led_status_topic]
    print subscribe_topic
 
    

    publish_id = 0 

    client = paho.Client()
    client.on_connect = on_connect
    client.on_publish = on_publish

    client.on_subscribe = on_subscribe
    client.on_message = on_message

    client.will_set(lwt_topic, lwt_messenage, lwt_qos, lwt_retain)
    client.username_pw_set(username, password)
    client.connect(broker, 1883)

    client.subscribe(subscribe_topic) # this fail.. no idea # workr now

    client.message_callback_add(nanopim1_led_topic[0], on_message_led)
    client.message_callback_add(nanopim1_led_status_topic[0], on_message_led_status)

    client.loop_forever()
    #client.loop_start()
    #client.loop_end()
except KeyboardInterrupt :
    program_exit()
finally :
    program_exit()
    raise
  




