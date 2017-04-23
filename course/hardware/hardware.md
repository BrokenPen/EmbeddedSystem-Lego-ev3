# Hardware

In this section, I only mention about the hardware you may need it.

The Software/OS requirement part in the `software.md`.

## Computer
---
The standard computer will be fine,  whether a Desktop or Notebook.

### Copmuter OS

Choose the solution that come into your condition.

#### For the school computer running Windows OS 

##### Boot from USB

==The computer bios is not locked or you can boot computer from a USB device.==

To avoid of troubleshooting in Windows OS, such as install Ethernet Driver for Lego EV3, use putty(ssh) remote access Lego EV3(ev3dev), using WinSCP(scp)...

Please use a Linux Live USB, due to most school computer might have installed recovery card by the school computer department and also strictly ban student to install software/OS on the computer.

- A 4GB Usb Memory Stick will be fine for flash as a Linux Live USB,
- A 8GB Usb Memory Stick will be better than 4GB Usb Memtory Stick.
- A 8GB Usb Memory Stick with Wifi compent will be better than above.

The boot menu is always available at comptuer startup screen(the logo), most of the bios boot menu is at F12(keyboard). Prese F12 after you press the power button to boot up the computer to enter boot menu.

##### Use virtual machine

==The computer bios is locked or you can't boot comptuer from a USB device==

Download [VMware player][vmware], [Virtual box][virtualbox] install into USB memory strick also copy the binary installer into USB memory strick
Download GNU/Linux distro image.

#### For the school computer running Unix-Like OS

Your school is amazing!, go next section - [Lego EV3](#lego-ev3).

#### For student are require to take their Notebook to the class

Use [VMware player][vmware], [Virtual box][virtualbox] to run GNU/Linux System is fine.
Install GNU/Linux  on Notebook is the best! 


## Lego EV3
---

> here isn't recommend you to buy Lego EV3 but only recommend for who already have the Lego EV3

[Lego mindstorm EV3 (part 31313) 350USD][lego-ev3-31313]
[Rechargeable Battery (part 45501) 85USD][lego-ev3-45501]

## microSD card for Lego EV3

a microSD card is indeed to install ev3dev.

a quota from : http://www.ev3dev.org/docs/getting-started/
> A [microSD][microsd] or [microSDHC][microsdhc] card (2GB or larger). microSDXC is not supported on the EV3. All cards larger than 32GB will not work with the EV3!

If you don't have a microSD or microSDHC (2GB to 16GB), read the follow, otherwise skip it.

In the 3C market, the mircoSD card of 8GB or 16GB which have higher C/P than the 2GB/4GB mircoSD card, also better storage size for other Single Board Computer to install OS if you wanna try other SBC later on. 

If you don't have microSD card for Lego EV3, I recommend you buy 8GB or 16GB mircoSD\microSDHC card.

### microSD card reader

- a USB microSD card reader.
- a microSD to SD adapter, if the computer has standard SD card slot.

### Wifi dongle for Lego EV3

The Wifi dongle on Lego EV3 is an optional hardware for setup wireless connection between Computer and Lego EV3.

If you already can connect Lego EV3 through Wifi dongle, skip this section!

The Wifi dongle work on Lego EV3

- Edimax would be fine
- try what you have that is work and buy as you need

Some cheap Wifi dongle should avoid which don't work on Lego EV3.

- rtk8188us, the chip is often used in the China Brand cheap Wifi dongle under 3USD.
- 360 generation 3 Wifi dongle, which don't support Linux, Lego EV3(ev3dev) too.


<!-- ## Reference -->

[vmware]: https://www.vmware.com/products/player/playerpro-evaluation.html
[virtualbox]: https://www.virtualbox.org/wiki/Downloads
[lego-ev3-31313]: https://shop.lego.com/en-US/LEGO-MINDSTORMS-EV3-31313
[lego-ev3-45501]: https://shop.lego.com/en-US/EV3-Rechargeable-DC-Battery-45501

[microsd]: https://en.wikipedia.org/wiki/Secure_Digital#SD_.28SDSC.29
[microsdhc]: https://en.wikipedia.org/wiki/Secure_Digital#SDHC
