import os
import helpers
import csv

MASTER_DATA_PATH = "data/master"

class MasterData:
    def __init__(self):
        # Initialize data by reading files
        self.set_items = init_master_set_items()
        self.unique_items = helpers.parse_file(f"{MASTER_DATA_PATH}/unique.txt")
        # self.other_items = helpers.parse_file(f"{MASTER_DATA_PATH}/other.txt")
        
def init_master_set_items():
    set_items_raw = helpers.parse_file(f"{MASTER_DATA_PATH}/set.txt")
    set_items = {}
    labels = set_items_raw.pop(0).split('\t')
    
    # TODO: account for master data entries not being tab delimited at the end of item 
    # entries when labeled props are missing
    for idx, item in enumerate(set_items_raw):
        entries = item.split('\t')
        set_items[entries[0]] = {}
        for idx, label in enumerate(labels):
            set_items[entries[0]][label] = entries[idx]
    
    return set_items

def init_master_unique_items():
    unique_items_raw = helpers.parse_file(f"{MASTER_DATA_PATH}/unique.txt")
    unique_items = {}
    
    return unique_items
    