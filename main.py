import os, sys
import helpers

def main(input):  # TODO: no base input, call functions for data
    print(input)           
    return 1

if __name__ == "__main__":
    SUCCESS, ERROR = 1, 0
    input = helpers.parse_file("set_items.txt")
    print(f"Exit: {main(input)} (expected {SUCCESS})")