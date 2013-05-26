import curses
import time

class Input:
    def __init__(self):
        self.input=''
    def set(self,text):
        self.input=text
    def get(self):
        return self.input

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

def inputLoop(inputPanel,inp):
    win=inputPanel.window()
    while 1:
        win.move(0, 1)
        win.addstr('Input')
        win.move(1,3)
        win.clrtoeol()
        inp.set(get_string(win))
        win.move(1,3)
        win.box()

def wl(screen,text):
    curr_y, curr_x = screen.getyx()
    screen.addstr(text)
    screen.clrtoeol()
    screen.move(curr_y+1, curr_x)
