from scheduler import Scheduler
from dispatcher import Dispatcher
from proceso import Process

class OS:
	
	def __init__(self):
		self.scheduler = Scheduler()
		self.dispatcher = Dispatcher()
		self.time = 0
		self.runningProcess = None
		self.lastID = 0


	def getProcesses(self, nextProcessesList):
		if nextProcessesList != None:
			for proc in nextProcessesList:
				print "OS received process", proc.getName()
				proc.id= self.lastID
				self.lastID+=1
				self.scheduler.schedule(proc)

	def run(self):

		# Revisamos si hay proceso running
		if self.runningProcess != None:
			
			# Revisar si termino
			if int(self.runningProcess.elapsedTime) >= int(self.runningProcess.totalTime):

				print "entra if"

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

