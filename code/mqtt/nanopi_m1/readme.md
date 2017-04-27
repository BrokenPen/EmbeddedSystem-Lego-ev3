---
##Nanopi m1 wiki :

- http://wiki.friendlyarm.com/wiki/index.php/NanoPi_M1

---

##Prepare (in your linux computer)

Download Nanopi M1 offical debian image(you could find the download site in Nanopi M1 English wiki) and unzip it.
  
    wget http://www.mediafire.com/file/6a9wmjz826rvngw/nanopi-m1-debian-sd4g-20160907.img.zip
    unzip nanopi-m1-debian-sd4g-20160907.img.zip

---

##Nanopi M1 Hardware spec

### Hardware Spec

>
- CPU: Allwinner H3, Quad-core Cortex-A7@1.2GHz
- GPU: Mali400MP2@600MHz，Supports OpenGL ES2.0
- DDR3 RAM: 512MB/1GB
- Connectivity: 10/100M Ethernet
- Audio: 3.5mm audio jack/Via HDMI
- Microphone: Onboard microphone
- IR Receiver: Onboard IR receiver
- USB Host：Type A, USB 2.0 x 3
- MicroSD Slot x 1
- MicroUSB: for data transmission and power input, OTG
- Video Output: HDMI 1.4 1080P, CVBS
- DVP Camera Interface: 24pin, 0.5mm pitch FPC seat
- Debug Serial Port: 4Pin, 2.54mm pitch pin header
- GPIO: 2.54mm spacing 40pin, compatible with Raspberry Pi's GPIO. It includes UART, SPI, I2C, IO etc
- User Key: Power LED x 1, Reset x 1
- PC Size: 64 x 56mm
- Power Supply: DC 5V/2A
- OS/Software: u-boot，Ubuntu MATE，Debian
 
---
 
