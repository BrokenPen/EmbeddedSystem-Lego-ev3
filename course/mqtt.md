# mqtt

MQTT stands for MQ Telemetry Transport. It is a publish/subscribe, extremely simple and lightweight messaging protocol, designed for constrained devices and low-bandwidth, high-latency or unreliable networks. [(mqtt org . What is MQTT)][mqtt]

<!--
### for the current state only installed= = not confige yet , ..
-->

## installation

- install open source mqtt broker : `mosquitto`
- install open source mqtt client : `mosquitto-clients` for testing
- install python mqtt library : `paho-mqtt`

## premise

assume you have run before

    sudo apt-get update -y & sudo apt full-upgarde -y

## install mqtt

      ssh robot@10.42.0.3
      sudo adduser mosquitto
      # type mosquitto as password for mosquitto, keep remaining field empty by pressing enter for Y
      sudo apt-get install mosquitto mosquitto-clients -y
      sudo apt-get install build-essential libwrap0-dev libssl-dev libc-ares-dev uuid-dev xsltproc -y


## confige mqtt

    # -c, overwrite existing files, I just dont use it
    # just make sure your pwfile is empty

Create mqtt client for connect mosquitto

    sudo su
    mkdir /etc/mosquitto
    echo "" > /etc/mosquitto/pwfile
    sudo mosquitto_passwd /etc/mosquitto/pwfile ev3
    # password : formosa

    sudo mosquitto_passwd  /etc/mosquitto/pwfile test
    # password : formosa

    sudo mkdir /var/lib/mosquitto/
    sudo chown mosquitto:mosquitto /var/lib/mosquitto/ -R

Configuration local

    cd /etc/mosquitto
    sudo cat mosquitto.conf
    # First line
    # Place your local configuration in /etc/mosquitto/conf.d/

Way to confige mosquitto

    cd /etc/mosquitto/conf.d
    ls
    # README
    cat README
    # Any files placed in this directory that have a .conf ending will be loaded as config files by the broker. Use this to make your local config.
    man mosquitto.conf

    # Let use the example text that I found in digitalocean.com
    # https://www.digitalocean.com/community/questions/how-to-setup-a-mosquitto-mqtt-server-and-receive-data-from-owntracks

    # confige mosquitto mqtt broker

    sudo nano /etc/mosquitto/conf.d/mosquitto.conf



Copy and Paste the follow content

    listener 1883 *
    persistence true
    persistence_location /var/lib/mosquitto/
    persistence_file mosquitto.db
    log_dest syslog
    log_dest stdout
    log_dest topic
    log_type error
    log_type warning
    log_type notice
    log_type information
    connection_messages true
    log_timestamp true
    allow_anonymous true
    password_file /etc/mosquitto/pwfile

Reset mosquitto service

    sudo /sbin/ldconfig
    sudo service mosquitto restart
    sudo update-rc.d mosquitto enable

Start mosquitto, make sure is started

    sudo mosquitto

---

## simple test mosquitto


you need two terminal to run subsriber and publisher side

    ssh robot@10.42.0.3
    sudo su root

simple test with authoration

### mqtt annmoymos connect

terminal 1 :

    sudo mosquitto

Result :

    1494404200: mosquitto version 1.3.4 (build date 2014-08-17 04:02:48+0000) starting
    1494404200: Using default config.
    1494404200: Opening ipv4 listen socket on port 1883.
    1494404200: Opening ipv6 listen socket on port 1883.
    1494404200: Warning: Address family not supported by protocol



terminal 2 :

    sudo mosquitto_sub -h 10.42.0.3 -p 1883 -t hello/world -d

Result :

    Client mosqsub/1365-ev3dev sending CONNECT
    Client mosqsub/1365-ev3dev received CONNACK
    Client mosqsub/1365-ev3dev sending SUBSCRIBE (Mid: 1, Topic: hello/world, QoS: 0)
    Client mosqsub/1365-ev3dev received SUBACK
    Subscribed (mid: 1): 0


---

terminal 3 :

    sudo mosquitto_pub -h 10.42.0.3 -p 1883 -d -t hello/world -m "hello"

Result :

    Client mosqpub/1367-ev3dev sending CONNECT
    Client mosqpub/1367-ev3dev received CONNACK
    Client mosqpub/1367-ev3dev sending PUBLISH (d0, q0, r0, m1, 'hello/world', ... (5 bytes))
    Client mosqpub/1367-ev3dev sending DISCONNECT

terminal 2 Result :

    Client mosqsub/1365-ev3dev received PUBLISH (d0, q0, r0, m0, 'hello/world', ... (5 bytes))
    hello

terminal 1 Result :

    ...
    1494404376: New connection from 10.42.0.3 on port 1883.
    1494404376: New client connected from 10.42.0.3 as mosqsub/1404-ev3dev (c1, k60).
    1494404387: New connection from 10.42.0.3 on port 1883.
    1494404387: New client connected from 10.42.0.3 as mosqpub/1405-ev3dev (c1, k60)
    ...

