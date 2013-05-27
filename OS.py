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
		self.procFromDisplay = None
		self.actionFromDisplay = 0 #0 = nada, 1 = proceso nuevo, 2 = cortar proceso actual
		self.menu ="...::: ACTIONS :::...\n" + " (1) Hacer llamada\n" +" (2) Cortar llamada\n"+" (3) Enviar Mensaje\n"+" (4) Agregar Contacto\n"
		self.lock = threading.Lock()
		self.nextProcessesList = []

	def getProcesses(self, nextProcessesList):
		self.nextProcessesList = []
		self.lock.acquire()
		if (self.actionFromDisplay == 2 and self.runningProcess != None):
			if(self.runningProcess.type == 1 or self.runningProcess.type == 2):
				self.runningProcess.elapsedTime = int(self.runningProcess.totalTime) + 1
		elif (self.actionFromDisplay == 1):
			self.addProcessToList()
		
		self.procFromDisplay = None
		self.actionFromDisplay = 0 
		self.lock.release()

		#Revisar lista de todos los procesos que llegaron
		if self.nextProcessesList != None:
			for proc in self.nextProcessesList:
				#print "OS received process", proc.getName()
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
		if not (self.procFromDisplay == 1 and self.runningProcess != None and (self.runningProcess.type == 1 or self.runningProcess.type == 2)):
			self.nextProcessesList.append(self.procFromDisplay)


	def run(self):
		# Revisamos si hay proceso running
		if self.runningProcess != None:
			# Revisar si termino
			if int(self.runningProcess.elapsedTime) >= int(self.runningProcess.totalTime):
				self.runningProcess = None
				#Revisar si hay algun proceso en la cola ready
				if not ( self.scheduler.isEmpty() ):
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

