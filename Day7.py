# Advent of Code 2020 Day 7

import AOC

lines = AOC.get_input_lines(7, AOC.format_strip)

# Parse all bag rules
def parse_rules() -> {}:
    rules = {}
    for line in lines:
        split = line.rsplit(" bags ")
        container = split[0]
        contents = []

        if "no other" not in split[1]:
            for entry in split[1].replace("contain " , "").split(","):
                if entry[0] == " ":
                    entry = entry[1:]
                entry = entry.replace(".", "")
                entry = entry.replace(" bags", "")
                entry = entry.replace(" bag", "")
                color = entry[2:]
                count = entry[:1]
                contents.append([color , count])

        rules[container] = contents
    return rules

def dig_into_color(rules : {} , color : str) -> bool: # had gold bag
    for contained_bags in rules[color]:
        if contained_bags[0] == "shiny gold":
            return True
        else:
            if dig_into_color(rules , contained_bags[0]):
                return True
    return False

def get_contained_bags(rules : {} , color : str) -> int:
    added_bags = 1 # this is a bag
    for contained_bags in rules[color]:
        print(color , "contains" , contained_bags)
        added_bags += int(contained_bags[1]) * get_contained_bags(rules , contained_bags[0])
    return added_bags

# Main
def part_1():
    rules = parse_rules()
    valid_bags = 0
    for color in rules.keys():
        if dig_into_color(rules , color):
            valid_bags += 1

    print("Valid bags:", valid_bags)

def part_2():
    rules = parse_rules()
    print("Contained bags: " , get_contained_bags(rules, "shiny gold") - 1) # doesn't contain itself

part_2()
