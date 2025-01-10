import os

def parse_file(path):    
    if not os.path.isabs(path):
        # If the path is relative, make it relative to the script's directory
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), path)
    with open(path, "r") as f:
        parsed_input = f.read().split('\n')
    return parsed_input