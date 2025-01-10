import os, sys
import tkinter as tk
import helpers, user

def main():
    user_set_items = user.set()
    user_unique_items = user.unique()
    user_other_items = user.other()
    print(user_set_items)
    print(user_unique_items)
    print(user_other_items)
    
    return 1

def on_click():
    print(f"Exit: {main()} (expected {SUCCESS})")

if __name__ == "__main__":
    SUCCESS, ERROR = 1, 0

    # Tkinter UI setup
    root = tk.Tk()
    root.title("Simple UI")

    button = tk.Button(root, text="Run Program", command=on_click)
    button.pack()

    # Start the Tkinter event loop
    root.mainloop()