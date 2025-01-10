import os
import helpers

USER_DATA_PATH = "data/output"
# Read
def set():
    return helpers.parse_file(f"{USER_DATA_PATH}/set.txt")

def unique():
    return helpers.parse_file(f"{USER_DATA_PATH}/unique.txt")

def other():
    return helpers.parse_file(f"{USER_DATA_PATH}/other.txt")

# Delete
def del_set(set_item):
    # implement delete item
    return f"deleted {set_item}"

def del_unique(unique_item):
    # implement delete item
    return f"deleted {unique_item}"

def del_other(other_item):
    # implement delete item
    return f"deleted {other_item}"