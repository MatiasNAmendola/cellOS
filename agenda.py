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

class ContactBook:
	def __init__(self):
		self.book=[]
		#Leer desde archivo


	def saveContact(self,name,number):

		io=open("contacts.txt", 'a')
		io.write("\n"+name+";"+number)
		io.close()
		self.loadContacts()


	def loadContacts(self):
		self.book=[]
		stringList = loadFromFile("contacts.txt")
		for string in stringList:
			attributes = string.split(";")
			newCont=Contact(attributes[0],attributes[1])
			self.book.append(newCont)


			