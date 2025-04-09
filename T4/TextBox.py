import curses
from curses import wrapper
from curses.textpad import rectangle, Textbox
import time

def main(stdscr):
    
    win = curses.newwin(2,17,3,3)
    
    box = Textbox(win)
    
    rectangle(stdscr, 2, 2, 5, 20)
    stdscr.refresh()
    
    box.edit()
    text = box.gather().strip().replace("\n","")
    
    stdscr.addstr(10, 0, text)
    
    stdscr.getch()
wrapper(main)
