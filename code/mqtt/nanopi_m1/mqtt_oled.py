#!/usr/bin/env python

import sys
import time
import Matrix.GPIO as GPIO
from oled import OLED
from oled import Font
from oled import Graphics
import threading
import ctypes # to stop thread

import paho.mqtt.client as paho
import string
import random


import itertools
TOGGLE = itertools.cycle(['gpio', 'mqtt']).next

THREADS = []

OLED_UPDATE = False
OLED_GPIO_UPDATE = -1 # inital as -1 as net setup yet
OLED_MQTT_UPDATE = False
OLED_MODE = 'gpio'

# GPIO IN pin set up
TOUCH_PAD = 8
VOICE_SENSOR = 10
EARTHQUAKE_SENSOR = 12
PIR_MOTION_SENSOR = 16

TOUCH_PAD_VALUE = -1
VOICE_SENSOR_VALUE = -1
EARTHQUAKE_SENSOR_VALUE = -1
PIR_MOTION_SENSOR_VALUE = -1

TOUCH_PAD_OLED_VALUE = -1
VOICE_SENSOR_OLED_VALUE = -1
EARTHQUAKE_SENSOR_OLED_VALUE = -1
PIR_MOTION_SENSOR_OLED_VALUE = -1

PUBLISH_COUNT = 0
RECEIVE_COUNT = 0


# GPIO OUT pin set up
#RED_LED = 7

#SOME GLOBAL VALUE FOR TEST
INDEX = 0

GPIO_CHAN = (TOUCH_PAD, VOICE_SENSOR, EARTHQUAKE_SENSOR, PIR_MOTION_SENSOR)

# i2c to OLED
I2C_BUS = 0
# Connect to the display on /dev/i2c-I2C_BUS
dis = OLED(I2C_BUS)

# mqtt variable
PUBLISH_THREADS = []
PUB_MUTEX = 0 # mqtt publish mutex

NODEMCU_DHT11_HUMI = 0
NODEMCU_DHT11_TEMP = 0
OLED_MSG = ""

def error_handler():
    GPIO.cleanup(GPIO_CHAN)
    dis.clear()
    f = Font(1)
    f.print_string(6, 0, "ERROR OCCURRED")

def oled_inital():
    # Start communication  
    dis.begin()
    # Start basic initialization
    dis.initialize() # always !!
    # Do additional configuration
    dis.set_memory_addressing_mode(0)
    dis.set_column_address(0, 127)
    dis.set_page_address(0, 7)
    # Clear display
    dis.clear()
    # Set font scale x1
    f = Font(1)
    # Print some large text
    f.print_string(0, 0, "Cloud Alarm")
    f.print_string(30, 8, "Starting")
    f = Font(3)
    f.print_string(0, 16, "|||||||||||||||||||||")
    #dont use any scroll please !!
    #dis.deactivate_scroll()
    # Send video buffer to display
    dis.update()
    time.sleep(2)
    dis.clear()
  

def pin_inital():
    try:
       GPIO.setmode(GPIO.BOARD)
       GPIO.setup(TOUCH_PAD, GPIO.IN)
       # GPIO.setup(RED_LED, GPIO.OUT)
       GPIO.setup(VOICE_SENSOR, GPIO.IN)
       GPIO.setup(EARTHQUAKE_SENSOR, GPIO.IN)
       GPIO.setup(PIR_MOTION_SENSOR, GPIO.IN)
    except Exception, e:
       print e
    # finally:
              

def program_end():
    GPIO.cleanup(GPIO_CHAN)
    dis.clear()
    f = Font(2)
    f.print_string(0, 0, "Program")
    f.print_string(0, 16, "Terminated")
    f.print_string(0, 32, "Good Bye!!")    
    dis.update()       
    time.sleep(2)
    dis.close()
    dis.update()

