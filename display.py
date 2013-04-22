import os as operativeSystem
from proceso import *
from mensaje import *
from llamada import *
from agenda import *

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

	def displayCurrentProcess(self, proc):
		print "Screen:"
		if proc == None:
			print "No current process"
		elif proc.type == 1:
			print "OUTGOING CALL"
			print proc.getNumber()
			print "Duration:", proc.elapsedTime
		elif proc.type == 2:
			print "INCOMING CALL"
			print proc.getNumber()
			print "Duration:", proc.elapsedTime
		elif proc.type == 3:
			print "SENDING A MESSAGE"
			print proc.getNumber()
			print proc.getText()
		elif proc.type == 5:
			print "CONTACT ADDED"
			print proc.contactNumber
			print proc.contactName
		else:
			print "OTHER PROCESSES"