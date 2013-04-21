from proceso import *

class Message(Process):

    def __init__(self, attributes):
		super().__init__(attributes)
		self.isIncoming = True
		if int(attributes[2]) == 3:
			self.isIncoming = False
		self.phoneNumber = attributes[4]
		self.text = attributes[5]
		self.totalTime = getSendingTime(self)


    def getNumber(self):
        return self.number

    def getText(self):
        return self.text

	def getSendingTime(self):
		length = len(self.text)
		time = length*20
		time = (time/1000) + 1
		return time
