import curses

def main(stdscr):
    stdscr.clear()
    stdscr.addstr(10, 10 ,"hllow")
    stdscr.refresh()
    stdscr.getch()

curses.wrapper(main)

