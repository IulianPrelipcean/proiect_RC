
import threading
import select
import time
import struct
import sys 

i=0
nr_pachet=0
class Pachet_Trimis:
    file_name = 'fisier.txt'

    def __init__(self, port):
        self.adresa = '127.0.0.3'
        self.port = port
        self.data = ''
        self.citire_date()

    def citire_date(self):
        with open(self.file_name, 'r') as stream:
            self.data = stream.read()
            #print(self.data)

    def preluare_date(self):
        global i
        ret_value = ''
        if (i+2 <= len(self.data)):
            ret_value = self.data[i:i+2]
        else:
            ret_value = "**"
        i+=2
        return ret_value

    def returnare_pachet(self):
        global nr_pachet
        if(nr_pachet>65530):
            nr_pachet = 0
        else:
            nr_pachet+=1

        #self.nr_p+=1
        # pachet = bytearray()
        # pachet.extend(struct.pack('!H', self.port))
        # pachet.extend(struct.pack('!H', nr_pachet))
        # #pachet.extend(struct.pack('!H', self.nr_p))
        # pachet.extend(bytearray(self.preluare_date(), 'utf-8'))
        # #print("aici este sizeof", sys.getsizeof(pachet))
        # #print("aici este len", len(pachet))
        # print("de aici", pachet)
        #return str(pachet)

        #var 2
        pachet = []
        pachet.append(self.port)
        pachet.append(nr_pachet)
        pachet.append(self.preluare_date())

        return str(pachet);

        