###Nanopi M1 layout
![NanoPi M1 Layout](http://wiki.friendlyarm.com/wiki/images/c/c9/NanoPi-M1-1602-if01.png  "NanoPi M1 Layout")

- Nanopi M1 GPIOs pin

>
| Pin# | Name                      | Linux gpio | Pin# |Name                           |Linux gpio|
|-----|-----------------------------------|-----|----|--------------------------------------|-----|
| 1  | SYS_3.3V                           |     | 2  | VDD_5V                               |     |
| 3  | I2C0_SDA                           |     | 4  | VDD_5V                               |     |
| 5  | I2C0_SCL                           |     | 6  | GND                                  |     |
| 7  | GPIOG11                            | 203 | 8  | UART1_TX/GPIOG6                      | 198 |
| 9  | GND                                |     | 10 | UART1_RX/GPIOG7                      | 199 |
| 11 | UART2_TX/GPIOA0                    | 0   | 12 | PWM1/GPIOA6                          | 6   |
| 13 | UART2_RTS/GPIOA2                   | 2   | 14 | GND                                  |     |
| 15 | UART2_CTS/GPIOA3                   | 3   | 16 | UART1_RTS/GPIOG8                     | 200 |
| 17 | SYS_3.3V                           |     | 18 | UART1_CTS/GPIOG9                     | 201 |
| 19 | SPI0_MOSI/GPIOC0                   | 64  | 20 | GND                                  |     |
| 21 | SPI0_MISO/GPIOC1                   | 65  | 22 | UART2_RX/GPIOA1                      | 1   |
| 23 | SPI0_CLK/GPIOC2                    | 66  | 24 | SPI0_CS/GPIOC3                       | 67  |
| 25 | GND                                |     | 26 | SPDIF-OUT/GPIOA17                    | 17  |
| 27 | I2C1_SDA/GPIOA19/PCM0_CLK/I2S0_BCK | 19  | 28 | I2C1_SCL/GPIOA18/PCM0_SYNC/I2S0_LRCK | 18  |
| 29 | GPIOA20/PCM0_DOUT/I2S0_SDOUT       | 20  | 30 | GND                                  |     |
| 31 | GPIOA21/PCM0_DIN/I2S0_SDIN         | 21  | 32 | GPIOA7                               | 7   |
| 33 | GPIOA8                             | 8   | 34 | GND                                  |     |
| 35 | UART3_CTS/SPI1_MISO/GPIOA16        | 16  | 36 | UART3_TX/SPI1_CS/GPIOA13             | 13  |
| 37 | GPIOA9                             | 9   | 38 | UART3_RTS/SPI1_MOSI/GPIOA15          | 15  |
| 39 | GND                                |     | 40 | UART3_RX/SPI1_CLK/GPIOA14            | 14  |

- Debug Port（UART0）
>
| Pin# | Name      |
|------|-----------|
| 1    | GND       |
| 2    | VDD_5V    |
| 3    | UART_TXD0 |
| 4    | UART_RXDO |

- DVP Camera IF Pin Spec
>
| Pin#         | Name        | Description                                            |
|--------------|-------------|--------------------------------------------------------|
| 1, 2         | SYS_3.3V    | 3.3V power output, to camera modules                   |
| 7,9,13,15,24 | GND         | Gound, 0V                                              |
| 3            | I2C2_SCL    | I2C Clock Signal                                       |
| 4            | I2C2_SDA    | I2C Data Signal                                        |
| 5            | GPIOE15     | Regular GPIO, control signals output to camera modules |
| 6            | GPIOE14     | Regular GPIO, control signals output to camera modules |
| 8            | MCLK        | Clock signals output to camera modules                 |
| 10           | NC          | Not Connected                                          |
| 11           | VSYNC       | vertical synchronization to CPU　from camera modules   |
| 12           | HREF/HSYNC  | HREF/HSYNC signal to CPU from camera modules           |
| 14           | PCLK        | PCLK  signal to CPU from camera modules                |
| 16-23        | Data bit7-0 | data signals                                           |

---

###Prepare (in your linux Computer)
ready a 4GB sd card with USB card reader plug in your computer or you just use sd slot for instead.

    # /dev/sdx is your sd card usb reader 
    # in my case is /dev/sdc
    # you should umount all partation in /dev/sdx if part. exist
    ls /dev/sd*
    ls /dev/sdc*
    sudo umount /dev/sdc1
    sudo umount /dev/sdc2 
    sudo dd if=nanopi-m1-debian-sd4g-20160907.img of=/dev/sdc

---

###Connect Nanopi with uart
ready a usb-ttl and connect Nanopi M1 uart pin also plug into your linux computer. After you done, power on your Nanopi M1 by mirco usb cable plug in usb charger(5V 2A is recommand)

>
- If the green LED is on and the blue LED is blinking this indicates your NanoPi M1 has successfully booted.
- If no LED blinking is undersupply.

- Debug Port（UART0) connect to USB-TTL
>
| NanoPi | NanoPi    | Usb-TTL |
|--------|-----------|---------|
| Pin#   | Name      | Name    |
| 1      | GND       | GND     |
| 2      | VDD_5V    | No Need |
| 3      | UART_TXD0 | RXD     |
| 4      | UART_RXDO | TXD     |

        # connect to Nanopi M1 by uart connection at buadrate at 115200
        sudo apt-get install screen -y
        screen /dev/ttyUSB0 115200

---

##Nanopi M1

- Nanopi M1 default user 
>
| Username | Password |
|----------|----------|
| fa       | fa       |
| root     | fa       |

Let login in with user:root passwd:fa

---

###Configure Nanopi M1 envoirment

---

####Network Connection

- Add Google dns
    
        # as always add google dns in your /etc/resovl.conf
        echo "nameserver 8.8.8.8" >> /etc/resolv.conf

- Rename your usb wifi adapter
        
        # find out the Hardware address of wifi NIC
        ifconfig wlan | grep HWaddr
        # in my case 
        # wlan0     Link encap:Ethernet  HWaddr 60:bb:5c:06:2e:1c
        
        # you may find a usb device register as similar info of above
        # simple edit the NAME="wlan0" to NAME="wifi0"
        nano /etc/udev/rules.d/70-persistent-net.rules
        # USB device 0x:0x (rtl8188eu)
        SUBSYSTEM=="net", ACTION=="add", DRIVERS=="?*", ATTR{address}=="60:bb:5c:06:2e:1c", ATTR{dev_id}=="0x0", ATTR{type}=="1", KERNEL=="wlan*", NAME="wifi0"
        
        # most easy way to get the new name by reboot
        # udevadm control --reload-rules # if this not work, you have to reboot
        reboot
        # also login as root as always
        ifconfig wifi0 start #make sure have start up
        # now type ifconfig, you sure see the NIC but no wlan0
        
