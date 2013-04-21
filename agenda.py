from proceso import *

class NewContact(Process):
	def __init__(self, attributes):
		Process.__init__(self, attributes)
		self.totalTime = 0
		self.contactName = attributes[4]
		self.contactNumber = attributes[5]
		
		
		
	