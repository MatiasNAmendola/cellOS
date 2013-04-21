from proceso import *


class Call(Process):


	def __init__(self, attributes):
		Process.__init__(self, attributes)
		self.isIncoming = True
		if int(attributes[2]) == 1:
			self.isIncoming = False
		self.phoneNumber = attributes[4]
		self.totalTime = attributes[5]
    
	def getNumber(self):
		return self.phoneNumber

	def getLength(self):
		return self.length

#test

#attributes = "hacer_llamada;41;1;0;2277567;10".split(";")
#attributes2 = "recibir_llamada;5;2;0;2277567;15".split(";")
#call = Call(attributes)
#call2 = Call(attributes2)
#print call.name
#print call2.name
