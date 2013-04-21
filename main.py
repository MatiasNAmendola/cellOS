from Tkinter import *
from proceso import *
from launcher import *
from GUI import *
import time
import multiprocessing as mp
from OS import *


if __name__ == '__main__':
	filePath = raw_input("Write file name for loading \n")
	launcher = Launcher(filePath)
	counter = 0
	root = Tk()
	app = GUI(root)
	root.mainloop()
	os = OS()
	
	quit = False	
	while(~quit):
		os.getProcesses(launcher.getNextProcesses(counter))
		#many things
		print "I'm counting ", counter
		counter += 1
		time.sleep(.1)
