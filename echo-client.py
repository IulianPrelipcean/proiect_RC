#!/usr/bin/env python3

import socket
import logging

HOST = '127.0.0.1'		# localhost
PORT = 65432			# port (non--privileged port are > 1023 ) 0-65536
	
# create a new socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = (HOST,PORT)

logging.basicConfig(filename="Client.log", format='%(asctime)s %(message)s', filemode='w', datefmt='%m/%d/%Y %I:%M:%S')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

while True:
	try:
		send_data = input ("Client send: ")
		logger.info(send_data)
		s.sendto(send_data.encode('utf-8'), server_address)


		data, addr = s.recvfrom(1024)
		print ("Message received on server: ", data.decode('utf-8'), "\n")
	except KeyboardInterrupt:
		print("\nClient went off")
		break

s.close()
	
