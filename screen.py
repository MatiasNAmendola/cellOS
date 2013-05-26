import curses
import time

class Screen:
	def __init__(self, screen):
		self.screen=screen
		self.height, self.width = self.screen.getmaxyx()
		self.screen.nodelay(1)
		self.screen.keypad(1)

	def __exit__(self,screen):
		self.screen.keypad(0)

	def drawHeader(self,text):
		text=text+'\n\n'
		self.screen.clear()
		self.screen.addstr(1, 1, text)
		self.screen.refresh()

	def wl(self,text):
		screen=self.screen
		curr_y, curr_x = screen.getyx()
		screen.addstr(curr_y, curr_x ,text)
		screen.clrtoeol()
		screen.move(curr_y+1, curr_x)
		self.screen.refresh()

	def start(self):
		while 1:
			key = self.screen.getch()
			if key == ord('q'): break
			self.drawHeader("TITULO DEL MENU")
			self.wl("Linea1")
			self.wl("Linea2")
			time.sleep(1)