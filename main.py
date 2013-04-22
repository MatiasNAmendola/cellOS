from proceso import *
from launcher import *
import time
import threading
from OS import *


def cycle(counter, os, launcher):
	quit = False
	while(~quit):
		os.getProcesses(launcher.getNextProcesses(counter))
		os.run()
		os.top()
		#many things
		print "I'm counting ", counter
		counter+=1
		time.sleep(1)
	
	

if __name__ == '__main__':
	#filePath = raw_input("Write file name for loading \n")
	launcher = Launcher("example.txt")
	counter = 0
	opS = OS()
	cycle (counter, opS, launcher)
	
	
