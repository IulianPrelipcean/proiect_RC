#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'	# localhost
PORT = 65432		# port (non--privileged port are > 1023 ) 0-65536
MESSAGE = b"Hello, Iuli!"	# message to send

# create a new socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# socket.sendto(bytes, address)
	# send data to socket
s.sendto(MESSAGE, (HOST,PORT))
		
