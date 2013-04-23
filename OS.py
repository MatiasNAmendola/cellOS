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

	def inputThreadRun(self):
		while True:
		
		
	def getProcesses(self, nextProcessesList):
		#Agregar procesos desde display
		self.display.cls()
		displayProc = self.display.displayMenu(time)
		if(displayProc != None):
		   nextProcessesList.append(displayProc)

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

