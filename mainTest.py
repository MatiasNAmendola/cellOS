import curses
import time
import threading
from curses import panel
from screen import *


def main(stdscr):
	inp=Input()## Este objeto guarda el ultimo input recibido desde inputPanel
	maxY,maxX=stdscr.getmaxyx()
	inputWin = create_input(stdscr,'input')
	inputPanel=curses.panel.new_panel(inputWin)
	inputPanel.move(0,0)
	
	loop = threading.Thread(target=inputLoop, args=(inputPanel,inp))
	loop.daemon = True
	loop.start()

	win = create_display(stdscr,'Display')
	menuPanel=curses.panel.new_panel(win)
	while 1:
		lastInput=inp.get()
		win.clear()
		
		win.move(0, 1)
		win.addstr('Display')
		win.move(1, 1)

		menuPanel.show()
		inputPanel.show()
		menuPanel.move(3,0)

		#con wl() se agrega una linea
		wl(win,inp.get())
		wl(win,'\n')
		wl(win,inp.get())
		wl(win,inp.get())
		wl(win,inp.get())

		win.box()
		stdscr.refresh()
		curses.panel.update_panels()
		curses.doupdate()
		time.sleep(1)





if __name__ == '__main__':
	lastInput='primer input'
	curses.wrapper(main)

