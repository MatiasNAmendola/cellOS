import curses
import time

class Screen:
	def __init__(self):
		self.lines=[]
	def get(self):
		return self.lines
	def addLine(self,text):
		self.lines.append(text)
	def clear(self):
		del self.lines[:]

def create_input(screen, title):
	maxY,maxX=screen.getmaxyx()
	win = curses.newwin(3, maxX,0,0)
	win.box()
	win.move(0, 1)
	win.addstr(title)
	win.move(1, 1)
	win.addstr('->')
	return win

def create_display(screen,title):
	maxY,maxX=screen.getmaxyx()
	win = curses.newwin(maxY-3, maxX,4,0)
	#win.box()
	win.move(0, 1)
	win.addstr(title)
	win.move(1, 1)
	return win


def wl(screen,text):

	curr_y, curr_x = screen.getyx()
	screen.addstr(curr_y,0,text)
	screen.clrtoeol()
	screen.move(curr_y+1, 0)

def writeMenu(name,options):
	output=[]
	st=''
	header='\n::::::'+name+'::::::'
	output.append(header)
	for k,v in options.items():
		st='('+str(k)+')'+' -> '+v
		output.append(st)
	output.append('::::::::::::::::::')
	strfinal=''
	for line in output:
		strfinal=strfinal+line+'\n'
	return strfinal