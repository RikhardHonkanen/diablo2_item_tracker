import os, sys
import tkinter as tk
import helpers

def main(input):  # TODO: no base input, call functions for data
    print(input)
    return 1

def on_click():
    input = helpers.parse_file("data/output/set.txt")
    print(f"Exit: {main(input)} (expected {SUCCESS})")

if __name__ == "__main__":
    SUCCESS, ERROR = 1, 0

    # Tkinter UI setup
    root = tk.Tk()
    root.title("Simple UI")

    button = tk.Button(root, text="Run Program", command=on_click)
    button.pack()

    # Start the Tkinter event loop
    root.mainloop()