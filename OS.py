class OS:
	def getProcesses(self, nextProcessesList):
		if nextProcessesList != None:
			for proc in nextProcessesList:
				print "OS received process", proc.getName()