#!/usr/bin/env python

import os
import sys
import time
import threading
import ctypes # to stop thread
import paho.mqtt.client as paho
import string
import random
import itertools
import subprocess

RECEIVE_COUNT = 0
PUBLISH_COUNT = 0 
CURRENT_SONG = ""
MPG123_VOLUME = "5000" # base on 32768 # mpg123 -f 32768 a.mp3


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def on_connect(client, userdata, flags, rc):
    print("[mqtt]"+"CONNACK received with code %d." % (rc))

def on_publish_print(topic, payload, qos):
  global PUBLISH_COUNT
  PUBLISH_COUNT += 1
  print "[mqtt]Published count : " + str(PUBLISH_COUNT) + "       QOS : " +str(qos); 
  print("[mqtt]"+topic+" : "+str(payload)) 

def on_publish(client, userdata, mid):
  #print("mid: " +str(mid))
  pass

def on_publish_track(data_name, send_index, topic, value):
   print "[mqtt]Sending " + data_name + ": " + str(send_index)
   print "[mqtt]"+topic + ":"
   print "[mqtt]"+str(value)  
   
def on_subscribe(client, userdata, mid, granted_qos):
    print("[mqtt]Subscribed: "+str(mid)+" "+str(granted_qos))
 
def on_message(client, userdata, msg):  
  global RECEIVE_COUNT
  RECEIVE_COUNT += 1
  print "[mqtt]Received count : " + str(RECEIVE_COUNT) + "       QOS : " +str(msg.qos); 
  print("[mqtt]"+msg.topic+" : "+str(msg.payload)) 

def it_is_not_playing():
     global CURRENT_SONG
     with open('music.pid') as file:
       t = file.read().strip()

     if(t == ""):
       return "[player]No song play yet"

     cmd = "ps -fp "+t+" | grep "+ t
     in_process = os.popen(cmd).read().strip()
     #print "in_process: "+in_process
     if (in_process == ""):
       return "[player]"+CURRENT_SONG+".mp3 is finished"  
     else:
       return False

