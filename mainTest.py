import curses
import time
import threading
from curses import panel
from screen import *
from proceso import *
from launcher import *
from OS import *


def refresh(displayPanel,scr): #loop refresca el display cada 1 seg
	win=displayPanel.window()
	lines=scr.lines
	
	win.clear()
	win.move(1, 1)
	displayPanel.show()
	displayPanel.move(3,0)
	win.move(1,1)
	for l in lines:
		wl(win,l)
	win.move(0, 1)
	win.addstr('Ingrese \'q\' para salir.')
	win.refresh()
	curses.panel.update_panels()


def cycle(os,launcher,displayPanel,scr):
	counter=0
	time.sleep(1)
	while 1:
		os.getProcesses(launcher.getNextProcesses(counter))
		os.run()
		refresh(displayPanel,scr)
		counter+=1
		time.sleep(1)
		

def refreshInput(inp):
	inp.move(0, 1)
	inp.addstr('Input')
	inp.move(1,3)
	inp.clrtoeol()

def main(stdscr):
	curses.curs_set(0)
	scr=Screen()## Este objeto guarda las lineas a mostrar en el display
	maxY,maxX=stdscr.getmaxyx()
	inp = create_input(stdscr,'input')
	inputPanel=curses.panel.new_panel(inp)
	inputPanel.move(0,0)
	win = create_display(stdscr,'Display')
	displayPanel=curses.panel.new_panel(win)

	filePath = "example.txt"
	launcher = Launcher(filePath)
	opS = OS()
	loop = threading.Thread(target=cycle, args=(opS,launcher,displayPanel,scr))
	loop.daemon = True
	loop.start()
	while 1:
		curses.echo()
		inputPanel.show()
		refreshInput(inp)
		scr.clear()
		stringMenu=writeMenu('ACTIONS',{1:'Hacer llamada',2:'Cortar Llamada',3:'Enviar mensaje',4:'Agregar contacto',5:'Mandar Ubicacion',6:'Jugar',7:'Escuchar Musica' })
		scr.addLine(stringMenu)
		lastInput=inp.getstr()
		scr.addLine(lastInput)
		inp.move(1,3)
		inp.box()

		if lastInput=='q':
			break
		elif lastInput=='1':
			scr.clear()
			scr.addLine("Escriba un numero de telefono")
			lastInput=inp.getstr()
			##Aqui lanzar el proceso
			
		elif lastInput=='2':
			#Aqui cortar llamada
			scr.addLine("Llamada actual finalizada")
			
		elif lastInput=='3':
			scr.clear()
			scr.addLine("Escriba un numero de telefono de destino")
			lastInput=inp.getstr()
			refreshInput(inp)
			scr.addLine("Escriba el mensaje")
			lastInput=inp.getstr()
			#lanzar el mensaje
		elif lastInput=='4':
			scr.clear()
			scr.addLine("Escriba el nombre")
			lastInput=inp.getstr()
			refreshInput(inp)
			scr.addLine("Escriba el numero")
			lastInput=inp.getstr()

		elif lastInput=='5':
			scr.clear()
			scr.addLine("Escriba numero de telefono del destinatario")
			lastInput=inp.getstr()

		elif lastInput=='6':
			scr.clear()
			scr.addLine("Jugando Angry Birds")
			lastInput=inp.getstr()

		elif lastInput=='7':
			scr.clear()
			scr.addLine("Escuchando Musica")
			lastInput=inp.getstr()




			





if __name__ == '__main__':

	curses.wrapper(main)
	curses.curs_set(1)

