import os
import tkinter as tk
from tkinter import simpledialog, messagebox
from dotenv import load_dotenv
import user
import master

# User data
inventory = user.UserInventory()
# Master data
master_data = master.MasterData()

def validate_name(name):
    """Validate the user's name."""
    if len(name) > 20:
        return False
    # Allow only alphanumeric and common symbols
    allowed_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{};:'\",.<>?/\\|`~ "
    return all(c in allowed_chars for c in name)

def get_user_name():
    """Prompt the user for their name if the file doesn't exist."""
    file_path = "data/output/name.txt"

    # Ensure directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Check if the file exists
    if not os.path.exists(file_path):
        while True:
            # Ask for user input using a Tkinter dialog
            user_name = simpledialog.askstring("Enter Your Name", "Please enter your name (max 20 characters):")
            if not user_name:  # If the user cancels or leaves blank
                messagebox.showwarning("Input Required", "Name cannot be empty. Please try again.")
                continue

            if validate_name(user_name):
                # Save the name to the file
                with open(file_path, "w") as f:
                    f.write(user_name)
                return user_name
            else:
                messagebox.showerror(
                    "Invalid Name",
                    "Name must only contain letters, numbers, or common symbols and be at most 20 characters long."
                )
    else:
        # Read the existing name from the file
        with open(file_path, "r") as f:
            return f.read().strip()
        
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
    
def suggest_items(event, entry, suggestions_listbox):
    """Suggest items based on user input."""
    user_input = entry.get().strip().lower()
    suggestions_listbox.delete(0, tk.END)  # Clear existing suggestions

    if user_input:  # If there's input, filter suggestions
        matches = [
            item for item in master_data.set_items.keys()
            if user_input in item.lower()
        ]
        for match in matches:
            suggestions_listbox.insert(tk.END, match)

    # Show or hide the suggestions Listbox based on matches
    if suggestions_listbox.size() > 0:
        suggestions_listbox.place(x=entry.winfo_x(), y=entry.winfo_y() + entry.winfo_height())
    else:
        suggestions_listbox.place_forget()
        
def select_suggestion(event, entry, suggestions_listbox):
    """Insert the selected suggestion into the Entry widget."""
    selected_item = suggestions_listbox.get(tk.ANCHOR)
    if selected_item:
        entry.delete(0, tk.END)
        entry.insert(0, selected_item)
        suggestions_listbox.place_forget()  # Hide suggestions

def add_item_callback(entry, category, output_label):
    """Callback for adding items to the inventory."""
    item = entry.get().strip()
    if validate_and_add_item(item, category):
        output_label.config(text=f"Item '{item}' successfully added to {category}!")
    else:
        output_label.config(text=f"Invalid item: '{item}'. Not found in MasterData.")
    entry.delete(0, tk.END)

def print_inventory(text_widget, item_group='set'):
    """Print inventory to Text Widget.
    By default set items, param item_group toggles set/unique/other items.
    """
    
    text_widget.delete("1.0", tk.END)  # Clear previous content

    if (item_group == 'set'):
        text_widget.insert(tk.END, "Set items:\n")
        for si in inventory.set_items:
            text_widget.insert(tk.END, f"{si}\n")
    elif (item_group == 'unique'):
        text_widget.insert(tk.END, "Unique items:\n")
        for ui in inventory.unique_items:
            text_widget.insert(tk.END, f"{ui}\n")
    else:
        text_widget.insert(tk.END, "Other items:\n")
        for oi in inventory.other_items:
            text_widget.insert(tk.END, f"{oi}\n")
    # TODO: Add display logic for other categories if needed

if __name__ == "__main__":
    # for value in master_data.set_items.keys():
    #     print(value)
    # for i in master_data.unique_items.keys():
    #     print(i)
    # og_data = helpers.sort_og_text_data()
    # print(og_data)
    # exit()
    
    # Tkinter UI setup
    root = tk.Tk()
    root.title("Diablo II Item Tracker")
    root.geometry("800x600")
    
    # Prompt for name if not already set
    user_name = get_user_name()
    ownership = "'" if user_name.endswith('s') else "'s"

    # Display the name in the main window
    greeting_label = tk.Label(root, text=f"{user_name}{ownership} DII Inventory", font=('Arial', 18))
    greeting_label.pack(pady=10)

    # Frame for inputs and buttons
    input_frame = tk.Frame(root)
    input_frame.pack(pady=10)

    # Updated UI for Set Items Entry with Suggestions
    set_label = tk.Label(input_frame, text="Add Set Item:")
    set_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
    set_entry = tk.Entry(input_frame, width=30)
    set_entry.grid(row=0, column=1, padx=5, pady=5)

    # Listbox for suggestions
    set_suggestions = tk.Listbox(root, height=5, width=30)

    # Bind events for dynamic suggestions
    set_entry.bind("<KeyRelease>", lambda e: suggest_items(e, set_entry, set_suggestions))
    set_suggestions.bind("<ButtonRelease-1>", lambda e: select_suggestion(e, set_entry, set_suggestions))
    set_suggestions.bind("<Return>", lambda e: select_suggestion(e, set_entry, set_suggestions))

    # Add button for adding the selected set item
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
    
    # Radio buttons for toggling item groups
    item_group_var = tk.StringVar(value='set')  # Default to 'set'

    toggle_frame = tk.Frame(root)
    toggle_frame.pack(pady=5)

    tk.Label(toggle_frame, text="Toggle Item Group:").pack(side=tk.LEFT, padx=5)

    tk.Radiobutton(toggle_frame, text="Set Items", variable=item_group_var, value='set', 
                   command=lambda: print_inventory(text_widget, item_group_var.get())).pack(side=tk.LEFT, padx=5)
    tk.Radiobutton(toggle_frame, text="Unique Items", variable=item_group_var, value='unique', 
                   command=lambda: print_inventory(text_widget, item_group_var.get())).pack(side=tk.LEFT, padx=5)
    tk.Radiobutton(toggle_frame, text="Other Items", variable=item_group_var, value='other', 
                   command=lambda: print_inventory(text_widget, item_group_var.get())).pack(side=tk.LEFT, padx=5)

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