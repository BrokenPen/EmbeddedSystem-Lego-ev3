### Using mqtt protocol to transfer data

#### What is mqtt
  http://mqtt.org/
 
---

#### Install mqtt aplication in raspberry pi 3
  - Open soucres mqtt application : mosquitto
  
    my Raspberry Pi 3 pre-installed with Raspbain, configuration done(already in use)
    https://www.raspberrypi.org/downloads/raspbian/
  According to the site( or apt-get update..), raspbian is using debian jessie end

  - Mosquitto offical install guide for debian repository
  https://mosquitto.org/2013/01/mosquitto-debian-repository/

---
  - Install step
        
        # login in to my RPI3 with ssh
        #
        ssh pi@192.168.42.1
        sudo apt-get install -y
        # Get:1 http://mirrordirector.raspbian.org jessie InRelease [14.9 kB] 
        # which mean using jessie debian end
        sudo adduser mosquitto
        sudo apt-get install mosquitto mosquitto-clients -y
  
  - Configure mosquitto

        # -c, overwrite existing files, I just dont use it
        # just make sure your pwfile is empty

        sudo mosquitto_passwd /etc/mosquitto/pwfile raspberrypi3
        # password : formosa
        
        sudo mosquitto_passwd  /etc/mosquitto/pwfile nanopim1
        # password : formosa

        sudo mosquitto_passwd  /etc/mosquitto/pwfile nodemcu
        # password : formosa

        ##client to control ..
        ##Use mqtt dashboard which download in andriod market
        sudo mosquitto_passwd  /etc/mosquitto/pwfile htc530
        # password : formosa

        ##a extra client to test..
        sudo mosquitto_passwd  /etc/mosquitto/pwfile thinkpad
        # password : formosa

        sudo mkdir /var/lib/mosquitto/
        sudo chown mosquitto:mosquitto /var/lib/mosquitto/ -R

        cd /etc/mostquitto
        sudo nano mosquitto.conf 
        # First line
        # Place your local configuration in /etc/mosquitto/conf.d/

        cd conf.d
        ls
        # README
        cat README
        # Any files placed in this directory that have a .conf ending will be loaded as config files by the broker. Use this to make your local config.
        man mosquitto.conf
        # Let use the example text that I found in digitalocean.com
        # https://www.digitalocean.com/community/questions/how-to-setup-a-mosquitto-mqtt-server-and-receive-data-from-owntracks
        sudo nano mosquitto.conf

        # Copy and Paste the follow content
        listener 1883 192.168.42.1
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
        allow_anonymous false
        password_file /etc/mosquitto/pwfile

        sudo /sbin/ldconfig
        sudo service mosquitto restart

---

  - Simple test mosquitto

        # you need two terminal to run subsriber and publisher side
        # ssh root@192.168.42.1
        
        # simple test with authoration
        # annmoymos connect  
        
        # terminal 1 :               
        mosquitto_sub -h 192.168.42.1 -p 1883 -t hello/world -d
        # Result : 
        # Client mosqsub/11891-BROKENPEN sending CONNECT
        # Client mosqsub/11891-BROKENPEN received CONNACK
        # Connection Refused: not authorised.
        
        # terminal 2 :   
        mosquitto_pub -h 192.168.42.1 -p 1883 -d -t hello/world -m "hello"
        # Result : 
        # Client mosqpub/12102-BROKENPEN sending CONNECT
        # Client mosqpub/12102-BROKENPEN received CONNACK
        # Connection Refused: not authorised.
        # Error: The connection was refused.
   
        # terminal 1 :  
        # use username and password to connect
        mosquitto_sub -h 192.168.42.1 -p 1883 -t hello/world -d -u raspberrypi3 -P formosa
        # Result :
        # Client mosqsub/18187-raspberry sending CONNECT
        # Client mosqsub/18187-raspberry received CONNACK
        # Client mosqsub/18187-raspberry sending SUBSCRIBE (Mid: 1, Topic: hello/world, QoS: 0)
        # Client mosqsub/18187-raspberry received SUBACK
        # Subscribed (mid: 1): 0

        # terminal 2 :   
        mosquitto_pub -h 192.168.42.1 -p 1883 -d -t hello/world -m "hello" -u nanopim1 -P formosa
        # Result : 
        # Client mosqpub/12210-BROKENPEN sending CONNECT
        # Client mosqpub/12210-BROKENPEN received CONNACK
        # Client mosqpub/12210-BROKENPEN sending PUBLISH (d0, q0, r0, m1, 'hello/world', ... (5 bytes))
        # Client mosqpub/12210-BROKENPEN sending DISCONNECT


---       
    
#### Topic in mqtt
  
    
  

#### Reference
  - mqtt
  http://mqtt.org/

  - mosquitto 
  English :

  https://mosquitto.org/2013/01/mosquitto-debian-repository/
  https://www.digitalocean.com/community/questions/how-to-setup-a-mosquitto-mqtt-server-and-receive-data-from-owntracks
  Chinese tutorial :
  http://cheng-min-i-taiwan.blogspot.tw/2015/03/raspberry-pimqtt-android.html
  
  - mosquitto manual
  https://mosquitto.org/man/
  https://mosquitto.org/man/mosquitto-8.html
  https://mosquitto.org/man/mosquitto_pub-1.html
   
  - raspbian
  https://www.raspberrypi.org/downloads/raspbian/

---

checked : Tuesday, 03. January 2017 12:11AM 
