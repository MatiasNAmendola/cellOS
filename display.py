import os as operativeSystem
from proceso import *
from mensaje import *
from llamada import *
from agenda import *

class LostCall:
	def __init__(self, call):
		self.call = call
		self.counter = 2



class Display:
	

	
	def __init__(self):
		self.lostCalls = [] 
	
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
		print "ID,Name,Status, Date, Type, Priority, Elapsed Time, Total Time"
		if readyList != None:
			self.printProcess(readyList[0], True)
			del readyList[0]
			for proc in readyList:
				self.printProcess(proc, False)
		print "---------------------------"

	def displayMenu(self, actualDate):
		print "...::: ACTIONS :::..."
		print " (1) Hacer llamada"
		print " (2) Enviar Mensaje"
		print " (3) Agregar Contacto"
		option = raw_input("Enter an Option: ")

		if option != None:
			if option == 1:
				number = raw_input("Enter a number: ")
				attributes = [number, actualDate]
				call = Call(attributes)
				return call

			elif option == 2:
				number = raw_input("Enter a number: ")
				mesage = raw_input("Enter your text: ")
				attributes = [number, message, actualDate]
				mess = Message(attributes)
				return mess

			
			elif option == 3:
				cName = raw_input("Enter contact name:")
				cNumber = raw_input("Enter contact number: ")
				attributes = [cName,cNumber,actualDate]
				nContact = NewContact(attributes)
				return nContact

		

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
		print "-----------------"
		self.displayLostCalls()
		
	def getLostCall(self, call):
		self.lostCalls.append(LostCall(call))
		
	def displayLostCalls(self):
		for i in range(len(self.lostCalls)):
			print "***LOST CALL FROM ", self.lostCalls[i].call.getNumber(), "***"
			if self.lostCalls[i].counter == 0:
				del self.lostCalls[i]
			else:
				self.lostCalls[i].counter -=1
			
		


		
