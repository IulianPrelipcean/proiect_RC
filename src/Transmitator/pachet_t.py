import threading
import select
import time
import struct
import sys

i = 0
nr_pachete = 0

class Pachet_Trimis:
    file_name = 'Transmitator/fisier.txt'

    def __init__(self, port):
        self.adresa = '127.0.0.3'
        self.port = port
        self.data = ''
        self.citire_date()

    def citire_date(self):
        with open(self.file_name, 'r') as stream:
            self.data = stream.read()
            # print(self.data)

    def preluare_date(self):
        global i
        ret_value = ''
        if (i + 2 <= len(self.data)):
            ret_value = self.data[i:i + 2]
        else:
            ret_value = "**"
        i += 2
        return ret_value

    def returnare_pachet(self):
        global nr_pachete

        nr_pachete += 1

        pachet = []
        pachet.append(self.port)
        pachet.append(nr_pachete)
        pachet.append(self.preluare_date())

        return str(pachet)
