<!-- for remarkable -->
<link rel="stylesheet" type="text/css" href="../../style.css">

<style type="text/css">
img {
  width: 50%;
}

img:.ev3-brick {
  width: 30%;
}
</style>
 
# ev3dev 
 
In this md file is talk about how to startup ev3dev.

## premise 

When you read this document, I assume you already done reading of

- course/operate-system/operate-system.md
- course/hardware/hardware.md

## prepare flash the microSD for ev3dev

option 1 : use ==refus== in ==Windows==


option 2 : use ==dd== utility in ==GNU/Linux==


### use refus in windows

1). download the ev3dev image for LEGO MINDSTORMS EV3 in www.ev3dev.org/downloads/

![](ev3dev/01-go-to-ev3dev-downloads.jpg) 

---
 
2). extract the zip file, assume you download store on desktop

![](ev3dev/03-extract-all-to-desktop.jpg) 

3). plug your mircoSD into comptuer, execute rufus.

![](ev3dev/09-ev3dev-rufus.PNG) 

4). Change Create a bootable disk using to DD image

![](ev3dev/10-ms-dos-to-dd-image.PNG) 

5). Select the ev3dev image by click the dvd-rom icon of left of DD image
![](ev3dev/11-select-the-img.PNG) 

6). Press start, wait until the green bar go 100%

![](ev3dev/12-press-start.PNG) 

---

### use dd utility in GNU/Linux

1). open terminal, except of click on `Acititcy` then type `terminal`, you also can press `ALT+F2` then type `gnome-terminal` to open `terminal`

2). copy ev3dev image url in www.ev3dev.org/downloads/, right click of Download for EV3, select Copy link address

3). use wget in terminal to download ev3dev image, to paste what you copy in clipboard press `CTRL+SHIFT+V` as same time

use `cd /tmp` switch to `/tmp` directory, so the download file won't keep it after boot
    
    cd /tmp 
    wget https://github.com/ev3dev/ev3dev/releases/download/ev3dev-jessie-2017-02-11/ev3dev-jessie-ev3-generic-2017-02-11.zip
    
4). after the download completed, need to `unzip` the file. 

    unzip ev3dev-jessie-ev3-generic-2017-02-11.zip
    cd ev3dev-jessie-ev3-generic-2017-02-11
    
5). plug your mircoSD into sd card slot or by mircoSD USB read to the computer, use `sudo fdisk -l` to find out which is the USB named.

    sudo fdisk -l
   
   in sd card slot case, you see `/dev/mmcblk0` as follow 
   
    ...
    Disk /dev/mmcblk0: 14.5 GiB, 15523119104 bytes, 30318592 sectors
    Units: sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    Disklabel type: dos
    Disk identifier: 0xfec402a8
    ...
    
   in mircoSD USB reader case, you see `/dev/sdx` as follow. (x is the letter the device asigned). If using linux live cd is will be `/dev/sdc`
   
    ...
    Disk /dev/sdd: 14.5 GiB, 15523119104 bytes, 30318592 sectors
    Units: sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    Disklabel type: dos
    Disk identifier: 0xfec402a8
    ...

6). flash the ev3dev image into the mircoSD card.

     dd if=ev3dev-jessie-ev3-generic-2017-02-11.img of=/dev/mmcblk0
     
7). now type `sudo fdisk -l` again, you see

    ...
    Device         Boot  Start      End  Sectors  Size Id Type
    /dev/mmcblk0p1        8192   106495    98304   48M  b W95 FAT32
    /dev/mmcblk0p2      106496 30318591 30212096 14.4G 83 Linux
    ...
    
---

## requirement

as your read as here, I though you already have these.

![](ev3-brick/05-requirement.jpg)

## attach mircoSD into EV3

1). The mircoSD card slot is locate as left side of EV3 brick

![](ev3-brick/07-mircosd-slot.jpg){:.ev3-brick}

2). insert mircoSD, the front side(logo) of mircoSD face up.

