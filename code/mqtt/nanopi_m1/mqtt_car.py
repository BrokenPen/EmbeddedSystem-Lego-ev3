

import paho.mqtt.client as paho
import time
import string
import random
import threading
import ctypes # to stop thread
import sys
import Matrix.GPIO as GPIO

LEFT_MOTOR = 29
RIGHT_MOTOR = 31
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


def on_message_car_left_motor(client, userdata, msg):
   client.on_message(client, userdata, msg)
   if (str(msg.payload) == "left_on") :
     print "[car]left motor on"
     GPIO.output(LEFT_MOTOR, GPIO.HIGH)
     #client.publish(nanopim1_led_topic[0], "on", 0, False)
     #client.publish(nanopim1_car_status_topic[0], "LED is ON now", 0, False)
   elif (str(msg.payload) == "left_off") :
     print "[car]left motor off"
     GPIO.output(LEFT_MOTOR, GPIO.LOW)
     #client.publish(nanopim1_led_topic[0], "on", 0, False)
     #client.publish(nanopim1_car_status_topic[0], "LED is ON now", 0, False)
 


def on_message_car_right_motor(client, userdata, msg):
   client.on_message(client, userdata, msg)

   if (str(msg.payload) == "right_on") :
     GPIO.output(RIGHT_MOTOR, GPIO.HIGH)
     #client.publish(nanopim1_led_topic[0], "off", 0, False)
     #client.publish(nanopim1_car_status_topic[0], "LED is OFF now", 0, False)
   elif (str(msg.payload) == "right_off") :
     GPIO.output(RIGHT_MOTOR, GPIO.LOW)
     #client.publish(nanopim1_led_topic[0], "off", 0, False)
     #client.publish(nanopim1_car_status_topic[0], "LED is OFF now", 0, False)

def on_message_car(client, userdata, msg):
   #client.on_message(client, userdata, msg)
    left_temp = GPIO.input(LEFT_MOTOR)
    right_temp = GPIO.input(RIGHT_MOTOR)
    if (str(msg.payload) == "forward") :
     GPIO.output(LEFT_MOTOR, GPIO.HIGH)
     GPIO.output(RIGHT_MOTOR, GPIO.HIGH)
    elif (str(msg.payload) == "none") :
     GPIO.output(LEFT_MOTOR, GPIO.LOW)
     GPIO.output(RIGHT_MOTOR, GPIO.LOW)
    elif (str(msg.payload) == "left") :
     GPIO.output(LEFT_MOTOR, GPIO.LOW)
     GPIO.output(RIGHT_MOTOR, GPIO.HIGH)
     time.sleep(0.2)
     GPIO.output(LEFT_MOTOR, left_temp)
     GPIO.output(RIGHT_MOTOR, right_temp)
    elif (str(msg.payload) == "right") :
     GPIO.output(LEFT_MOTOR, GPIO.HIGH)
     GPIO.output(RIGHT_MOTOR, GPIO.LOW)
     time.sleep(0.2)
     GPIO.output(LEFT_MOTOR, left_temp)
     GPIO.output(RIGHT_MOTOR, right_temp)


def on_message_car_direction(client, userdata, msg):
   client.on_message(client, userdata, msg)

   if (str(msg.payload) == "move_forward") :
     GPIO.output(LEFT_MOTOR, GPIO.HIGH)
     GPIO.output(RIGHT_MOTOR, GPIO.HIGH)
     #client.publish(nanopim1_led_topic[0], "off", 0, False)
     #client.publish(nanopim1_car_status_topic[0], "LED is OFF now", 0, False)
     client.publish(nanopim1_car_topic[0][:-2]+"/left_motor", "left_on", 0, False)
     #time.sleep(0.01)
     client.publish(nanopim1_car_topic[0][:-2]+"/right_motor", "right_on", 0, False)
   elif (str(msg.payload) == "release") :
     GPIO.output(LEFT_MOTOR, GPIO.LOW)
     GPIO.output(RIGHT_MOTOR, GPIO.LOW)
     client.publish(nanopim1_car_topic[0][:-2]+"/left_motor", "left_off", 0, False)
     #time.sleep(0.01)
     client.publish(nanopim1_car_topic[0][:-2]+"/right_motor", "right_off", 0, False)
     #client.publish(nanopim1_led_topic[0], "off", 0, False)
     #client.publish(nanopim1_car_status_topic[0], "LED is OFF now", 0, False)



'''
def on_message_car_status(client, userdata, msg):
   client.on_message(client, userdata, msg)
   if (str(msg.payload) == "ask"):
     if(GPIO.input(LED_PIN) == GPIO.HIGH): 
       client.publish(nanopim1_led_status_topic[0], "LED is ON now", 0, False)
     elif(GPIO.input(LED_PIN) == GPIO.LOW): 
       client.publish(nanopim1_led_status_topic[0], "LED is OFF now", 0, False)
'''

def program_exit():
    pass  

nanopim1_car_topic = ("/sbc/nanopim1/car/#", 0)
nanopim1_car_status_topic =  ("/sbc/nanopim1/car/status", 0)  
        
try:
    #gpio inital

    GPIO.setmode(GPIO.BOARD)
    GPIO.cleanup(LEFT_MOTOR)
    GPIO.cleanup(RIGHT_MOTOR)
    GPIO.setup(LEFT_MOTOR, GPIO.OUT)
    GPIO.setup(RIGHT_MOTOR, GPIO.OUT)
    GPIO.output(LEFT_MOTOR, GPIO.LOW)
    GPIO.output(RIGHT_MOTOR, GPIO.LOW)


    

    # mqtt connection variable
    broker = "192.168.42.1"
    clientId = "nanopim1_" + id_generator()
    username = "nanopim1"
    password = "formosa"
        
    lwt_topic = nanopim1_car_status_topic[0]
    lwt_messenage = "offline"
    lwt_qos = 1
    lwt_retain = False
    
    subscribe_topic = [nanopim1_car_topic, nanopim1_car_status_topic]
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

    #client.message_callback_add(nanopim1_car_topic[0], on_message_car)
    client.message_callback_add(nanopim1_car_topic[0][:-2]+"/direction", on_message_car_direction)
    client.message_callback_add(nanopim1_car_topic[0][:-2]+"/left_motor", on_message_car_left_motor)
    client.message_callback_add(nanopim1_car_topic[0][:-2]+"/right_motor", on_message_car_right_motor)
    client.message_callback_add(nanopim1_car_topic[0][:-2], on_message_car)
    

    client.loop_forever()

except KeyboardInterrupt :
    program_exit()
finally :
    program_exit()
    raise
  




