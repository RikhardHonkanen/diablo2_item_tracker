import os
import helpers

USER_DATA_PATH = "data/output"
def set():
    return helpers.parse_file(f"{USER_DATA_PATH}/set.txt")

def unique():
    return helpers.parse_file("{USER_DATA_PATH}/unique.txt")

def other():
    return helpers.parse_file("{USER_DATA_PATH}/other.txt")
