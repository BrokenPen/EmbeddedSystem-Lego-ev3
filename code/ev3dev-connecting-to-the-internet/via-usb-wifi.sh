#!/bin/sh
ifconfig eth0 10.42.0.1
iptables --table nat --append POSTROUTING --out-interface wlan0 -j MASQUERADE
iptables --append FORWARD --in-interface usb0 -j ACCEPT
echo 1 > /proc/sys/net/ipv4/ip_forward
