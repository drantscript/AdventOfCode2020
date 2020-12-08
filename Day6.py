# Advent of Code 2020 Day 6

import AOC

def part_1():
    lines = AOC.get_input_lines(6, AOC.format_strip)
    groups = []
    current_group = ""
    for line in lines:
        if line == "":
            groups.append(current_group)
            current_group = ""
        else:
            for c in line:
                if c not in current_group:
                    current_group += c

    groups.append(current_group)
    return groups

def part_2():
    lines = AOC.get_input_lines(6, AOC.format_strip)
    groups = []
    current_group = ""
    new_line = True
    for line in lines:
        if line == "":
            groups.append(current_group)
            current_group = ""
            new_line = True
        else:
            if new_line: 
                current_group = line
                new_line = False
            else:
                test_group = current_group
                for c in test_group:
                    if c not in line:
                        current_group = current_group.replace(c, "")

    groups.append(current_group)
    return groups

# Main
# groups = part_1()
groups = part_2()

final_count = 0
for group in groups:
    final_count += len(group)

print("Final count:", final_count)
