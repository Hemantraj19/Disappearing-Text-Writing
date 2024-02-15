# Disappearing Text Writing

This Python script creates a simple graphical user interface (GUI) using Tkinter for a "Disappearing Text Writing" application. The application allows users to type text, and after a certain period, the text disappears.

## Prerequisites
- Python installed on your system
- Tkinter library
- PIL (Python Imaging Library) for handling images

## Instructions
1. Ensure you have Python installed on your system.
2. Install required libraries if not already installed. You can install Tkinter using pip:
   ```
   pip install tk
   ```
   You can install PIL using:
   ```
   pip install pillow
   ```
3. Download the script and the required image file (`bg.png`) to the same directory.
4. Run the script using Python.

## Features
- The GUI is built using Tkinter, a standard GUI library for Python.
- Upon running the script, users will see a window titled "Disappearing Text Writing" with a background image (`bg.png`).
- Users can type text into the text entry field provided.
- After typing each key, a countdown timer starts from 5 seconds. If the user stops typing, the timer counts down to 0.
- When the timer reaches 0, the text entry field is cleared.
- Users can continue typing after the text field is cleared.

## Usage
- Run the script.
- Type text into the provided text entry field.
- The countdown timer starts after each keystroke.
- If you pause typing, the timer will continue to count down.
- After 5 seconds of inactivity, the text entry field will be cleared.

## Files
- `main.py`: Python script containing the GUI code.
- `bg.png`: Background image used in the GUI.

## Acknowledgments
- This script was created as a learning exercise in using Tkinter for GUI development in Python.
- The script demonstrates event handling and basic GUI layout techniques.
