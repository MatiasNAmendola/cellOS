from Tkinter import *
from proceso import *
from launcher import *
from GUI import *
import time
import threading
from OS import *


def cycle(counter, os, launcher):
	quit = False
	while(~quit):
		os.getProcesses(launcher.getNextProcesses(counter))
		#many things
		print "I'm counting ", counter
		time.sleep(1)
		counter+=1



if __name__ == '__main__':
	filePath = raw_input("Write file name for loading \n")
	launcher = Launcher(filePath)
	counter = 0
	root = Tk()
	app = GUI(root)
	os = OS()
	quit = False	
	cycleThread = threading.Thread(None, target= cycle, args= (counter, os, launcher))
	cycleThread.setDaemon(True)
	cycleThread.start()
	root.mainloop()