![](ev3-brick/08-mircosd-front-on-top.jpg){:.ev3-brick}

3). connect EV3 brick to computer though USB cable, then press the center key(OK) to boot up EV3 brick. You should see Linux like start up screen.

![](ev3-brick/10-attack-battery-usb-poewron.jpg){:.ev3-brick}

4). ouch, I forget attach the power cable.

 ![](ev3-brick/11-loading-ev3dev.jpg){:.ev3-brick}
 
5). ev3dev brick menu

 ![](ev3-brick/15-brick-gui-interface.jpg){:.ev3-brick}

## setup EV3 network

1). Enter Wireless and Networks

 ![](ev3-brick/18-select-wireless-and-networks.jpg){:.ev3-brick}

2). Enter All Network Connections

<!--
![](ev3-brick/19-wireless-and-networks.jpg) {:.ev3-brick}
-->

![](ev3-brick/20-select-all-network-connections.jpg){:.ev3-brick}

3). Enter Wired

![](ev3-brick/21-enter-wired.jpg){:.ev3-brick}

4). Enable Connect automatically

Default as disable

![](ev3-brick/22-select-connect-automatically.jpg){:.ev3-brick}

Now enabled

![](ev3-brick/23-auto-enabled.jpg){:.ev3-brick}

5). Enter IPv4

![](ev3-brick/25-select-ipv4.jpg){:.ev3-brick}

6). Enter Change...

![](ev3-brick/26-change-the-configure.jpg){:.ev3-brick}

7). Select Load Linux defaults

![](ev3-brick/28-local-linux-default.jpg){:.ev3-brick}

8). The Linux defaults config

![](ev3-brick/30-network-interface.jpg){:.ev3-brick}

9). RETURN, enter DNS

![](ev3-brick/33-select-dns.jpg){:.ev3-brick}

10). Select Add

![](ev3-brick/34-add-new-dns.jpg){:.ev3-brick}

11). OK, 
![](ev3-brick/35-enter-new-dns.jpg){:.ev3-brick}

12). Type in 8.8.8.8, then select OK

![](ev3-brick/36-enter-google-dns-8.8.8.8.jpg){:.ev3-brick}

13). Select Add

![](ev3-brick/37-select-add.jpg){:.ev3-brick}

<!--
14). Select ENET

![](ev3-brick/40-browsing-enet.jpg) 

15). ENET result

![](ev3-brick/41-enet-result.jpg) 
-->
## setup correct network ip in computer

1). open your terminal, type sudo ifconfig usb0 10.42.0.1

     sudo ifconfig usb0 10.42.0.1
     
troubleshooting, type sudo ifconfig to see usb0, usb1 exist or not

## ev3dev connecting to the Internet via usb

code/ev3dev-connecting-to-the-internet/via-usb.sh

1). 

create a empty file call via-usb.sh in code user code direcotry

    cd ~
    mkdir code
    cd code
    touch via-usb.sh
    
use geany IDE to edit via-usb.sh
    
    geany via-usb.sh

type the follow code in the file, CRTL+S to save the content, ALT+F4 to quit geany.

caution: if computer access Internet via WiFi, change eth0 to wlan0 in line 3.
    
    #!/bin/sh
    ifconfig usb0 10.42.0.1
    iptables --table nat --append POSTROUTING --out-interface eth0 -j MASQUERADE
    iptables --append FORWARD --in-interface usb0 -j ACCEPT
    echo 1 > /proc/sys/net/ipv4/ip_forward
    
gain execute pressmission to the via-usb.sh 

    chmod +x via-sub.sh
    
execute the via-usb.sh with priilage right

    sudo ./via-sub.sh

## ev3dev connecting to the Internet via WiFi adapter

code/ev3dev-connecting-to-the-internet/via-wifi-adapter

// TODO

1). attach WiFi adapter to ev3-brick USB port, using the ev3dev brick menu config wireless connection

## access ev3dev through ssh

## update ev3dev


