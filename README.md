# Pybroadcast
![alt next](https://github.com/goyeahia/pybroadcast/blob/master/pybraodcast.png)
## Overview
Pybroadcast is a simple  encrypted full duplex video transmission service for local network. It uses symmetric advanced cryptographic algorithm to encrypt frames. It is safe cause encrypted frame is passed over network. Both the client and server use the same key. pbkdf2 is used to generate key from passwords. It is easy to use. 

## Features
- It is a cross platform module
- Easy to use

## Installation
Extract files from the archive, open a shell/console in that directory and let Distutils do the rest

``` 
python setup.py install
```

## Usage :
 - Assign you local address .
  For linux : Open up your terminal . Type "ifconfig" Find wlan0 for wifi network and eth0 for broadband servcies. Copy the inet address for ipv4 and  inet6 for ipv6.
  For windows : Open up your cmd. Type "ipconfig"  Find wlan0 for wifi network and eth0 for broadband servcies. Copy the inet address for ipv4 and  inet6 for ipv6.
- Assign a port number. The default is 1111
- Now run the program with python3 

## Example
Please look in the GIT Repository. There is an example directory where you can find a simple terminal and more. 

## References
- Python : https://www.python.org/
- Opencv : https://pypi.org/project/opencv-python/
