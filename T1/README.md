# T1: Basic curses Window

This script demonstrates a simple **curses** program that displays text in a terminal window.

## 📜 Code Breakdown

- `import curses` → Loads the **curses** library for terminal UI.
- `main(stdscr)` → The main function where `stdscr` represents the terminal screen.
- `stdscr.clear()` → Clears the screen before displaying content.
- `stdscr.addstr(10, 10, "hllow")` → Prints `"hllow"` at row **10**, column **10**.
- `stdscr.refresh()` → Updates the terminal screen to reflect changes.
- `stdscr.getch()` → Waits for a key press before exiting.
- `curses.wrapper(main)` → Initializes **curses**, runs `main()`, and restores the terminal on exit.

## 🖥️ Output Behavior
When you run the script, it will:
✅ Clear the screen  
✅ Display `"hllow"` at position (10,10)  
✅ Wait for a key press before closing  

This is the foundation for building more complex text-based UI applications! 🚀