def oled_display():
    global INDEX
    global VOICE_SENSOR
    global VOICE_SENSOR_OLED_VALUE
    global EARTHQUAKE_SENSOR
    global EARTHQUAKE_SENSOR_OLED_VALUE
    global PIR_MOTION_SENSOR
    global PIR_MOTION_SENSOR_OLED_VALUE
    global TOUCH_PAD
    global TOUCH_PAD_OLED_VALUE
    global OLED_UPDATE
    global OLED_GPIO_UPDATE
    global OLED_MQTT_UPDATE
    global OLED_MODE
    global NODEMCU_DHT11_HUMI
    global NODEMCU_DHT11_TEMP
    global OLED_MSG
    

  #
    if VOICE_SENSOR_OLED_VALUE == -1:
      dis.clear()
      OLED_UPDATE = True  
    if OLED_MQTT_UPDATE == -1:
      dis.clear()
      OLED_MQTT_UPDATE = True  
  # 
  #  if GPIO.input(VOICE_SENSOR) != VOICE_SENSOR_OLED_VALUE:
  #    VOICE_SENSOR_OLED_VALUE = GPIO.input(VOICE_SENSOR)
  #    OLED_UPDATE = True
  #  if GPIO.input(EARTHQUAKE_SENSOR) != EARTHQUAKE_SENSOR_OLED_VALUE:
  #    EARTHQUAKE_SENSOR_OLED_VALUE = GPIO.input(EARTHQUAKE_SENSOR)
  #    OLED_UPDATE = True
  #  if GPIO.input(PIR_MOTION_SENSOR) != PIR_MOTION_SENSOR_OLED_VALUE:
  #    PIR_MOTION_SENSOR_OLED_VALUE = GPIO.input(PIR_MOTION_SENSOR)
  #    OLED_UPDATE = True
  #  if GPIO.input(TOUCH_PAD) != TOUCH_PAD_OLED_VALUE:
  #    TOUCH_PAD_OLED_VALUE = GPIO.input(TOUCH_PAD)
  #    OLED_UPDATE = True
  #
    if OLED_MODE == 'gpio':
      if OLED_GPIO_UPDATE:
        dis.clear()
        f = Font(1)
        f.print_string(0, 0,  "VOICE      :"+str(VOICE_SENSOR_OLED_VALUE))
        f.print_string(0, 9,  "EARTHQUAKE :"+str(EARTHQUAKE_SENSOR_OLED_VALUE))
        f.print_string(0, 18, "PIR_MOTION :"+str(PIR_MOTION_SENSOR_OLED_VALUE))  
        f.print_string(0, 27, "TOUCH_PAD  :"+str(TOUCH_PAD_OLED_VALUE)) 
        f.print_string(0, 36, str(INDEX))  
        #f.print_string(0, 0, "VOICE :"+str(VOICE_SENSOR_VALUE))
        #f.print_string(0, 16, "EARTHQUAKE :"+str(EARTHQUAKE_SENSOR_VALUE))
        #f.print_string(0, 32, "PIR_MOTION :"+str(PIR_MOTION_SENSOR_VALUE))  
        #f.print_string(0, 48, str(INDEX))  
        f.print_string(0, 45, "OLED MOD   :"+str(OLED_MODE))
        dis.update()  

    if OLED_MODE == 'mqtt':
      if OLED_MQTT_UPDATE:
        dis.clear()
        f = Font(1)
        
        #f.print_string(0, 0, "Mqtt       :"+str(VOICE_SENSOR_OLED_VALUE))
        #f.print_string(0, 9, "0123456789012345678901") # the width is 21 font1 char
        #f.print_string(0, 0, "Nodemcu DHT11")
        f.print_string(0, 0,  "humidity    :"+str(NODEMCU_DHT11_HUMI))
        f.print_string(0, 9,  "temperature :"+str(NODEMCU_DHT11_TEMP))
        f.print_string(0, 18, "Messenage   :"+str(OLED_MSG))
        #f.print_string(0, 18, "01234567890123456789010123456789012345678901012345678901234567890!")
        
        f.print_string(0, 45, "OLED MOD   :"+str(OLED_MODE))
        dis.update()  
        OLED_MQTT_UPDATE = False

