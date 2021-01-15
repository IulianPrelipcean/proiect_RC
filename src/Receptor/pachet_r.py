import socket
import threading
import select
import time
import struct

from Transmitator.pachet_t import nr_pachete

class Pachet_Confirmare:

    def __init__(self, port):
        self.adresa = '127.0.0.3'
        self.port = port
        self.data = ''

    def preluare_date_confirmare(self, data):
        global nr_pachet
        nr_pachet = data[8]

    def returnare_pachet_confirmare(self):
        global nr_pachete

        nr_pachete+=1
        pachet = []
        pachet.append(self.port)
        pachet.append(nr_pachete)

        return str(pachet)
