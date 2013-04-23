class Process:
	def __init__(self, attributes):
		if attributes[0]:
			self.id = 0
			self.name = attributes[1]
			self.date = int(attributes[2])
			self.type= int(attributes[3])
			self.priority = int(attributes[4])
			self.fromFile = attributes[0]
			if self.type == 7:
				self.totalTime = 2
			else:
				self.totalTime = attributes[5]
				self.elapsedTime = 0
	
		else:
			self.id = 0
			self.fromFile = False
			self.date = attributes[2]
			self.type= attributes[1]
			self.elapsedTime = 0
			self.totalTime = 1
			
			if attributes[1] == 1: 
				self.name = "Llamando desde display"
				self.priority = 0


			elif attributes[1] == 3:
				self.name = "Enviando mensaje desde display"
				self.priority = 1
		

			elif attributes[1] == 5:
				self.name = "Agregando contacto desde display"
				self.priority = 3


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