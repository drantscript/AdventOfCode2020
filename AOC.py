# Advent of Code 2020 Helpers

import os

def get_input_lines(day : int, format_func : callable(str) = None) -> list:
    """
    : Read lines of current day to list, optionally formats
    """
    print("===========================")
    print("Advent of Code 2020 Day" , str(day))
    print("===========================")
    
    file_name = "inputs/day" + str(day) + ".txt"
    assert os.path.exists(file_name) == True, str("Required file not found: " + file_name)
    file = open(file_name, "r")

    lines = []
    for line in file:
        lines.append(line if format_func == None else format_func(line))

    file.close()

    return lines

def format_to_int(line : str) -> int:
    return int(line.strip())

def format_strip(line : str) -> str:
    return line.strip()
