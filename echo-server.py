#!/usr/bin/env python3

import socket
import logging

HOST = '127.0.0.1'	# localhost
PORT = 65432		# port (non-privileged ports are > 1023) 0-65536

# socket.socket (family, typee, proto=0, fileno = None)
	#Create a new socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# socket.bind(address)
	#bind the socket to address
server_address = (HOST,PORT)
s.bind(server_address)

logging.basicConfig(filename="Server.log", format='%(asctime)s %(message)s', filemode='w', datefmt='%m/%d/%Y %I:%M:%S')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

while True:
	try:
	# socket.recvfrom(bufsize [,flags])
		# receive data from the socket. The return value is a pair (bytes, address) where bytes is a btes object representing the data received and address is the address of the socket sending the data.
		data, addr = s.recvfrom(1024)
		print("Message received from: ", addr)
		print("Server received: ", data.decode('utf-8'), "\n")

		logger.info(data.decode('utf-8'))

		send_data=data.decode('utf-8')
		s.sendto(send_data.encode('utf-8'),addr)
	except KeyboardInterrupt:
		print("\nServer went off")
		break

