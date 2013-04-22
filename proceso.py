class Process:

	def __init__(self, attributes):
		self.id = 0
		self.name = attributes[0]
		self.date = int(attributes[1])
		self.type= int(attributes[2])
		self.priority = int(attributes[3])
		if self.type == 7:
			self.totalTime = 2
		else:
			self.totalTime = attributes[4]
		self.elapsedTime = 0
	
	def __init__(self, typeOfProcess,actualDate):
		self.id = 0
		
		#Hacer llamada
		if typeOfProcess == 1: 
			self.name = "Llamando desde display"
			self.date = actualDate
			self.type= typeOfProcess
			self.priority = 0
			self.elapsedTime = 1

		elif typeOfProcess == 3:
			self.name = "Enviando mensaje desde display"
			self.date = actualDate
			self.type= typeOfProcess
			self.priority = 1
			self.elapsedTime = 1

		elif typeOfProcess == 5:
			self.name = "Agregando contacto desde display"
			self.date = actualDate
			self.type= typeOfProcess
			self.priority = 3
			self.elapsedTime = 1


	def getName(self):
		return self.name
		
	def getTotalTime(self):
		return self.totalTime

	def getId(self):
		return self.id

	def getElapsedTime(self):
		return self.elapsedTime
	
	def getPriority(self):
		return self.priority
	
	def getDate(self):
		return self.date