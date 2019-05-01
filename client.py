#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 01:46:58 2019

@author: Yeahia Sarker

"""

import cv2
import struct
import pickle
import imutils
import sys
import time

class pybroadcast_clientside:
    def __init__(self):
        """ Initializing Socket Server..."""
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def client_server(self, host_ip, port):
        """ Fabricating Server Side...."""
        self.host_ip = host_ip
        self.port = port
        try:
            print("Waiting for client")
            self.server.connect((host_ip, port))
        except Exception:
            print("Bind Error!")
            print("The receiver couldn't connect")
            print("Please check the host ip address")
            self.server.close()
            sys.exit()
        self.server.listen(1)
        print("client side is ready. Waiting for connection.... " )
        print("Press ctrl + c to terminate the program")