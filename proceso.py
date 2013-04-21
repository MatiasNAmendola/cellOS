''' def __init__(self, id, nombre, fecha, tipo, prioridad, opciones):
        self.id = id
        self.name = nombre
        self.totalTime = tiempo
		self.elapsedTime = 0
		self.priority = prioridad
		self.options = opciones
		self.type = tipo'''


class Process:

	def __init__(self, attributes):
		self.id = 0
		self.name = attributes[0]
		self.date = int(attributes[1])
		self.type= attributes[2]
		self.priority = attributes[3]
		self.totalTime = attributes[4]
		self.elapsedTime = 0
		

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