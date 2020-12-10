 
import socket
import threading
import select
import time
import struct


nr_pachet=0
class Pachet_Confirmare:

    def __init__(self, port):
        
        self.adresa = '127.0.0.3'
        self.port = port
        #self.nr_pachet = 0
        self.data = ''
        
    def preluare_date_confirmare(self, data):
        global nr_pachet
        # print("sunste bine", data)
        # print("dimnsiuen  ", len(data))
        # print("prima", str(data[8]))


        nr_pachet = data[8]

        #self.nr_pachet = data[]
        # for i in range(len(data)):
        #     print(i,  "= ", str(data[i]))

        #print(data[24:25])
        #print(data[29:30])
        #print(len(data))


        # global i
        # ret_value = ''
        # if (i+2 <= len(self.data)):
        #     ret_value = self.data[i:i+2]
        # else:
        #     ret_value = "##"
        # i+=2
        # return ret_value


    def returnare_pachet_confirmare(self):
        global nr_pachet
        pachet = []
        pachet.append(self.port)
        pachet.append(nr_pachet)


        return str(pachet);

