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

def init_all_set_names_in_collection(set_items_raw, set_items):
    """index	*ID	set	item	*ItemName	rarity
    First few entries in the "labels" rowin master data. We are mainly 
    interested in the "set" entry at index 2 for each row here.
    """
    all_sets = set()
    for item in set_items_raw:
        entries = item.split('\t')
        if (len(entries) > 2 and entries[2] != ''):
            all_sets.add(entries[2])

def init_master_set_items():
    """Initialize the master set items dictionary from raw data.

    Reads the set items data from a tab-delimited file and organizes it into 
    a dictionary where each item is keyed by its name. Missing or empty fields 
    in the raw data are handled by assigning "N/A" as a default value.
    """
    set_items_raw = utils.parse_file(f"{MASTER_DATA_PATH}/set.txt")
    labels = set_items_raw.pop(0).split('\t')  # Pop the row with labels, careful if moving this
    
    set_items = {}
    set_items = init_all_set_names_in_collection(set_items_raw, set_items)
    
    for idx, item in enumerate(set_items_raw):
        entries = item.split('\t')
        set_items[entries[0]] = {}
        for idx, label in enumerate(labels):
            # If the index is out of range or the value is an empty string, assign "N/A"
            if idx >= len(entries) or entries[idx].strip() == "":
                set_items[entries[0]][label] = "N/A"
            else:
                set_items[entries[0]][label] = entries[idx]
    
    return set_items

def init_master_unique_items():
    """Initialize master unique items, same handling as for set items"""
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
    