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

## attach mircoSD into EV3

## setup EV3 network

## setup coorect network ip in computer

## access ev3dev through ssh

## update ev3dev


