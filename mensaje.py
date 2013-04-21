from proceso import *

def getSendingTime(string):
	length = len(string)
	time = length*20
	time = (time/1000) + 1
	return time


class Message(Process):

    def __init__(self, attributes):
		Process.__init__(self, attributes)
		self.isIncoming = True
		if int(attributes[2]) == 3:
			self.isIncoming = False
		self.phoneNumber = attributes[4]
		self.text = attributes[5]
		self.totalTime = getSendingTime(self.text)


    def getNumber(self):
        return self.number

    def getText(self):
        return self.text



#test
#
#attributes = "recibir_mensajes;6;4;2;2277567;Hola".split(";")
#attributes2 = "enviar_mensajes;14;3;2;2277567;Como va?".split(";")
#msg = Message(attributes)
#msg2 = Message(attributes2)
#print msg.name
#print msg2.name