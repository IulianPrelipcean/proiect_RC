from tkinter import *
from Transmitator.transmitator import Sender

sender = Sender()

def onStart():
    print("Transmitator is ON")
    sender.connect()


def onStop():
    print("Transmitator is OFF")
    sender.close_connection()


def onCongestion():
    print("cong")


class UIObjects:

    def __init__(self):
        # initializeaza fereastra
        self.root = Tk()

        # titlu
        self.root.title("Transmitator")

        # creeaza obiecte
        self.startButton = Button(self.root, text="Start connection", command=onStart, padx=50, pady=50, fg="blue",bg="red")
        self.stopButton = Button(self.root, text="Stop connection", command=onStop, padx=50, pady=50, fg="blue", bg="red")

        # plaseaza obiecte in fereastra
        self.startButton.grid(row=0, column=0)
        self.stopButton.grid(row=0, column=1)

    def startInterface(self):
        self.root.mainloop()

def main():
    p1 = UIObjects()
    p1.startInterface()

#main()


