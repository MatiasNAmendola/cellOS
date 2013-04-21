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
				proc.id= lastID
				lastID+=1
				scheduler.schedule(proc)

	def run(self):

		# Revisamos si hay proceso running
		if runningProcess != None:
			
			# Revisar si termino
			if runningProcess.elapsedTime == runningProcess.totalTime:
				runningProcess = None
				#Revisar si hay algun proceso en la cola ready
				if( ~scheduler.isEmpty() ):
					runningProcess = scheduler.dequeReady()
				else:
					return

			# Revisar si existe algun proceso con mayor prioridad
			if runningProcess.getPriority() > scheduler.nextReady().getPriority():
				dispatcher.save(runningProcess)
				scheduler.schedule(runningProcess)
				runningProcess = scheduler.dequeReady()
				dispatcher.load(runningProcess)

			runningProcess.elapsedTime+=1


	def getReadyList(self):
		info = []
		info.append(runningProcess)
		info.extend(scheduler.readyList)

		return info


	def tick(self):
		self.time+=1

