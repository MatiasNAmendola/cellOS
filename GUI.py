from Tkinter import *

class GUI:


	def __init__(self, master):
		self.displayString = "Nada que mostrar"
		frame = Frame(master)
		frame.pack()
		self.button1 = Button(frame, text="1", command= lambda: self. pressKey(1))
		self.button1.grid(row=1, column=0)
		self.button2 = Button(frame, text="2", command= lambda: self. pressKey(2))
		self.button2.grid(row=1, column=1)
		self.button3 = Button(frame, text="3", command= lambda: self. pressKey(3))
		self.button3.grid(row=1, column=2)
		self.button4 = Button(frame, text="4", command= lambda: self. pressKey(4))
		self.button4.grid(row=2, column=0)
		self.button5 = Button(frame, text="5", command= lambda: self. pressKey(5))
		self.button5.grid(row=2, column=1)
		self.button6 = Button(frame, text="6", command= lambda: self. pressKey(6))
		self.button6.grid(row=2, column=2)
		self.button7 = Button(frame, text="7", command= lambda: self. pressKey(7))
		self.button7.grid(row=3, column=0)
		self.button8 = Button(frame, text="8", command= lambda: self. pressKey(8))
		self.button8.grid(row=3, column=1)
		self.button9 = Button(frame, text="9", command= lambda: self. pressKey(9))
		self.button9.grid(row=3, column=2)
		self.button0 = Button(frame, text="0", command= lambda: self. pressKey(0))
		self.button0.grid(row=4, column=1)
		self.buttonCall = Button(frame, text="Call", fg='green', bg='green', command=self.pressCallButton)
		self.buttonCall.grid(row=5, column=0)
		self.buttonHang = Button(frame, text="Hang", fg='red', bg='red', command=self.pressHangButton)
		self.buttonHang.grid(row=5, column=2)
		self.buttonMessage = Button(frame, text="Message", command= self.writeMessage)
		self.buttonMessage.grid(row=5, column=1)
		self.screenLabel = Label(frame, text = self.displayString)
		self.screenLabel.grid(row=0)
	
	def pressKey(self, key):
		print "You've pressed key", key

	def pressCallButton(self):
		print "You're calling"

	def pressHangButton(self):
		print "You're hanging"

	def writeMessage(self):
		print "You're sending a message"
 