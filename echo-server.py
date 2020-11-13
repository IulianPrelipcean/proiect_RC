#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'	# localhost
PORT = 65432		# port (non-privileged ports are > 1023) 0-65536

# socket.socket (family, typee, proto=0, fileno = None)
	#Create a new socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# socket.bind(address)
	#bind the socket to address
s.bind((HOST,PORT))

while True:
	# socket.recvfrom(bufsize [,flags])
		# receive data from the socket. The return value is a pair (bytes, address) where bytes is a btes object representing the data received and address is the address of the socket sending the data.
	data, addr = s.recvfrom(1)
	print("received message: %s" %data)
