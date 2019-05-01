#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 02:11:24 2018
@author: Yeahia Sarker
"""

from imutils.video import FileVideoStream
from imutils.video import FPS
import cv2
import imutils
import numpy as np
import pickle
import socket
import struct
import sys
import time


class pybroadcast_serverside:
    def __init__(self):
        """ Initializing Socket Server..."""
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def host_server(self, host_ip, port):
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
            sys.exit("Connection has been terminated")

    def send_data(self):

        starting_video_stream = FileVideoStream(0).start()
        time.sleep(1.0)
        fps_timer = FPS().start() # Starting frame per second counter
        while True:
            frame = starting_video_stream.read()
            frame = imutils.resize(frame, width=450)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame = np.dstack([frame, frame, frame])
            frame = cv2.medianBlur(frame,5) # blurring frames to reduce noise
            serialized_data = pickle.dumps(frame)
            new_serialized_data = struct.pack("H", len(serialized_data)) + serialized_data
            self.__base.send(new_serialized_data)
            print("Sending frames.....")
            cv2.imshow("[Pybroadcast] Server", frame)
            cv2.waitKey(1)
            fps_timer.update() # Updating frame per second counter

videoserver = pybroadcast_serverside()
videoserver.host_server("192.168.0.104",1111) # must assign the local addressS
