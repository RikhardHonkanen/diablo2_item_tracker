import os
from tkinter import simpledialog, messagebox
import helpers.validation as validation

def get_user_name():
    """Prompt the user for their name if the file doesn't exist."""
    file_path = "data/output/name.txt"

    # Ensure directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Check if the file exists
    if not os.path.exists(file_path):
        while True:
            # Ask for user input using a Tkinter dialog
            user_name = simpledialog.askstring("Enter Your Name", "What is your name adventurer? (max 20 characters):")
            if not user_name:  # If the user cancels or leaves blank
                messagebox.showwarning("Input Required", "Name cannot be empty. Please try again.")
                continue

            if validation.validate_name(user_name):
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