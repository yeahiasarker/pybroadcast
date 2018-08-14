# SafeVid
## Overview
SafeVid is a simple  encrypted full duplex video transmission service for local network. It uses symmetric advanced cryptographic algorithm to encrypt frames. It is safe cause encrypted frame is passed over network. Both the client and server use the same key. pbkdf2 is used to generate key from passwords. It is easy to use. 

Usage :
 - Assign you local address .
  For linux : Open up your terminal . Type "ifconfig" Find wlan0 for wifi network and eth0 for broadband servcies. Copy the inet address for ipv4 and  inet6 for ipv6.
  For windows : Open up your cmd. Type "ipconfig"  Find wlan0 for wifi network and eth0 for broadband servcies. Copy the inet address for ipv4 and  inet6 for ipv6.
- Assign a port number. The default is 1111
- Now run the program with python3 
