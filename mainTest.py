import curses
import time
import threading
from curses import panel
from screen import *

def refresh(displayPanel,scr): #loop refresca el display cada 1 seg
	win=displayPanel.window()
	lines=scr.lines
	while 1:

		win.clear()
		
		win.move(1, 1)
		displayPanel.show()
		displayPanel.move(3,0)
		win.move(1,1)
		for l in lines:
			wl(win,l)

		#win.box()
		win.move(0, 1)
		win.addstr('')
		win.refresh()
		curses.panel.update_panels()
		time.sleep(1)

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
		principal={1:'Menu1',2:'Menu2',3:'Menu3',9: 'Salir' }
		stringMenu=writeMenu('MENU PRINCIPAL',principal)
		scr.addLine(stringMenu)
		lastInput=inp.getstr()
		scr.addLine(lastInput)
		inp.move(1,3)
		inp.box()
		if lastInput=='quit':
			break





if __name__ == '__main__':

	curses.wrapper(main)
	curses.curs_set(1)