- Setting up wifi connection
        
        #
        nano /etc/network/interfaces.d/wifi0
        # type in
        allow-hotplug wifi0
        iface wifi-fast inet dhcp
        wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
        
        #add your wifi connection info.
        nano /etc/wpa_supplicant/wpa_supplicant.conf
        # type in
        country=GB
        ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
        update_config=1

        network={
            ssid="YourWiFiSSID"
            psk="YourWiFiPassword"
            #psk=1b66ca678d6f439f7360686ff5eeb7519cdc44b76a40d96515e4eb807a6d408b
            #key_mgmet="WPA-PSK"
            #ap-scan="1"
        }
        
        #If your WiFi password has special characters or you don't want your password saved as plain text you can use "wpa_passphrase" to generate a psk for your WiFi password. Here is how you can do it:
        wpa_passphrase YourWiFiESSID
        
        ifdown wifi0
        ifup wifi0
        
        # as assume your wifi working well. now you can access the Internet
        
---

####Package installation
        
- Update your package

        apt-get update -y
        
- Use i2c connection
   
        apt-get install i2c-tools -y
        # Determine which bus is in use and address
        i2cdetect -y -r 0
        # You may see the address is 3c on bus 1
        i2cdetect -y -r 1
        
- Backup the sd card(clone the sd card)

         shutdown -h -t now
         
         # Linux computer side
         # get your sd card and plug in your linux computer
         # alwyas umount partation
         sudo umount /dev/sdc1
         sudo umount /dev/sdc2 
         dd if=/dev/sdc of=nanopi_m1_backup.img
        
        #>
        #note : Network configuration finish and installed i2c-tools only
        
- Use ssh to connect Nanopi M1

    your linux computer side
        
        # to find out what machine connect in the same network
        arp
        # in my case, the nanopi m1 ip is 192.168.42.3
        ssh -l root 192.168.42.3
       
--- 

- Install FamilyArm offical C gpio library : Martix
        
        git clone https://github.com/friendlyarm/matrix.git
        cd matrix
        make && make install
        # test
        cd demo
        cd matrix-gpio_out
        make
        ./Matrix-gpio_out
        #Led on pin(7) blinking, is work

- Install python library

        apt-get update -y
        apt-get install python-pip -y
        # pip install sysv_ipc # IPC communcation
        
---

-   ==- (not work)pip install gpio==
       gpio is not work for nanopi m1(h3)
       
       
        pip install gpio
        #
        #File : test.py
        #!/usr/bin/env python
        import gpio
              gpio.setup(7,'out')
              gpio.set(7,0)
       
        python test.py     
        DEBUG:gpio:Write 7: 0
        DEBUG:gpio:writing: <open file '/sys/class/gpio/gpio7/value', mode 'w+' at 0xb6a56e90>: 0
        DEBUG:gpio:Write 7: 1
        DEBUG:gpio:writing: <open file '/sys/class/gpio/gpio7/value', mode 'w+' at 0xb6a56e90>: 1
       
        # remove gpio because dont work
        pip uninstall gpio
            
