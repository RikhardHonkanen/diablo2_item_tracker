import os
import helpers.utils as utils
import csv

MASTER_DATA_PATH = "../data/master"  # Rel. to parse_file() func

class MasterData:
    def __init__(self):
        # Initialize data by reading files
        self.set_items = init_master_set_items()
        self.unique_items = init_master_unique_items()
        # self.other_items = helpers.parse_file(f"{MASTER_DATA_PATH}/other.txt")

# def init_all_sets(set_items_raw):
#     """index	*ID	set	item	*ItemName	rarity
#     ^^First few entries in the "labels" row in master data^^ We are mainly 
#     interested in the "set" entry at index 2 for each row here.
#     """
    
#     return set_items

def init_master_set_items():
    """Initialize the master set items dictionary from raw data.

    Reads the set items data from a tab-delimited file and organizes it into 
    a dictionary where each item is keyed by its name. Missing or empty fields 
    in the raw data are handled by assigning "N/A" as a default value.
    """
    set_items_raw = utils.parse_file(f"{MASTER_DATA_PATH}/set.txt")
    labels = set_items_raw.pop(0).split('\t')  # Pop the row with labels
    set_items = {}
    
    for item in set_items_raw:
        entries = item.split('\t')
        set_name = entries[2] if len(entries) > 2 else ""
        if set_name:  # Only process items with a valid set name
            if set_name not in set_items:
                set_items[set_name] = {}  # Initialize the set dictionary if not present
            
            item_name = entries[0]
            set_items[set_name][item_name] = {}  # Add the item to the inner dictionary
            
            # Populate item details (if needed, based on labels)
            for idx, label in enumerate(labels):
                skip = [0, 2]
                if (idx in skip or idx > 4):
                    continue
                value = entries[idx] if idx < len(entries) and entries[idx].strip() else "N/A"
                set_items[set_name][item_name][label] = value
    
    return set_items

def init_master_unique_items():
    """Initialize master unique items"""
    unique_items_raw = utils.parse_file(f"{MASTER_DATA_PATH}/unique.txt")
    unique_items = {}
    labels = unique_items_raw.pop(0).split('\t')
    
    for idx, item in enumerate(unique_items_raw):
        entries = item.split('\t')
        unique_items[entries[0]] = {}
        for idx, label in enumerate(labels):
            # If the index is out of range or the value is an empty string, assign "N/A"
            if idx >= len(entries) or entries[idx].strip() == "":
                unique_items[entries[0]][label] = "N/A"
            else:
                unique_items[entries[0]][label] = entries[idx]
    
    return unique_items
    