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
		string = string[:-2]
		attributes = string.split(";")
		nextProcess = Process(self.nextID, attributes)
		self.nextID += 1
		return nextProcess

	def getNextProcesses(self, count):
		processesToSend = []
		while self.processList and self.processList[0].getDate() == count:
			processesToSend.append(self.processList[0])
			del self.processList[0]
		return processesToSend
		