---

### mqtt auth connect

use username and password to connect

terminal 2 :

    mosquitto_sub -h 10.42.0.3 -p 1883 -t hello/world -d -u ev3 -P formosa

Result :

    Client mosqsub/600-ev3dev sending CONNECT
    Client mosqsub/600-ev3dev received CONNACK
    Client mosqsub/600-ev3dev sending SUBSCRIBE (Mid: 1, Topic: hello/world, QoS: 0)
    Client mosqsub/600-ev3dev received SUBACK
    Subscribed (mid: 1): 0

---

terminal 3 :

    mosquitto_pub -h 10.42.0.3 -p 1883 -d -t hello/world -m "hello" -u test -P formosa

Result :

    Client mosqpub/617-ev3dev sending CONNECT
    Client mosqpub/617-ev3dev received CONNACK
    Client mosqpub/617-ev3dev sending PUBLISH (d0, q0, r0, m1, 'hello/world', ... (5 bytes))
    Client mosqpub/617-ev3dev sending DISCONNECT


terminal 1 result :

    ...
    1494407699: New connection from 10.42.0.3 on port 1883.
    1494407699: New client connected from 10.42.0.3 as mosqsub/600-ev3dev (c1, k60, uev3).
    1494407739: New connection from 10.42.0.3 on port 1883.
    1494407739: New client connected from 10.42.0.3 as mosqpub/617-ev3dev (c1, k60, utest).
    ...


---



### troubleshooting

Result

    Error: Connection refused

Solution : Make sure the mosquitto broker is started!

    sudo mosquitto

### python mqtt library

    sudo apt-get install python3-pip  -y # pip ulitily
    sudo pip3 install paho-mqtt


### python mqtt publisher

    #!/usr/bin/env python3
    # import mqtt library
    import paho.mqtt.client as mqtt
    
    # This is the Publisher
    client = mqtt.Client()
    
    # connect to localhost /etc/hosts, ev3 self
    client.connect("localhost",1883,60)
    
    # public Hello world to class/ev3dev
    client.publish("class/ev3dev", "Hello world!");
    
    # after published the messenage, disconnect from the mqtt broker
    client.disconnect();



### python mqtt subsriber 

in python mqtt subsriber we need to implement on_connect and on_message function of mqtt.Client
    
    #!/usr/bin/env python3
    # import mqtt library
    import paho.mqtt.client as mqtt

    # This is the Subscriber

    
    def on_connect(client, userdata, flags, rc):
       # conver the connect result into string and print it
       print("Connected with result code "+str(rc))
       # subscribed after connect to mqtt broker
       client.subscribe("class/ev3dev")

    def on_message(client, userdata, msg):
       # conver the messenage payload part to string and print it out
       print(msg.topic+" "+str(msg.payload))
    
    
    client = mqtt.Client()
    
    # connect to localhost mqtt broker, ev3dev self
    client.connect("localhost",1883,60)

    # assign callback function
    client.on_connect = on_connect
    client.on_message = on_message

    # run the subscriber forever
    client.loop_forever()

### python mqtt keep publish data forever

In the above of python mqtt publisher example, only publish "Hello World" one time. To keep publish data in a short period or after a event/value changed, in  case publish more than one, simply add a while loop in python main part



    #!/usr/bin/env python3
    
    import paho.mqtt.client as mqtt
    # need some delay for each publish
    improt sleep
    
    # This is the Publisher
    client = mqtt.Client()
    
    # connect to localhost /etc/hosts, ev3 self
    client.connect("localhost",1883,60)
    
    # a variable to count how many time published
    counter = 0
    
    # while loop
    while True: 
       # public Hello world to class/ev3dev
       client.publish("class/ev3dev", "Hello world!");
       
       # increase counter and print 
       counter+=1
       print("publish count : ", str(counter))

       # wait 5 seconds
       sleep(5)
      
    # never reach here
    client.disconnect();
    
### python mqtt event driven

in this case, we want to after a value changed or a event trigger actived then publish messenage to mqtt broker. Simpley use a if condition in a while loop

    while True:
        if ts.value == 1 :
          client.publish("class/ev3dev/button", "button pressed")
          sleep(0.5)

### assigment 1

  write two program, python mqtt subsriber and publisher program while sensor value is changed, publish some info.
  
  

### assgiment 2

require : esp8266 lesson

   write two or more program, use esp8266(NodeMCU) to connect more sensor, when trigger is actived, ask esp8266 for data then puslibhs to mqtt broker.

## reference link

[mqtt]:
- FAQ - Frequently Asked Questions | MQTT. MQTT.ORG. [accessed 2017 May 6]. http://mqtt.org/faq
What is MQTT?

## Useful link

- paho-mqtt 1.2.3 : Python Package Index. paho-mqtt 1.2.3 : Python Package Index. [accessed 2017 May 6]. https://pypi.python.org/pypi/paho-mqtt/1.2.3
