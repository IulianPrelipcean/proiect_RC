#!/usr/bin/env python3

import socket
import threading
import select
import time
   
 
class Sender:
    HOST = '127.0.0.3'      
    PORT_s = 65432            
    PORT_r = 65431            
    
    

    
    def __init__(self):
        #create a new UDP socket
        addr_receiver=(Sender.HOST, Sender.PORT_r)
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.s.bind((Sender.HOST, Sender.PORT_s))
        

    def connect(self):
        self.receive_thread = threading.Thread(target=self.receive_function)
        self.send_thread = threading.Thread(target=self.send_function)
        self.running = True
        self.receive_thread.start()
        self.send_thread.start()

    def close_connection(self):
        self.running = False
        self.receive_thread.join()
        self.send_thread.join()


    def receive_function(self):
        contor = 0
        while self.running:
            r, _, _ = select.select([self.s], [], [], 1)
            time.sleep(1)
            if not r:
                contor = contor + 1
                print("receive in Sender")
            else:
                data, address = self.s.recvfrom(1024)
                print("S-a receptionat in sender class ", str(data), " de la ", address)
                print("Contor= ", contor)

    def send_function(self):
        while self.running:
            try:
                message = "data from sender class"
                #self.s.sendto(message.encode('utf-8'), (Sender.HOST, Sender.PORT))
                #self.s.sendto(bytes(message.encode('utf-8')), self.addr_receiver)
                self.s.sendto(bytes(message.encode('utf-8')), (Sender.HOST, Sender.PORT_r))
            except KeyboardInterrupt:
                self.running = False
                print("stoped from sender")

    


# send = Sender()
# send.connect()

