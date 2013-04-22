from proceso import Process

def loadFromFile(filePath):	
	lines = []
	io = open(filePath)
	for line in io:
		lines.append(line)
	io.close()
#	print lines
	return lines
		


class Launcher:
	"""Sends processes to OS"""
		
	def __init__(self, filePath):
		self.nextID = 0
		self.processList = []
		stringList = loadFromFile(filePath)
		for string in stringList:
			self.processList.append(self.stringToProcess(string))
		self.processList.sort(key=lambda proc: proc.getDate())
#		for proc in self.processList:
#			print proc.getName(), " ", proc.getDate()
		
	def stringToProcess(self, string):
		string = string[:-1]
		attributes = string.split(";")
		# Distincion de Procesos.
		if int(attributes[2]) == 1 or int(attributes[2]) == 2:
			nextProcess = Call(attributes)

		elif int(attributes[2]) == 3 or int(attributes[2]) == 4:
			nextProcess = Message(attributes) 

		elif int(attributes[2]) == 5:
			nextProcess = NewContact(attributes) 

		else:
			nextProcess = Process(attributes) 

		return nextProcess

	def getNextProcesses(self, count):
		processesToSend = []
		while self.processList and self.processList[0].getDate() == count:
			processesToSend.append(self.processList[0])
			del self.processList[0]
		return processesToSend
		