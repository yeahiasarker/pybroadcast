#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 02:11:24 2018

@author: Yeahia Sarker
"""

import socket
import sys
import cv2
import pickle

class serverside:

    def __init__(self):
        """ Initializing Socket Server..."""
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def serve(self, host_ip, port):
        """ Fabricating Server Side...."""
        self.host_ip = host_ip
        self.port = port
        try:
            self.server.bind((host_ip, port))
        except Exception:
            print("Bind Error!")
            print("The receiver couldn't connect")
            print("Please check the host ip address")
            self.server.close()
            sys.exit()
        self.server.listen(1)
        print("Server side is ready. Waiting for connection.... " )
        print("Press ctrl + c to terminate the program")
        try:
            self.__base, addr = self.server.accept()
            print("Connection has been established")
            print('Got a connection from {}'.format(str(addr)))
        except Exception as e:
            print(e)
        except KeyboardInterrupt:
            self.server.close()
            print("Connection has been terminated")
            sys.exit()

    def send_data(self):
        while True:
            cap = cv2.VideoCapture(0) # open default camera
            ret,frame = cap.read()
            frame = cv2.medianBlur(frame,5) # blurring frames to reduce noise
            data = pickle.dumps(frame)
            self.__base.send(data)
            print("Sending frames.....")

videoserver = serverside()
videoserver.serve("local address",1111) # must assign the local addressS