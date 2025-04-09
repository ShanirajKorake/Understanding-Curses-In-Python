import curses
from curses import wrapper
import time

def main(stdscr):
    
    stdscr.refresh()
    pad = curses.newpad(100, 100)
    for i in range(100):
        for j in range(26):
            char = chr(65 + j)
            pad.addstr(char)
    for i in range(50):
        stdscr.clear()
        stdscr.refresh()
        pad.refresh(0, 0, 5, i, 25, 25+i)
        time.sleep(.2)
    stdscr.getch()


wrapper(main)