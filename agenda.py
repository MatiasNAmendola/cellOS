from proceso import *

def loadFromFile(filePath):	
	lines = []
	io = open(filePath)
	for line in io:
		lines.append(line)
	io.close()
	return lines

class NewContact(Process):
	def __init__(self, attributes):
		Process.__init__(self, attributes)
		self.totalTime = 0
		self.contactName = attributes[4]
		self.contactNumber = attributes[5]

class Contact:
	def __init__(self,name,number):
		self.name=name
		self.number=number
	def contactToString(self):
		print self.name+": "+self.number

class ContactBook:
	def __init__(self):
		self.book=[]
		self.loadContacts()

	def saveContact(self,name,number):

		io=open("contacts.txt", 'a')
		io.write(name+";"+number+"\n")
		io.close()
		self.loadContacts()
		

	def loadContacts(self):
		self.book=[]
		stringList = loadFromFile("contacts.txt")
		for string in stringList:
			attributes = string.split(";")
			newCont=Contact(attributes[0],attributes[1])
			self.book.append(newCont)
		self.currentContact=0

	def navContact(self,movedown):

		largo=len(self.book)
		if movedown==True:
			if largo<=0:
				return
			elif self.currentContact>=largo-1:
				self.currentContact=0
			else:
				self.currentContact+=1

		else:
			if largo<=0:
				return
			elif self.currentContact<=0:
				self.currentContact=largo-1
			else:
				self.currentContact-=1
		return self.book[self.currentContact]

	def remContact(self,contact):
		index =0
		for cont in self.book:
			

			if cont.name==contact.name:
				del self.book[index]
			index+=1
		io = open("contacts.txt", 'w')
		for cont in self.book:
			io.write(cont.name+";"+cont.number)