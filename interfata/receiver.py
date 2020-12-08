#!/usr/bin/env python3

import socket
import threading
import select
import time
   
 
class Receiver:
    HOST = '127.0.0.6'      
    PORT_s = 65432            
    PORT_r = 65431            
    
    
    
    def __init__(self):
        #create a new UDP socket
        #addr_sender=(Receiver.HOST, Receiver.PORT_s)
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.s.bind((Receiver.HOST, Receiver.PORT_r))
        
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
                print("receive in Receiver")
            else:
                data, address = self.s.recvfrom(1024)
                print("S-a receptionat in receiver class ", str(data), " de la ", address)
                print("data este", len(str(data)))
                print("Contor= ", contor)

    def setMessage(self):
        self.mess = "AAAAAAA _____ data from receiver"
        return self.mess


    def send_function(self):
        while self.running:
            try:
                message = self.setMessage()
                # message = "data from receiver class"
                # message = getMessage()
                #self.s.sendto(message.encode('utf-8'), (Sender.HOST, Sender.PORT))
                #self.s.sendto(bytes(message.encode('utf-8')), self.addr_sender)
                self.s.sendto(bytes(message.encode('utf-8')), (Receiver.HOST, Receiver.PORT_s))
            except KeyboardInterrupt:
                self.running = False
                print("stoped from receiver")

    


# receive = Receiver()
# receive.connect()
