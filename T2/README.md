# T2: Text Formatting & Colors in curses

This tutorial explores **text attributes and colors** in `curses` to enhance terminal UI display.

## 📜 Code Breakdown

- `curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_RED)` → Defines a **color pair** (foreground: yellow, background: red).
- `stdcsr.addstr(y, x, "text", attr)` → Prints text at `(y, x)` position with an **attribute**.

### 🖍️ Text Attributes Used:
| Attribute | Description |
|-----------|-------------|
| `curses.A_NORMAL` | Normal text |
| `curses.A_STANDOUT` | Highlighted text |
| `curses.A_UNDERLINE` | Underlined text |
| `curses.A_REVERSE` | Swap foreground & background |
| `curses.A_BLINK` | Blinking text |
| `curses.A_DIM` | Dimmed text |
| `curses.A_BOLD` | Bold text |
| `curses.A_PROTECT` | Protected mode |
| `curses.A_INVIS` | Invisible text |
| `curses.A_ALTCHARSET` | Alternate character set |
| `curses.A_CHARTEXT` | Character text mask |
| `curses.color_pair(1)` | Uses defined color pair |

## 🎨 Output Behavior
✅ Displays various **text styles** in different lines.  
✅ Uses a **custom color pair** (yellow text on red background).  
✅ Waits for **user input** before exiting.

---

This tutorial introduces essential styling options for building **visually appealing terminal interfaces** in `curses`. 🚀