def read_gpio():

    global INDEX
    global VOICE_SENSOR
    global VOICE_SENSOR_OLED_VALUE
    global EARTHQUAKE_SENSOR
    global EARTHQUAKE_SENSOR_OLED_VALUE
    global PIR_MOTION_SENSOR
    global PIR_MOTION_SENSOR_OLED_VALUE
    global TOUCH_PAD
    global TOUCH_PAD_OLED_VALUE
    global OLED_UPDATE
    global OLED_GPIO_UPDATE
    global OLED_MQTT_UPDATE
    global OLED_MODE
    OLED_UPDATE = False
    OLED_GPIO_UPDATE = False
    global client
    
    if GPIO.input(VOICE_SENSOR) != VOICE_SENSOR_OLED_VALUE:
      VOICE_SENSOR_OLED_VALUE = GPIO.input(VOICE_SENSOR)
      OLED_GPIO_UPDATE = True
      INDEX += 1
      client.publish("/sbc/nanopim1/sensor/voice", str(VOICE_SENSOR_OLED_VALUE), 0, False)
      on_publish_print("/sbc/nanopim1/sensor/voice", str(VOICE_SENSOR_OLED_VALUE), 0)
    if GPIO.input(EARTHQUAKE_SENSOR) != EARTHQUAKE_SENSOR_OLED_VALUE:
      EARTHQUAKE_SENSOR_OLED_VALUE = GPIO.input(EARTHQUAKE_SENSOR)
      OLED_GPIO_UPDATE = True
      INDEX += 1
      client.publish("/sbc/nanopim1/sensor/earthquake", str(EARTHQUAKE_SENSOR_OLED_VALUE), 0, False)
      on_publish_print("/sbc/nanopim1/sensor/earthquake", str(EARTHQUAKE_SENSOR_OLED_VALUE), 0)
    if GPIO.input(PIR_MOTION_SENSOR) != PIR_MOTION_SENSOR_OLED_VALUE:
      PIR_MOTION_SENSOR_OLED_VALUE = GPIO.input(PIR_MOTION_SENSOR)
      OLED_GPIO_UPDATE = True
      INDEX += 1
      client.publish("/sbc/nanopim1/sensor/pir_motion", str(PIR_MOTION_SENSOR_OLED_VALUE), 0, False)
      on_publish_print("/sbc/nanopim1/sensor/pir_motion", str(PIR_MOTION_SENSOR_OLED_VALUE), 0)
    if GPIO.input(TOUCH_PAD) != TOUCH_PAD_OLED_VALUE:
      TOUCH_PAD_OLED_VALUE = GPIO.input(TOUCH_PAD)
      OLED_GPIO_UPDATE = True
      INDEX += 1
      client.publish("/sbc/nanopim1/input/touch_pad", str(TOUCH_PAD_OLED_VALUE), 0, False)
      on_publish_print("/sbc/nanopim1/input/touch_pad", str(TOUCH_PAD_OLED_VALUE), 0)
      
      # a button down with 0.1s debounce
      if TOUCH_PAD_OLED_VALUE == GPIO.LOW :
        time.sleep(0.1)
      if GPIO.input(TOUCH_PAD) == GPIO.HIGH :
        OLED_MODE = TOGGLE()
        print "OLED MODE : " + OLED_MODE
        if OLED_MODE == 'mqtt':
          OLED_MQTT_UPDATE = True
      

def terminate_thread(thread):
    """Terminates a python thread from another thread.

    :param thread: a threading.Thread instance
    """
    if not thread.isAlive():
      return

    exc = ctypes.py_object(SystemExit)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(
        ctypes.c_long(thread.ident), exc)
    if res == 0:
      raise ValueError("nonexistent thread id")
    elif res > 1:
      # """if it returns a number greater than one, you're in trouble,
      # and you should call it again with exc=NULL to revert the effect"""
      ctypes.pythonapi.PyThreadState_SetAsyncExc(thread.ident, None)
      raise SystemError("PyThreadState_SetAsyncExc failed")

def kill_threads():
    global THREADS
    terminate_thread(THREADS)

def run_oled():
    oled_inital()
    pin_inital()
    while 1:
      read_gpio()
      oled_display()          
      time.sleep(0.001)

# ------------------------oled part end---------------------__#

# ------------------------mqtt part start-----bad coding sytle-#


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def on_connect(client, userdata, flags, rc):
    print("CONNACK received with code %d." % (rc))

def on_publish_print(topic, payload, qos):
  global PUBLISH_COUNT
  PUBLISH_COUNT += 1
  print "Published count : " + str(PUBLISH_COUNT) + "       QOS : " +str(qos); 
  print(topic+" : "+str(payload)) 

