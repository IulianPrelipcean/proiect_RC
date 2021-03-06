#!/usr/bin/env python3

import socket
from Transmitator.pachet_t import *
from Transmitator.Tahoe import *


class Sender:
    HOST = '127.0.0.3'
    PORT_s = 65432
    PORT_r = 65431

    def __init__(self):
        # create a new UDP socket
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.s.bind((Sender.HOST, Sender.PORT_s))

    def connect(self):
        self.pachet = Pachet_Trimis(Sender.PORT_r)

        # algoritmul tahoe
        self.tahoe = Tahoe()

        # cream thead-urile
        self.receive_thread = threading.Thread(target=self.receive_function)
        self.send_thread = threading.Thread(target=self.send_function)

        # pornim thread-urile
        self.running = True
        self.receive_thread.start()
        self.send_thread.start()

    def close_connection(self):
        self.running = False
        self.receive_thread.join()
        self.send_thread.join()

    def receive_function(self):
        while self.running:
            r, _, _ = select.select([self.s], [], [], 1)
            time.sleep(2)
            if not r:
                print("receive nothing in Sender")
            else:
                data, address = self.s.recvfrom(1024)
                print("(Transmitator) Mesaj de confirmare ", str(data))

    def setMessage(self):
        self.message = self.pachet.returnare_pachet()
        return self.message

    def send_function(self):
        while self.running:
            try:
                cwnd = self.tahoe.getCwndSize()
                for index in range(1, cwnd):
                    message = self.setMessage()
                    self.s.sendto(bytes(message.encode('utf-8')), (Sender.HOST, Sender.PORT_r))
            except KeyboardInterrupt:
                self.running = False
                print("stopped from sender")
