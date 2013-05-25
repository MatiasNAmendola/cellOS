from scheduler import Scheduler
from dispatcher import Dispatcher
from proceso import Process
from display import *
import time
import threading

class OS:

	def __init__(self):
		self.scheduler = Scheduler()
		self.dispatcher = Dispatcher()
		self.time = 0
		self.runningProcess = None
		self.lastID = 0
		self.display = Display()
		self.inpThread = threading.Thread(target = self.inputThreadRun)
		self.inpThread.daemon = True
		self.inpThread.start()
		self.procFromDisplay = None
		self.actionFromDisplay = 0 #0 = nada, 1 = proceso nuevo, 2 = cortar proceso actual
		self.menu ="...::: ACTIONS :::...\n" + " (1) Hacer llamada\n" +" (2) Cortar llamada\n"+" (3) Enviar Mensaje\n"+" (4) Agregar Contacto\n"
		self.lock = Lock()


	def inputThreadRun(self):
		while True:
			option = int(raw_input("Enter an Option: "))
			if option != None:
				self.lock.acquire()
				if option == 1:
					number = raw_input("Enter a number: ")
					attributes = [False, 1, self.time, number]
					call = Call(attributes)
					self.actionFromDisplay = 1
					self.procFromDisplay = call
				elif option == 2:
					self.actionFromDisplay = 2
					self.procFromDisplay= -1
				elif option == 3:
					number = raw_input("Enter a number: ")
					message = raw_input("Enter your text: ")
					attributes = [False, 3,self.time,number,message]
					mess = Message(attributes)
					self.procFromDisplay = mess
					self.actionFromDisplay = 1
				elif option == 4:
					cName = raw_input("Enter contact name:")
					cNumber = raw_input("Enter contact number: ")
					attributes = [False, 5, self.time,cName,cNumber]
					nContact = NewContact(attributes)
					self.procFromDisplay = nContact
					self.actionFromDisplay = 1
				self.lock.release()
		
	def getProcesses(self, nextProcessesList):
		#Agregar procesos desde display
		#displayProc = self.display.displayMenu(time)
		#print self.procFromDisplay
		#
		self.lock.acquire()
		if (self.actionFromDisplay == 2 and self.runningProcess != None):
			if(self.runningProcess.type == 1 or self.runningProcess.type == 2):
				self.runningProcess.elapsedTime = int(self.runningProcess.totalTime) + 1
		elif (self.actionFromDisplay == 1)
			self.addProcessToList()
		
		self.procFromDisplay = None
		self.actionFromDisplay = 0 
		self.lock.release()

		#Revisar lista de todos los procesos que llegaron
		if nextProcessesList != None:
			for proc in nextProcessesList:
				print "OS received process", proc.getName()
				accepted = True
				if self.runningProcess != None:
					if self.runningProcess.type == 1 or self.runningProcess == 2:
						if proc.type ==2:
							self.display.getLostCall(proc)
							accepted = False
				if (accepted):
					proc.id= self.lastID
					self.lastID+=1
					self.scheduler.schedule(proc)
					
					
		
	def addProcessToList(self):
		
			
		elif displayProc.type == 1:
					if self.runningProcess != None:
						if self.runningProcess.type != 1 and self.runningProcess.type != 2: 
							nextProcessesList.append(displayProc)
					
					else:
						nextProcessesList.append(displayProc)
				else:
					nextProcessesList.append(displayProc)

		self.procFromDisplay = None

		displayProc = None

	def run(self):
		# Revisamos si hay proceso running
		if self.runningProcess != None:
			# Revisar si termino
			if int(self.runningProcess.elapsedTime) >= int(self.runningProcess.totalTime):
				self.runningProcess = None
				#Revisar si hay algun proceso en la cola ready
				if( ~self.scheduler.isEmpty() ):
					self.runningProcess = self.scheduler.dequeReady()
				else:
					return
			if self.scheduler.isEmpty()==False:
				# Revisar si existe algun proceso con mayor prioridad
				if self.runningProcess.getPriority() > self.scheduler.nextReady().getPriority():
					self.dispatcher.save(self.runningProcess)
					self.scheduler.schedule(self.runningProcess)
					self.runningProcess = self.scheduler.dequeReady()
					self.dispatcher.load(self.runningProcess)
			if self.runningProcess != None:
				self.runningProcess.elapsedTime+=1
				if self.runningProcess.type== 1:
					if self.runningProcess.fromFile == False:
						self.runningProcess.totalTime+=1
		else:
			if  self.scheduler.isEmpty() == False:
				self.runningProcess = self.scheduler.dequeReady()
				self.dispatcher.load(self.runningProcess)
				self.runningProcess.elapsedTime+=1

	def getReadyList(self):
		info = []
		info.append(self.runningProcess)
		info.extend(self.scheduler.readyList)
		return info

	def tick(self):
		self.time+=1
	
	def top(self):
		self.display.top(self.getReadyList())
	
	def displayCurrentProcess(self):
		self.display.displayCurrentProcess(self.runningProcess)

	def updateDisplay(self):
		output= self.menu + "\n" +self.display.getTop(self.getReadyList())
		print output
		self.displayCurrentProcess()

