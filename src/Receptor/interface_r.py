from tkinter import *

from Receptor.receptor import Receiver

receiver = Receiver()


def onStart():
    print("Receptor is ON")
    receiver.connect()


def onStop():
    print("Receptor is OFF")
    receiver.close_connection()


def onCongestion():
    print("Congestion activated")


def sendData():
    print("Receptor send data")


class UIObjects:

    def __init__(self):
        # initializeaza fereastra
        self.root = Tk()

        # titlu
        self.root.title("Receptor")

        # creeaza obiecte
        self.startButton = Button(self.root, text="Start connection", command=onStart, padx=50, pady=50, fg="blue", bg="green")
        self.stopButton = Button(self.root, text="Stop connection", command=onStop, padx=50, pady=50, fg="blue", bg="green")
        self.congestionButton = Button(self.root, text="Congestie", command=onCongestion, padx=50, pady=10, fg="blue", bg="green")

        # plaseaza obiecte in fereastra
        self.startButton.grid(row=0, column=0)
        self.stopButton.grid(row=0, column=1)
        self.congestionButton.grid(row=4, column=1)

    def startInterface(self):
        self.root.mainloop()

def main():
    p1 = UIObjects()
    p1.startInterface()

#main()
