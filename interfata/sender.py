#!/usr/bin/env python3

import socket

class Sender:
	HOST = '127.0.0.1'		# localhost
	PORT = 65432			# port (non--privileged port are > 1023 ) 0-65536

	def __init__(self):
		pass

	def connect(self):
		#create a new socket
		self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		#self.s.bind(Sender.HOST, Sender.PORT)
		self.s.bind('127.0.0.1', 65432)

	def startSend(self, message):
		self.s.sendto(message.encode('utf-8'), (Sender.HOST, Sender.PORT))


