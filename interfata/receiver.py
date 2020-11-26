#!/usr/bin/env python3

import socket
import sys

class Receiver:
	HOST = '127.0.0.1'		# localhost
	PORT = 65432			# port (non--privileged port are > 1023 ) 0-65536

	def __init__(self):
		pass

	def connect(self):
		#create a new socket
		self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		

	def startReceive(self):
		while True:
			data, addr = self.s.recvfrom(1024)
			print("Message received from: ", addr)
			print("Message received: ", data.decode('utf-8'), "\n")
			break;
			
	def closeReceiver(self):
		self.s.close()


rev = Receiver()
rev.connect()
rev.startReceive()
rev.closeReceiver()

