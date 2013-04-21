from proceso import *

class AddContact(Process):
	def __init__(self, attributes):
		super(AddContact, self).__init__(self, attributes)
		self.totalTime = 0
		self.contactName = attributes[4]
		self.contactNumber = attributes[5]
		
		
		
	