import os, sys
import tkinter as tk
import helpers
import user
import master

# User data
inventory = user.UserInventory()
# Master data
master_data = master.MasterData()

def print_inventory(text_widget):
    text_widget.delete("1.0", tk.END)  # Clear previous content
    
    # TODO: Work with the data in set_items and the helper
    # function to figure out the output data structure.
    set_items = helpers.sort_og_text_data(inventory.set_items)
    
    # Testing
    text_widget.insert(tk.END, "Test:\n")
    for line in master_data.set_items:
        text_widget.insert(tk.END, f"{line}\n\n")
    
    # text_widget.insert(tk.END, "Set items:\n")
    # for si in inventory.set_items:
    #     text_widget.insert(tk.END, f"{si}\n\n")
        
    # text_widget.insert(tk.END, "Unique items:\n")
    # for ui in inventory.set_items:
    #     text_widget.insert(tk.END, f"{ui}\n\n")
        
    # text_widget.insert(tk.END, "Other items:\n")
    # for oi in inventory.other_items:
    #     text_widget.insert(tk.END, f"{oi}\n\n")
        
def main():
    # Main program logic
    return 1

if __name__ == "__main__":
    SUCCESS, ERROR, COUNTER = 1, 0, 0

    # Tkinter UI setup
    root = tk.Tk()
    root.title("Diablo II item tracker")
    root.geometry("800x500")

    label = tk.Label(root, text="Diablo is cute <3", font=('Arial', 18))
    label.pack()

    # Frame to hold the Text widget and Scrollbar
    frame = tk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Text widget for displaying content
    text_widget = tk.Text(frame, wrap=tk.WORD, height=20, width=80)
    text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    print_inventory(text_widget)
    
    # Button to test printing out inventory
    # Pass the text_widget when setting the button's command
    button = tk.Button(root, text="Print items", command=lambda: print_inventory(text_widget))
    button.pack()

    # Scrollbar for the Text widget
    scrollbar = tk.Scrollbar(frame, command=text_widget.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Configure the Text widget to use the Scrollbar
    text_widget.config(yscrollcommand=scrollbar.set)

    # Start the Tkinter event loop
    root.mainloop()

    # Run Program
    print(f"Exit: {main()} (expected {SUCCESS})")