#!/bin/sh
ifconfig usb0 10.42.0.1
iptables --table nat --append POSTROUTING --out-interface eth0 -j MASQUERADE
iptables --append FORWARD --in-interface usb0 -j ACCEPT
echo 1 > /proc/sys/net/ipv4/ip_forward
