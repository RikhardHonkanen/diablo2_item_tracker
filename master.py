import os
import helpers
import csv

MASTER_DATA_PATH = "data/master"

class MasterData:
    def __init__(self):
        # Initialize data by reading files
        self.set_items = helpers.parse_file(f"{MASTER_DATA_PATH}/set.txt")
        self.unique_items = helpers.parse_file(f"{MASTER_DATA_PATH}/unique.txt")
        # self.other_items = helpers.parse_file(f"{MASTER_DATA_PATH}/other.txt")