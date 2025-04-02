import curses

def main(stdcsr):
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_RED)
    
    stdcsr.clear()
    stdcsr.addstr(1, 10, "hello World")
    stdcsr.addstr(2, 10, "NORMAL : hello World",curses.A_NORMAL)
    stdcsr.addstr(3, 10, "STANDOUT : hello World",curses.A_STANDOUT)
    stdcsr.addstr(4, 10, "UNDERLINE : hello World",curses.A_UNDERLINE)
    stdcsr.addstr(5, 10, "REVERSE : hello World",curses.A_REVERSE)
    stdcsr.addstr(6, 10, "BLINK : hello World",curses.A_BLINK)
    stdcsr.addstr(7, 10, "DIM : hello World",curses.A_DIM)
    stdcsr.addstr(8, 10, "BOLD : hello World",curses.A_BOLD)
    stdcsr.addstr(9, 10, "PROTECT : hello World",curses.A_PROTECT)
    stdcsr.addstr(10, 10, "INVIS : hello World",curses.A_INVIS)
    stdcsr.addstr(11, 10, "ALTCHARSET : hello World",curses.A_ALTCHARSET)
    stdcsr.addstr(12, 10, "CHARTEXT : hello World",curses.A_CHARTEXT)
    stdcsr.addstr(13, 10, "COLORPAIR : hello World",curses.color_pair(1))
    stdcsr.getch()
    pass

curses.wrapper(main)