def on_publish(client, userdata, mid):
  #print("mid: " +str(mid))
  pass

def on_publish_track(data_name, send_index, topic, value):
   print "Sending " + data_name + ": " + str(send_index)
   print topic + ":"
   print str(value)  
   
def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))
 
def on_message(client, userdata, msg):
  #print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))     
  global RECEIVE_COUNT
  RECEIVE_COUNT += 1
  print "Received count : " + str(RECEIVE_COUNT) + "       QOS : " +str(msg.qos); 
  print(msg.topic+" : "+str(msg.payload)) 

def on_message_humi(client, userdata, msg):
   client.on_message(client, userdata, msg)
   global NODEMCU_DHT11_HUMI
   global OLED_MQTT_UPDATE
   NODEMCU_DHT11_HUMI = msg.payload
   OLED_MQTT_UPDATE = True
  

def on_message_temp(client, userdata, msg):
   client.on_message(client, userdata, msg)
   global NODEMCU_DHT11_TEMP
   global OLED_MQTT_UPDATE
   NODEMCU_DHT11_TEMP = msg.payload
   OLED_MQTT_UPDATE = True

def on_message_oled(client, userdata, msg):
   client.on_message(client, userdata, msg)
   global OLED_MSG
   global OLED_MQTT_UPDATE
   OLED_MSG = msg.payload
   OLED_MQTT_UPDATE = True
 
        
def kill_publish_threads():
    global PUBLISH_THREADS
    for thread in PUBLISH_THREADS:
        terminate_thread(thread)



   

  
#------------------The mqtt part end-------------#
#----------------- The real main ----------------#    
 

client = paho.Client()

nodemcu_dht11_humi_topic = ("/mcu/nodemcu/sensor/dht11/humidity", 0)
nodemcu_dht11_temp_topic = ("/mcu/nodemcu/sensor/dht11/temperature", 0)
nanopim1_oled_msg_topic = ("/sbc/nanopim1/oled" , 0)
subscribe_topic = [nodemcu_dht11_humi_topic, nodemcu_dht11_temp_topic, nanopim1_oled_msg_topic]

def main():
  global THREADS
  try:
    t = threading.Thread(target=run_oled)
    THREADS.append(t) 
    t.start()

    # mqtt connection variable
    broker = "192.168.42.1"
    clientId = "nanopim1_" + id_generator()
    username = "nanopim1"
    password = "formosa"
    
    lwt_topic = "/sbc/nanopim1"
    lwt_messenage = "offline"
    lwt_qos = 1
    lwt_retain = False
      

    
    publish_id = 0 

    #client = paho.Client()
    client.on_connect = on_connect
    client.on_publish = on_publish

    client.on_subscribe = on_subscribe
    client.on_message = on_message

    client.will_set(lwt_topic, lwt_messenage, lwt_qos, lwt_retain)
    client.username_pw_set(username, password)
    client.connect(broker, 1883)

    client.subscribe(subscribe_topic) # this fail.. no idea
    print subscribe_topic
  
    client.message_callback_add(nodemcu_dht11_humi_topic[0], on_message_humi)
    client.message_callback_add(nodemcu_dht11_temp_topic[0], on_message_temp)
    client.message_callback_add(nanopim1_oled_msg_topic[0], on_message_oled)

    #topic 1 :
    #t = threading.Thread(target=publish_hello_world, args=(,))
    #t1 = threading.Thread(target=publish_hello_world)
    #publish_threads.append(t1)
    #t1.start()

    #topic 2 :
    #t2 = threading.Thread(target=publish_goodbye_world)
    #publish_threads.append(t2)
    #t2.start()


    client.loop_forever()
    while 1:
     time.sleep(0.001)

  # ugly code but work
  except Exception, e:
    print e
  except KeyboardInterrupt:
    kill_threads()
    kill_publish_threads() # added mqtt
    print "threads successfully closed"
    program_exit()

  finally:
    dis.clear()
    #dis.send_data([0]*(64 * 128 // 8))
    dis.update()
    dis.close()
    kill_publish_threads() # added mqtt
    program_end()
    program_exit()
        



        
if __name__ == '__main__':
  main()
    
