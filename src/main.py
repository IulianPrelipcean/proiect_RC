from Receptor.interface_r import UIObjects as Receptor
from Transmitator.interface_t import UIObjects as Transmitator

from threading import Thread

def receptorThread():
    r = Receptor()
    r.startInterface()


def transmitatorThread():
    t = Transmitator()
    t.startInterface()


if __name__ == '__main__':
    threadReceptor = Thread(target=receptorThread)
    threadTransmitator = Thread(target=transmitatorThread)

    threadReceptor.start()
    threadTransmitator.start()
