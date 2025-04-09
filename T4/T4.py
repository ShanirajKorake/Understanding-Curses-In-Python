import curses
from curses import wrapper
import time

def main(stdscr):
    stdscr.nodelay(True)
    x, y = 0, 0
    x2 = 0

    while True:
        try:
            key = stdscr.getkey()
        except:
            key = None

        if key == "KEY_LEFT":
            x -= 1
        elif key == "KEY_RIGHT":
            x += 1
        elif key == "KEY_UP":
            y -= 1
        elif key == "KEY_DOWN":
            y += 1
        elif key == "q":
            break

        # Get terminal size and clamp coordinates
        max_y, max_x = stdscr.getmaxyx()
        x = max(0, min(x, max_x - 1))
        y = max(0, min(y, max_y - 1))

        stdscr.clear()
        x2 += 1

        if x2 // 100 < max_x:
            stdscr.addstr(0, x2 // 100, "hellow")

        stdscr.addstr(y, x, "0")
        stdscr.refresh()
        time.sleep(0.01)

wrapper(main)
