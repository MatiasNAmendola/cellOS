import curses
import time
import threading
from curses import panel
from screen import *


def main(stdscr):
	curses.curs_set(0)
	scr=Screen()## Este objeto guarda las lineas a mostrar en el display
	maxY,maxX=stdscr.getmaxyx()
	inp = create_input(stdscr,'input')
	inputPanel=curses.panel.new_panel(inp)
	inputPanel.move(0,0)
	win = create_display(stdscr,'Display')
	displayPanel=curses.panel.new_panel(win)
	loop = threading.Thread(target=refresh, args=(displayPanel,scr))
	loop.daemon = True
	loop.start()
	while 1:
		curses.echo()
		inputPanel.show()
		inp.move(0, 1)
		inp.addstr('Input')
		inp.move(1,3)
		inp.clrtoeol()
		lastInput=inp.getstr()
		scr.addLine(lastInput)
		inp.move(1,3)
		inp.box()
		if lastInput=='quit':
			break





if __name__ == '__main__':

	curses.wrapper(main)
	curses.curs_set(1)

