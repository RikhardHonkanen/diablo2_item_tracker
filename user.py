import helpers.utils as utils

USER_DATA_PATH = "../data/output"  # Rel. to parse_file() func

class UserInventory:
    def __init__(self):
        # Initialize data by reading files
        self.set_items = utils.parse_file(f"{USER_DATA_PATH}/set.txt")
        self.unique_items = utils.parse_file(f"{USER_DATA_PATH}/unique.txt")
        self.other_items = utils.parse_file(f"{USER_DATA_PATH}/other.txt")

    def refresh(self):
        """Reload data from files."""
        self.set_items = utils.parse_file(f"{USER_DATA_PATH}/set.txt")
        self.unique_items = utils.parse_file(f"{USER_DATA_PATH}/unique.txt")
        self.other_items = utils.parse_file(f"{USER_DATA_PATH}/other.txt")

    def delete_set_item(self, set_item: str) -> str:  #May start using type annotations
        """Delete an item from set items."""
        # Implement deletion logic here
        # For example, remove the item from the list and update the file
        if set_item in self.set_items:
            self.set_items.remove(set_item)
            # Optionally, write changes back to the file
            # helpers.write_file(f"{USER_DATA_PATH}/set.txt", self.set_items)
            return f"Deleted {set_item} from set"
        return f"Item {set_item} not found in set"

    def delete_unique_item(self, unique_item: str) -> str:
        """Delete an item from unique items."""
        # See comments above
        if unique_item in self.unique_items:
            self.unique_items.remove(unique_item)
            return f"Deleted {unique_item} from unique items"
        return f"Item {unique_item} not found in unique items"

    def delete_other_item(self, other_item: str) -> str:
        """Delete an item from other items."""
        # See comments above
        if other_item in self.other_items:
            self.other_items.remove(other_item)
            return f"Deleted {other_item} from other items"
        return f"Item {other_item} not found in other items"
    
    # TODO: functions
    def write_to_file(self, path):
        """Accepts a path and the data to write to the file
        returns 1 on success (?)
        """
        file = USER_DATA_PATH + path
        data = {}
        if (path == '/set'):
            pass
        
        return 1
    
    
    def add_unique_item(self, unique_item) -> str:
        """Add a unique item to inventory."""
        return f"{unique_item} added to your inventory."