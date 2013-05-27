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
	win.box()
	win.move(0, 1)
	win.addstr(title)
	win.move(1, 1)
	return win


def get_string(win):
	curses.echo()
	result = win.getstr()
	curses.echo()
	return result


def wl(screen,text):
	curr_y, curr_x = screen.getyx()
	screen.addstr(text)
	screen.clrtoeol()
	screen.move(curr_y+1, curr_x)

def writeMenu(name,options):
	output=[]
	st=''
	header='::::::'+name+'::::::'
	output.append(header)
	for key, v in options.items():
		st=key+" -> "+v
		output.append(st)
	output.append('::::::::::::::::::')
	strfinal=''
	for line in output:
		strfinal=strfinal+line+'\n'
	return strfinal