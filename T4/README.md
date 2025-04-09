# T4: User Inputs & Textbox in curses

This tutorial covers **handling user input** and creating a **textbox UI** using `curses`, enabling more interactive terminal applications.

---

## 🧠 Concepts Covered
- Reading user **keystrokes in real-time**
- Moving characters based on input
- Creating **textbox input fields**
- Drawing rectangles for UI components

---

## 📁 Files
- `T4.py` → Real-time **key movement handler**
- `TextBox.py` → **Textbox interface** with `Textbox` & `rectangle`

---

## 🔹 T4.py: Realtime Arrow Key Input
Moves a character (`0`) around the screen using arrow keys.

### 🚀 Key Features:
- `stdscr.nodelay(True)` → Makes input **non-blocking**
- `stdscr.getkey()` → Reads the **pressed key**
- Arrow keys (`KEY_LEFT`, etc.) move the cursor
- `q` exits the program
- Adds a small text animation at the top

### 🔒 Boundary Control:
Clamps the coordinates within terminal size using:
```python
max_y, max_x = stdscr.getmaxyx()
x = max(0, min(x, max_x - 1))
y = max(0, min(y, max_y - 1))
```

---

## 🔸 TextBox.py: Text Input Field
Creates a **visual textbox** inside a rectangle where the user can type.

### 🧰 Tools Used:
| Function | Purpose |
|----------|---------|
| `curses.newwin()` | Creates a new window |
| `Textbox(win)` | Text input handler |
| `rectangle()` | Draws a border |
| `box.edit()` | Enables typing input |
| `box.gather()` | Collects the typed text |

### ✨ Output:
- User types inside the rectangle
- Text is printed at line 10 after pressing Enter

---

## 📌 Summary
| Feature | T4.py | TextBox.py |
|--------|-------|-------------|
| Real-time keys | ✅ | ❌ |
| Text input | ❌ | ✅ |
| Visual UI | Basic | Box UI |
| Exit key | `q` | Enter + any key |

This tutorial shows how to take **manual input** and process it dynamically using curses — a huge step toward building full TUI apps. 🚀