- ==- (not work)pip install cgpio==
   >
   Souces : [cgpio 0.7 : Python Package Index](https://pypi.python.org/pypi/cgpio/0.7) 
  >>
   a gpio class based on gpio-0.1.2
   Accesiing Pi-gpio the standard linux [sysfs interface],
   tested on RPI, NanoPi M1

       
        pip install cgpio
        #
        #File : test.py
        #!/usr/bin/env python
        import gpio
              gpio.setup(7,'out')
              gpio.set(7,0)
       
        python test.py     
        DEBUG:gpio:Write 7: 0
        DEBUG:gpio:writing: <open file '/sys/class/gpio/gpio7/value', mode 'w+' at 0xb6a56e90>: 0
        DEBUG:gpio:Write 7: 1
        DEBUG:gpio:writing: <open file '/sys/class/gpio/gpio7/value', mode 'w+' at 0xb6a56e90>: 1
       
        # remove gpio because dont work
        pip uninstall cgpio
        
---
       
- use command to access sysfs interface
      [GPIO Sysfs Interface for Userspace](https://www.kernel.org/doc/Documentation/gpio/sysfs.txt)
      
     >
     by caluate pin linux gpio
     pin = GROUP start offset + pin#
     GPIOG_11 = 192 + 11 = 203
     >
| chip        | group | register |
|-------------|-------|-------|
| gpiochip0   | GPIOA | 32bit |
| gpiochip32  | GPIOB | 32bit |
| gpiochip64  | GPIOC | 32bit |
| gpiochip96  | GPIOD | 32bit | 
| gpiochip128 | GPIOE | 32bit |
| gpiochip160 | GPIOF | 32bit |
| gpiochip192 | GPIOG | 32bit |
| gpiochip224 | GPIOH | 32bit |

      >
      
      after caluation or
      according to the Nanopi M1 gpio layout, GPIOG_11(pin# 7) which linux gpio is 203
      
        cd /sys/class/gpio
        echo "203" > export
        cd gpio203
        cat directin # output in
        cat value # output 0
        echo "out" > direction
        echo "1" > value
        # led light # I have connected a LED.
        
---        

- (Custom version)FramilyArm Martix-Python
      Sources : [friendlyarm/matrix-python](https://github.com/friendlyarm/matrix-python) 
      
      Offical Martix-Python Martix.GPIO/gpio.c file : [matrix-python/gpio.c at master · friendlyarm/matrix-python](https://github.com/friendlyarm/matrix-python/blob/master/Matrix.GPIO/gpio.c) 
      
        #Line 7 - 11
        static int pinGPIO[GPIO_MAX_NUM+1] = {-1, -1, -1, 99, -1, 98, -1,  60, 117, -1, 113,
            61, 58, 62, -1, 63, 78,  -1,  59, 95, -1,
            96, 97, 93, 94, -1, 77, 103, 102, 72, -1,
            73, 92, 74, -1, 76, 71,  75, 162, -1, 163,
        };
 
      Offical Martix Martix.GPIO/gpio.c file : [https://github.com/friendlyarm/matrix/blob/master/lib/gpio.c](matrix/gpio.c at master · friendlyarm/matrix) 
      
        #Line 22 - 31
        case BOARD_NANOPI_2:{        
        int tempPinGPIO[41] = {-1, -1, -1, 99, -1, 98, -1,  60, 117, -1, 113,
                                   61, 58, 62, -1, 63, 78,  -1,  59, 95, -1,
                                   96, 97, 93, 94, -1, 77, 103, 102, 72, -1,
                                   73, 92, 74, -1, 76, 71,  75, 162, -1, 163,
                                  };
        memcpy(pinGPIO, tempPinGPIO, sizeof(pinGPIO));
        ret = 0;
        break;
        }
        
       Which mean Martix-Python is design for ==NanoPi 2== only in gpio section
       
       ----
       
       ==Let try to replace the Martix-Python Martix.GPIO/gpio.c pinGPIO array with NanoPi M1 gpio==
       
       I find in Martix Martix.GPIO/gpio.c
       
        #Line 12 - 21     
        case BOARD_NANOPI_M1: {
        int tempPinGPIO[41] = {-1, -1, -1, -1, -1, -1,  -1, 203, 198, -1, 199,
                                    0,  6,  2, -1,  3, 200,  -1, 201, -1, -1,
                                   -1,  1, -1, -1, -1,  -1,  -1,  -1, 20, -1,
                                   21,  7,  8, -1, 16,  13,   9,  15, -1, 14,
                                  };
        memcpy(pinGPIO, tempPinGPIO, sizeof(pinGPIO));
        ret = 0;
        break;
        }
        
       My version of Martix-Python Martix.GPIO/gpio.c
       [matrix-python/gpio.c at master · BrokenPen/matrix-python](https://github.com/BrokenPen/matrix-python/blob/master/Matrix.GPIO/gpio.c) 
       
        #Line 8 - 15
        // Todo : other board competitive
        // Note : pinGOIO is for NanoPi M1
        static int pinGPIO[GPIO_MAX_NUM+1] = {
            -1, -1, -1, -1, -1, -1,  -1, 203, 198, -1, 199,
            0,  6,  2, -1,  3, 200,  -1, 201, -1, -1,
            -1,  1, -1, -1, -1,  -1,  -1,  -1, 20, -1,
            21,  7,  8, -1, 16,  13,   9,  15, -1, 14,
        };
               
        
       ==Let try install my version Martix-Python==
       Work!!!
       
        apt-get install python-dev -y
        git clone https://github.com/BrokenPen/matrix-python/
        cd matrix-python
        cd Matrix.GPIO
        python setup.py install
        cd test
        python matrix_led.py
        light on 
        light off
        #pin7 led on and off, is working!!

---

- install wiringNP(wiringPi for NanoPi)

        git clone https://github.com/friendlyarm/WiringNP
        cd WiringNP
        chmod +x ./build
        ./build
        #test wiringNP uility
        gpio readall
        gpio mode 7 out
        gpio pin 7 1
        gpio pin 7 0
        gpio reset
        #led on and led off, WiringNP is working!

--- 
        
- make a backup again..

---

- Prepare pyMOD-OLED install dependencies
        
        apt-get install python-dev python-setuptools libffi-dev -y
        pip install image
        
- install pyMOD-OLED()
        
        # i2c need root privileges to access
        # make sure you are login in as root
        # or use 
        # sudo python Hello_World.py

        # pip install mod-oled-128x64
        # or
        git clone https://github.com/StefanMavrodiev/pyMOD-OLED
        cd pyMOD-OLED
        python setup.py install
        
        # test
        cd example
        python Hello_World.py # work

        nano Draw_Bitmap.py
        # dis = OLED(1) change to 
        # dis = OLED(0) # i2c on /dev/i2c-0
        python Draw_Bitmap.py 
        # work but.. the horizontal scroll setup in Hello_World.py also affect the clown in Draw Bitmap too..
        # even I try run Draw_Bitmap.py the horizontal affect still
        # It is the design of ssd1602
        
        #pip uninstall mod-oled-128x64
        
---
 
 - make a backup again..

---

   

- install python mqtt library
 
        #detail : http://www.hivemq.com/blog/mqtt-client-library-paho-python
        pip install paho-mqtt

---

- insatll python uuid library(installation is fial on my nanopim1)
    
        pip install uuid
        #example code : 
        import uuid
        print uuid.uuid4()
        print str(uuid.uuid4().fields[-1])[:5]
        
        pip uninstall uuid
   
---
        
- use python random to generate a random id
  http://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python
  
--- 

## Install ftp

   # more ..
   https://www.raspberrypi.org/documentation/remote-access/ftp.md

- :
   
        # I just need to access the file by ftp
        # I use fa or root to login ftp.
        # so I don't need extra setting
        apt-get update -y
        apt-get install pure-ftpd -y
        
---

##Try to play music on nanopim1

- : Install pygame

        pip install pygame
        # Error
        sh: 1: sdl-config: not found

        # fix
        wget http://www.libsdl.org/release/SDL-1.2.14.tar.gz
        tar -xzvf SDL-1.2.14.tar.gz
        cd SDL-1.2.14
        ./configure 
        sudo make all
        # after a long long long time

        pip install pygame
        # same problem

        # try..
        sudo apt-get python-pygame
        # problem fix
        # but seem don't fix to my mp3 file
        # or the default output sound device is wrong

        # try vlc library
        sudo apt-get install libvlc-dev -y
        
        # vlc code error
        # AttributeError: 'NoneType' object has no attribute 'media_player_new'

- Install mpg123

        # real solution omg..
        # Try 
        sudo apt-get install mpg123 -y
        aplay -l

        #output
        card 0: audiocodec [audiocodec], device 0: SUNXI-CODEC sndcodec-0 []
        Subdevices: 1/1
        Subdevice #0: subdevice #0
        card 1: sndhdmi [sndhdmi], device 0: SUNXI-HDMIAUDIO sndhdmi-0 []
        Subdevices: 1/1
        Subdevice #0: subdevice #0
        card 2: Device [USB PnP Sound Device], device 0: USB Audio [USB Audio]
        Subdevices: 1/1
        Subdevice #0: subdevice #0

        #seem my usb sound card is 2
        mpg123 -a hw:2,0 *.mp3
        mpg123 -a hw:2,0 the_hero.mp3
                
---

##Extra note:

---
## Hardware datasheet
 
 - SSD1306 (OLED) 
 https://cdn-shop.adafruit.com/datasheets/SSD1306.pdf

---

## just other funny stuff I found

 - Nanopi m1 gpio control in goLang
 https://github.com/bluebanboom/M1HTTPCar/blob/master/gpio/gpio.go
 
---

### MQTT
 
 - open soucres mosquitto 
 https://mosquitto.org/2013/01/mosquitto-debian-repository/
 
 - a simple chinese mosquitto tutorial
 http://cheng-min-i-taiwan.blogspot.tw/2015/03/raspberry-pimqtt-android.html

 - hivemq 
 http://www.hivemq.com/blog/mqtt-client-library-paho-python

---

### electronic 

unfortanly I only have pnp transistor not npn, also I dont have any motor driver, so the car module.. no control unit to access it
also is stupid to use relay to control the ac motor. I leave the car part in next semester
 
- http://www.dummies.com/programming/electronics/components/electronics-components-use-a-transistor-as-a-switch/

- http://www.technologystudent.com/elec1/transis1.htm

---
author : BrokenPen
updated date : Saturday, 17. December 2016 04:47PM 
checked date : Monday, 02. January 2017 11:16PM 

 
        

