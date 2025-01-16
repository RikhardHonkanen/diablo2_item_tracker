import os

def parse_file(path):    
    if not os.path.isabs(path):
        # If the path is relative, make it relative to the script's directory
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), path)
    with open(path, "r") as f:
        parsed_input = f.read().split('\n')
    return parsed_input

# Function may be removed, organizes original raw data
def sort_og_text_data():
    data = parse_file("data/output/set_original.txt")
    completed_sets = []
    incomplete_sets = {}

    current_set = None
    in_incomplete = False

    for line in data:
        if not line.strip():
            continue

        # Check for section headers
        if line == '<<Completed Sets>>':
            in_incomplete = False
            current_set = None
            continue
        elif line == '<<Incomplete Sets>>':
            in_incomplete = True
            current_set = None
            continue

        # Process completed sets
        if not in_incomplete:
            completed_sets.append(line)
        # Process incomplete sets
        else:
            if line.startswith('<<') and line.endswith('>>'):
                current_set = line
                incomplete_sets[current_set] = []
            elif current_set:
                is_found = line.startswith('~~') and line.endswith('~~')
                item_name = line.strip('~~')
                incomplete_sets[current_set].append({"name": item_name, "found": is_found})

    # Organize the result
    organized_data = {
        "completed_sets": completed_sets,
        "incomplete_sets": incomplete_sets
    }
    
    return organized_data