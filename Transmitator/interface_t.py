from tkinter import *
from transmitator import *
#from receiver import *

sender = Sender()

def onStart():
	print("onStart")
	sender.connect()

def onStop():
	print("stop")
	sender.close_connection()

def onCongestion():
	print("cong")

def sendData():
	print("send data")



class UIObjects:

	def __init__(self):

		# initializeaza fereastra
		self.root = Tk()

		self.root.title("Transmitator")
		# creeaza obiecte
		self.startButton = Button(self.root, text="Start connection", command=onStart, padx=50, pady=50, fg="blue", bg="red")
		self.stopButton = Button(self.root, text="Stop connection", command=onStop, padx=50, pady=50, fg="blue", bg="red")
		#self.congestionButton = Button(self.root, text="Congestie", command=onCongestion, padx=50, pady=10, fg="blue", bg="red")
		self.sendButton = Button(self.root, text="Send Data", command=sendData, padx=50, pady=10, fg="blue", bg="red")
		self.text1 = Label(self.root, text="Mesaj trimis")
		self.text2 = Label(self.root, text="Mesaj primit")
		self.messageToSend = Entry(self.root, width=20, borderwidth=5)
		self.messageToReceive = Entry(self.root, width=20, borderwidth=5)
		
		# plaseaza obiecte in fereastra
		self.startButton.grid(row=0, column=0)
		self.stopButton.grid(row=0, column=1)
		self.text1.grid(row=1, column=0)
		self.text2.grid(row=1, column=1)
		self.messageToSend.grid(row=2, column=0)
		self.messageToReceive.grid(row=2, column=1)
		self.sendButton.grid(row=3, column=0)
		#self.congestionButton.grid(row=4, column=0)

	def getMessageToSend(self):
		return self.messageToSend.get()

	def setMessageFromSender(self, message):
		self.messageToReceive.insert(0, message)

	def startInterface(self):
		self.root.mainloop()

def main():

	global flagSend
	p1 = UIObjects()

	p1.setMessageFromSender("")

	# if (flagSend == 1):
	# 	message = p1.getMessageToSend()
	# 	p1.setMessageFromSender(message)	
	# 	flagSend = 0;
	# else:
	# 	p1.setMessageFromSender("eroare")	
	# 	flagSend = 0;
	
	p1.startInterface()	


main()
