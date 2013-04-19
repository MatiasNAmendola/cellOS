from proceso import Process

class Scheduler:

	def __init__(self):
		self.readyList=[]
	

	def schedule(self,newProcess):
		self.readyList.append(newProcess)
		self.readyList.sort(key=Process.getPriority)

	def printReadyList(self):
		for p in self.readyList:
			print 'pid->',p.getId(),'\tpriority->',p.getPriority()
	def dequeReady(self):
		outbound=self.readyList.pop(0)
		return outbound