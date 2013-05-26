import time
import curses
from screen import *


def main(stdscr):
	curses.echo()
	curses.curs_set(0)
	curses.use_default_colors()
	sc = Screen(stdscr)
	sc.start()


if __name__ == '__main__':
	try:
		curses.wrapper(main)
	except KeyboardInterrupt:
		curses.endwin()
		pass