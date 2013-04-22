from proceso import *
from launcher import *
import time
import threading
from OS import *
import os as operativeSystem

def cycle(counter, os, launcher):
	quit = False
	while(~quit):
		os.getProcesses(launcher.getNextProcesses(counter))
		os.run()
		top(os.getReadyList())
		#many things
		print "I'm counting ", counter
		counter+=1
		time.sleep(1)
	
	
###################Metodos auxiliares################

def cls():
    operativeSystem.system(['clear','cls'][operativeSystem.name == 'nt'])

def printProcess(proc, isRunning):
	if proc != None:
		status = "Ready"
		if isRunning:
			status = "Running"
		print proc.id, proc.name, status, proc.date, proc.type, proc.priority, proc.elapsedTime, proc.totalTime


def top(originalList):
	readyList = originalList[:]
	cls()
	print "ID,Name,Status, Date, Type, Priority, Elapsed Time, Total Time"
	if readyList != None:
		printProcess(readyList[0], True)
		del readyList[0]
		for proc in readyList:
			printProcess(proc, False)
	print "---------------------------"


#####################################################










if __name__ == '__main__':
	#filePath = raw_input("Write file name for loading \n")
	launcher = Launcher("example.txt")
	counter = 0
	opS = OS()
	cycle (counter, opS, launcher)
	
	