def kill_mpg():
       with open('music.pid') as file:
          t = file.read().strip()  
 
       #os.system("sudo kill "+t)
       p = subprocess.Popen(["kill", t, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
       out, err = p.communicate()
    
       if (err != ""):   
         print "[player]Unkown Error(err) : "+err  
       if (out != ""):
         print "[player]Unkown Error(out) : "+out
           #print "[player]"+payload_msg+".mp3 is finished"  
         #else:
         

def player_stop(payload_msg):
     global CURRENT_SONG
    
     with open('music.pid') as file:
       t = file.read().strip()
     '''
     if(t == ""):
       print "[player]No song play yet"
       return

     cmd = "ps -fp "+t+" | grep "+ t
     in_process = os.popen(cmd).read().strip()
     #print "cmd :"+cmd
     #print "in  :"+in_process

     if (in_process == ""):
       print "[player]"+payload_msg+".mp3 is finished"  
     else:
     '''
     play_msg = it_is_not_playing()
     if(play_msg): #playing
       print play_msg
     else: #not playing

       kill_mpg()

       print "[player]Stop playing " + CURRENT_SONG + ".mp3"


     os.system("echo -n > music.pid")   
     CURRENT_SONG = ""

def mp3_exist(payload_msg):

     p = subprocess.Popen(['ls', payload_msg+".mp3"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
     out, err = p.communicate()
    
     if (err != ""):
       print "[player]No "+payload_msg+".mp3" 
       return False
     else:
       return True

     #/home/fa/project/mp3/
     #songAvailble = os.popen("ls "+payload_msg+".mp3").read().strip() #this one is wrong     

     # if(songAvailble.find("No such file or directory")) :  #wrong
     #  print "[player]No "+payload_msg+".mp3"               #wrong
     #  return                                               #wrong

def player_play(payload_msg):
     global MSG123_VOLUME
     global CURRENT_SONG
     CURRENT_SONG = payload_msg
     with open('music.pid') as file:
       t = file.read().strip()

     if ( t == ""):
       print "[player]No other song is playing"
       print "[player]Play " + CURRENT_SONG + ".mp3"
     else:
       print CURRENT_SONG + "is playing now"
     
     mpg123 = "mpg123 -a hw:2,0 -f "+MPG123_VOLUME+" "+payload_msg+".mp3"
     os.system(mpg123 +"  > /dev/null 2>&1 & echo $! > music.pid ")
     

def player_volume(client, payload_msg):
  global MPG123_VOLUME
  if(payload_msg == "vol--"):
    MPG123_VOLUME = str(int(MPG123_VOLUME)-500)
  elif(payload_msg == "vol++"):
    MPG123_VOLUME = str(int(MPG123_VOLUME)+500)

  client.publish(main.nanopim1_music_status_topic[0], "Volume : "+MPG123_VOLUME, 0, False)   
  on_publish_track("Player Status", PUBLISH_COUNT, main.nanopim1_music_status_topic[0], "Volume : "+MPG123_VOLUME)

def player(client, payload_msg):
   global CURRENT_SONG
   global MPG123_VOLUME
   if(payload_msg == "offline"): # do nothing # the lwt payload of self 
     return
   elif(payload_msg == "vol--" or payload_msg == "vol++"):
     player_volume(client, payload_msg)
     return
   elif(payload_msg == "stop"):
     if(CURRENT_SONG == ""):
       print "[player]No song playing"
     else:
       player_stop(payload_msg) # kill the mpg123 

   else:
     if(mp3_exist(payload_msg) == False): # mp3 file dont exist
       return
     else:
       player_stop(payload_msg) # kill the mpg123 # make sure only one mpg123 is running
       player_play(payload_msg)
       client.publish(main.nanopim1_music_status_topic[0], "Song : "+payload_msg, 0, False)   

   time.sleep(0.1)

def on_message_music(client, userdata, msg):
   client.on_message(client, userdata, msg)
   player(client, str(msg.payload)) # call mqtt music player 

def on_message_music_status(client, userdata, msg):
   global CURRENT_SONG
   global PUBLISH_COUNT
   
   if(str(msg.payload).strip() == "ask"):
     client.on_message(client, userdata, msg) # only log in right paylaod
     PUBLISH_COUNT += 1
     
     if (CURRENT_SONG == ""):
       value = "No Song Playing"
     else:
       value = CURRENT_SONG

     client.publish(main.nanopim1_music_status_topic[0], value, 0, False)   
     on_publish_track("Player Status", PUBLISH_COUNT, main.nanopim1_music_status_topic[0], value)
        
def main():

  try:
    os.system("echo -n > music.pid")
    client = paho.Client()

    # mqtt connection variable
    broker = "192.168.42.1"
    clientId = "nanopim1_" + id_generator()
    username = "nanopim1"
    password = "formosa"
    
    lwt_topic = "/sbc/nanopim1/music/status"
    lwt_messenage = "offline"
    lwt_qos = 1
    lwt_retain = False
      
    publish_id = 0 

    client = paho.Client()
    client.on_connect = on_connect
    client.on_publish = on_publish

    client.on_subscribe = on_subscribe
    client.on_message = on_message

    client.will_set(lwt_topic, lwt_messenage, lwt_qos, lwt_retain)
    client.username_pw_set(username, password)
    client.connect(broker, 1883)

    main.nanopim1_music_topic = ("/sbc/nanopim1/music" , 1)
    main.nanopim1_music_status_topic = ("/sbc/nanopim1/music/status", 0)
    subscribe_list = [main.nanopim1_music_topic, main.nanopim1_music_status_topic]
    client.subscribe(subscribe_list)
    print "[mqtt]subscribed topic: "+str(subscribe_list)

    client.message_callback_add(main.nanopim1_music_topic[0], on_message_music)
    client.message_callback_add(main.nanopim1_music_status_topic[0], on_message_music_status)
    
    client.publish(main.nanopim1_music_status_topic[0], "online", 0, False)   
    on_publish_track("Player Status :", PUBLISH_COUNT, main.nanopim1_music_status_topic[0], "online")
    
    client.loop_forever()

    # // Need to use thread to do 
    #while True:
    #  global CURRENT_SONG
    #  if(it_is_not_playing and CURRENT_SONG != ""):
    #    print "[player]"+CURRENT_SONG+".mp3 is finished"  
    #    client.publish(main.nanopim1_music_status_topic[0], "Song finished : "+CURRENT_SONG, 0, False)   
    #    os.system("echo -n > music.pid")   
    #    CURRENT_SONG = ""
    #  time.sleep(1)

  except Exception, e:
    kill_mpg()
    print e
  except KeyboardInterrupt:
    kill_mpg()
    pass
  finally:
    kill_mpg()
    pass
        
        
if __name__ == '__main__':
  main()
    
