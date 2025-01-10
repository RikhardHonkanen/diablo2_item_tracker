import os
import helpers

# USER DATA = OUTPUT
def set():
    return helpers.parse_file("data/output/set.txt")  #TODO: break out stuff into .env or constants

def unique():
    return helpers.parse_file("data/output/unique.txt")

def other():
    return helpers.parse_file("data/output/other.txt")
