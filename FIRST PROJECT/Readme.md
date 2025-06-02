# Four in a Row (Connect Four) - Python CLI Game

A simple and interactive command-line (CLI) version of the classic Connect Four game for two players, written in Python.

---

## 📖 About The Project

**Four in a Row (Connect Four)** is a classic two-player connection game in which players take turns dropping colored discs into a seven-column, six-row vertically suspended grid. The pieces fall straight down, occupying the lowest available space within the column. The objective is to be the first to form a horizontal, vertical, or diagonal line of four of one's own discs.

This project is a **CLI-based Python implementation** of the game, designed for local two-player fun and learning. All interaction happens through the terminal or command prompt.

---

## 🛠️ Built With

- [Python 3](https://www.python.org/)

---

## ✨ Features

- **Command-Line Interface:** Play entirely in your terminal or command prompt.
- **User-Friendly Board Display:** Clear and readable board after every move.
- **Input Validation:** Handles invalid inputs and full columns gracefully.
- **Automatic Piece Placement:** Drops the piece to the lowest available spot in the selected column.
- **Win Detection:** Checks for four-in-a-row horizontally, vertically, and diagonally.
- **Draw Detection:** Detects and announces a tie if the board is full with no winner.
- **Replay Option:** Play multiple games in one session.
- **Graceful Exit:** Quit at any time with `quit` or `Ctrl+C`.
- **Clear Prompts:** Easy-to-understand instructions and error messages.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your system

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/four-in-a-row.git
   ```
2. **Navigate to the project directory:**
   ```bash
   cd four-in-a-row
   ```
3. **(Optional) Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. **No external dependencies needed!**

---

## 💡 Usage

Run the game with:

```bash
python four_in_a_row.py
```

Follow the on-screen prompts to play. All actions and game progress are displayed in your terminal window.

### Example Gameplay

```
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |
  1   2   3   4   5   6   7

Player1 X's turn.
Enter the column Number you want to place the Piece : (1-7) or 'quit' to exit:
```

---

## 🙏 Acknowledgements

- [othneildrew/Best-README-Template](https://github.com/othneildrew/Best-README-Template) for README inspiration
- Classic Connect Four game

---

**Enjoy playing Four in a Row on your command line!**

---

> **Note:**  
> Replace `https://github.com/yourusername/four-in-a-row.git` with your actual GitHub repository URL before publishing.
---
---