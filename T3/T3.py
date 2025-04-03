import curses
from curses import wrapper
import time

def main(stdscr):
    curses.curs_set(0)
    
    counter_win = curses.newwin(1,20, 10, 10)
    for i in range(10, -1, -1):
        counter_win.clear()
        if i % 2 == 0:
            counter_win.addstr(0, 0, f"Count : {i}", curses.A_NORMAL)
        else:
            counter_win.addstr(0, 0, f"Count : {i}",curses.A_REVERSE)
        
        counter_win.refresh()
        time.sleep(1)
    stdscr.getch()


wrapper(main)