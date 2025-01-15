import os, sys
import tkinter as tk
import helpers
import user
import master

# User data
inventory = user.UserInventory()
# Master data
master_data = master.MasterData()

def validate_and_add_item(item, category):
    """Validate the item against MasterData and add to UserInventory if valid."""
    if item in master_data.set_items.keys():
        if category == "set_items":
            inventory.set_items.add(item)
        # elif category == "unique_items":
        #     inventory.unique_items.add(item)
        # TODO: Add logic for other categories if necessary
        return True
    else:
        return False

def add_item_callback(entry, category, output_label):
    """Callback for adding items to the inventory."""
    item = entry.get().strip()
    if validate_and_add_item(item, category):
        output_label.config(text=f"Item '{item}' successfully added to {category}!")
    else:
        output_label.config(text=f"Invalid item: '{item}'. Not found in MasterData.")
    entry.delete(0, tk.END)

def print_inventory(text_widget):
    text_widget.delete("1.0", tk.END)  # Clear previous content

    text_widget.insert(tk.END, "Set items:\n")
    for si in inventory.set_items:
        text_widget.insert(tk.END, f"{si}\n")

    text_widget.insert(tk.END, "\nUnique items:\n")
    for ui in inventory.unique_items:
        text_widget.insert(tk.END, f"{ui}\n")

    # TODO: Add display logic for other categories if needed

if __name__ == "__main__":
    for value in master_data.set_items.keys():
        print(value)
    # print(master_data.unique_items)
    exit()
    # Tkinter UI setup
    root = tk.Tk()
    root.title("Diablo II Item Tracker")
    root.geometry("800x600")

    label = tk.Label(root, text="Diablo is cute <3", font=('Arial', 18))
    label.pack()

    # Frame for inputs and buttons
    input_frame = tk.Frame(root)
    input_frame.pack(pady=10)

    # Entry and Button for Set Items
    set_label = tk.Label(input_frame, text="Add Set Item:")
    set_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
    set_entry = tk.Entry(input_frame, width=30)
    set_entry.grid(row=0, column=1, padx=5, pady=5)
    set_add_button = tk.Button(input_frame, text="Add", 
                               command=lambda: add_item_callback(set_entry, "set_items", message_label))
    set_add_button.grid(row=0, column=2, padx=5, pady=5)

    # Entry and Button for Unique Items
    unique_label = tk.Label(input_frame, text="Add Unique Item:")
    unique_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
    unique_entry = tk.Entry(input_frame, width=30)
    unique_entry.grid(row=1, column=1, padx=5, pady=5)
    unique_add_button = tk.Button(input_frame, text="Add", 
                                  command=lambda: add_item_callback(unique_entry, "unique_items", message_label))
    unique_add_button.grid(row=1, column=2, padx=5, pady=5)

    # Label for messages
    message_label = tk.Label(root, text="", fg="green")
    message_label.pack()

    # Frame to hold the Text widget and Scrollbar
    frame = tk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Text widget for displaying content
    text_widget = tk.Text(frame, wrap=tk.WORD, height=20, width=80)
    text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    print_inventory(text_widget)

    # Scrollbar for the Text widget
    scrollbar = tk.Scrollbar(frame, command=text_widget.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Configure the Text widget to use the Scrollbar
    text_widget.config(yscrollcommand=scrollbar.set)

    # Start the Tkinter event loop
    root.mainloop()