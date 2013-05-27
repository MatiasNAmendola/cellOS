import curses
import time

class Screen:
	def __init__(self):
		self.lines=[]
	def get(self):
		return self.lines
	def addLine(self,text):
		self.lines.append(text)
	def addLines(self,lines):
		for line in lines:
			self.lines.append(line)
	def clear(self):
		del self.lines[:]

	def printProcess(self, proc, isRunning):
		output=''
		if proc != None:
			status = "Ready"
			if isRunning:
				status = "Running"
			output+= proc.id, proc.name, status, proc.date, proc.type, proc.priority, proc.elapsedTime, proc.totalTime
			return output


	def getTop(self,originalList):
		readyList = originalList[:]
		output = "ID,Name,Status, Date, Type, Priority, Elapsed Time, Total Time"
		if readyList != None:
			output+="\n"+self.getProcessLine(readyList[0], True)
			del readyList[0]
			for proc in readyList:
				output+="\n"+self.getProcessLine(proc, False)
		
		output+="\n"+"---------------------------"
		return output

	def getProcessLine(self, proc, isRunning):
		if proc != None:
			status = "Ready"
			if isRunning:
				status = "Running"
			out = str(proc.id)+" "+str(proc.name)+" "+ str(status)+" "+ str(proc.date)+" "+ str(proc.type)+" "+ str(proc.priority)+" "+ str(proc.elapsedTime)+" "+ str(proc.totalTime)
			return out
		return ""

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
	return output