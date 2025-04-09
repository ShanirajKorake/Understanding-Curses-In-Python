# T3: Windows and Pads in `curses`

This tutorial explores the **`curses` library's advanced screen manipulation** using **windows** and **pads** to enhance terminal UI control and structure.

---

## 📁 Files
- `T3.py` → Demonstrates a simple **window-based countdown**.
- `Pads.py` → Demonstrates **scrolling large content** using a `pad`.

---

## 🧱 What are `windows` and `pads` in curses?

| Concept | Description |
|--------|-------------|
| `Window` | A window in curses is a sub-section of the terminal screen. You can control its size, position, and content independently from the main screen. |
| `Pad` | A pad is like a window but can be **larger than the actual screen**. You can scroll through it to display content that doesn't fit the screen at once. |

---

## 🪟 T3.py: Window Countdown Example
### 🔍 Description:
- Creates a small **window** positioned at `(10, 10)` with size `(1, 20)`.
- Performs a **countdown from 10 to 0**, alternating text styles using `curses.A_NORMAL` and `curses.A_REVERSE`.
- Uses `stdscr` for main text and a separate window for the dynamic counter.

### 💡 Key Concepts:
- `curses.newwin(height, width, y, x)` → Creates a new window.
- `win.addstr(y, x, text, attr)` → Adds styled text to the window.
- `win.refresh()` → Refreshes only the window area.

### ✅ Behavior:
- Displays "hello world" on main screen.
- Updates the countdown in the small window every second.
- Waits for user input to exit.

---

## 📜 Pads.py: Scrollable Pad Example
### 🔍 Description:
- Creates a **100x100 pad**.
- Fills it with a repeating A–Z pattern.
- Simulates **horizontal scrolling** across the pad, displaying chunks using `pad.refresh()`.

### 💡 Key Concepts:
- `curses.newpad(rows, cols)` → Creates a pad larger than screen.
- `pad.addstr(text)` → Adds content to pad.
- `pad.refresh(pminrow, pmincol, sminrow, smincol, smaxrow, smaxcol)` → Controls which part of the pad is displayed on screen.

### ✅ Behavior:
- Simulates smooth scrolling of content.
- Great for large logs, tables, or text blocks.

---

## 🚀 Summary
This tutorial demonstrates:
- **Independent window areas** for structured UI design.
- **Pads** for navigating large off-screen content.

Together, they allow you to build more **dynamic and manageable terminal interfaces** with `curses`!

