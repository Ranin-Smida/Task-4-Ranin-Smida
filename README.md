# General Knowledge Quiz (CustomTkinter)

A small general-knowledge quiz desktop app built with Python and CustomTkinter. It presents a randomized set of questions, accepts typed answers (press Enter to submit), and tracks the user's score.

**Features**
- **Simple UI:** Uses `customtkinter` for a modern dark-themed GUI.
- **Shuffled Questions:** Questions are randomized each run.
- **Keyboard Support:** Press `Enter` to submit an answer.
- **Score Tracking:** Shows current and final score when the quiz ends.

**Requirements**
- Python 3.8 or newer
- Dependencies listed in `requirements.txt` (install with pip)

**Installation**
1. Clone the repository:

   git clone https://github.com/Ranin-Smida/Task-4-Ranin-Smida.git
   cd Task-4-Ranin-Smida

2. (Optional) Create and activate a virtual environment:

   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS / Linux
   source .venv/bin/activate

3. Install dependencies:

```bash
pip install -r requirements.txt
```

**Usage**
1. Run the application:

```bash
python main.py
```

2. Type your answer into the input field and press `Enter` or click **Submit Answer**.
3. Click **Reset Quiz** to reshuffle questions and start over.

**File Overview**
- `main.py` — main application script containing the quiz logic and GUI.
- `requirements.txt` — Python dependencies required to run the app.
- `README.md` — this file.

**Customization**
- Edit the `questions` list in `main.py` to add or modify quiz questions and accepted answers.
- UI colors and fonts are defined near the top of `main.py` as constants (`BG_COLOR`, `PANEL_COLOR`, `PRIMARY_COLOR`, etc.).

**Contributing**
Pull requests and issue reports are welcome. Please include minimal reproduction steps for bugs and keep changes focused.

**License & Author**
This repository was prepared by Ranin Smida. Include a license file if you want to specify reuse terms.
# Smart Expense Tracker

A desktop expense tracker built with CustomTkinter. Add expenses, set a budget,
see remaining budget, and review history in a simple GUI.

## Requirements

- Python 3.8+
- `customtkinter`

## Install

Create a virtual environment on Windows and install the dependency:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

## Features

- Add expenses with category selection
- Set and track a budget
- View total spent and remaining budget
- Clear all expenses with confirmation
- Reset the input fields

## Files

- `main.py` - expense tracker application
- `requirements.txt` - Python dependency list
