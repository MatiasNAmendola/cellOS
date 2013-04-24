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
		#print "...::: ACTIONS :::..."
		#print " (1) Hacer llamada"
		#print " (2) Cortar llamada"
		#print " (3) Enviar Mensaje"
		#print " (4) Agregar Contacto"
		option = int(raw_input("Enter an Option: "))

		if option != None:
			if option == 1:
				number = raw_input("Enter a number: ")
				attributes = [False, 1, actualDate, number]
				call = Call(attributes)
				return call

			elif option == 2:
				return -1

			elif option == 3:
				number = raw_input("Enter a number: ")
				message = raw_input("Enter your text: ")
				attributes = [False, 3,actualDate,number,message]
				mess = Message(attributes)
				return mess

			
			elif option == 4:
				cName = raw_input("Enter contact name:")
				cNumber = raw_input("Enter contact number: ")
				attributes = [False, 3, actualDate,cName,cNumber]
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
		for i in range(len(self.lostCalls)-1,-1,-1):
			print "***LOST CALL FROM ", self.lostCalls[i].call.getNumber(), "***"
			if self.lostCalls[i].counter == 0:
				del self.lostCalls[i]
			else:
				self.lostCalls[i].counter -=1

	def getProcessLine(self, proc, isRunning):
		if proc != None:
			status = "Ready"
			if isRunning:
				status = "Running"
			out = str(proc.id)+" "+str(proc.name)+" "+ str(status)+" "+ str(proc.date)+" "+ str(proc.type)+" "+ str(proc.priority)+" "+ str(proc.elapsedTime)+" "+ str(proc.totalTime)
			return out
		return ""

	
	def getTop(self,originalList):
		readyList = originalList[:]
		output = "ID,Name,Status, Date, Type, Priority, Elapsed Time, Total Time"
		if readyList != None:
			output+="\n"+self.getProcessLine(readyList[0], True)
			del readyList[0]
			for proc in readyList:
				output+="\n"+self.getProcessLine(proc, False)
		
		output+="\n"+"---------------------------"
		return output

	


		


		
