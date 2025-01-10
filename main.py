import os, sys
import tkinter as tk
import helpers
import user

def on_click_print_inventory():
    print(user.set())
    print(user.unique())
    print(user.other())

def main():
    # Main program logic
    return 1

if __name__ == "__main__":
    SUCCESS, ERROR = 1, 0

    # Tkinter UI setup
    root = tk.Tk()
    root.title("Diablo II item tracker")
    root.geometry("800x500")

    label = tk.Label(root, text="Diablo is cute <3", font=('Arial', 18))
    label.pack()
    
    # Button to test printing out inventory
    button = tk.Button(root, text="Print items", command=on_click_print_inventory)
    button.pack()

    # Start the Tkinter event loop
    root.mainloop()
    
    # Run Program
    print(f"Exit: {main()} (expected {SUCCESS})")