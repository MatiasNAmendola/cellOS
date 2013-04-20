#from Tkinter import *
#from proceso import Proceso
#from llamada import Llamada
#from mensaje import Mensaje
from launcher import Launcher
import time


if __name__ == '__main__':
	filePath = raw_input("Write file name for loading \n")
	launcher = Launcher(filePath)
	quit = False
	counter = 0
	while(~quit):
		#many things
		print "I'm counting ", counter
		counter += 1
		time.sleep(1)
