import os as operativeSystem

class Display:
	
	def cls(self):
	    operativeSystem.system(['clear','cls'][operativeSystem.name == 'nt'])

	def printProcess(self, proc, isRunning):
		if proc != None:
			status = "Ready"
			if isRunning:
				status = "Running"
			print proc.id, proc.name, status, proc.date, proc.type, proc.priority, proc.elapsedTime, proc.totalTime


	def top(self, originalList):
		readyList = originalList[:]
		self.cls()
		print "ID,Name,Status, Date, Type, Priority, Elapsed Time, Total Time"
		if readyList != None:
			self.printProcess(readyList[0], True)
			del readyList[0]
			for proc in readyList:
				self.printProcess(proc, False)
		print "---------------------------"
