import os, sys
import tkinter as tk
import helpers
import user

def on_click_print_inventory():
    text_widget.delete("1.0", tk.END)  # Clear previous content
    text_widget.insert(tk.END, "Set items:\n")
    text_widget.insert(tk.END, f"{user.set()}\n\n")
    text_widget.insert(tk.END, "Unique items:\n")
    text_widget.insert(tk.END, f"{user.unique()}\n\n")
    text_widget.insert(tk.END, "Other items:\n")
    text_widget.insert(tk.END, f"{user.other()}\n")

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

    # Frame to hold the Text widget and Scrollbar
    frame = tk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Text widget for displaying content
    text_widget = tk.Text(frame, wrap=tk.WORD, height=20, width=80)
    text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Scrollbar for the Text widget
    scrollbar = tk.Scrollbar(frame, command=text_widget.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Configure the Text widget to use the Scrollbar
    text_widget.config(yscrollcommand=scrollbar.set)

    # Start the Tkinter event loop
    root.mainloop()

    # Run Program
    print(f"Exit: {main()} (expected {SUCCESS})")