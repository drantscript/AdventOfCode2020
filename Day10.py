# Advent of Code 2020 Day 10

import AOC

def part_1():
    lines = AOC.get_input_lines("10", AOC.format_to_int)
    lines.sort()

    diffs = [0,0,0]
    diffs[lines[0] - 1] += 1 # outlet to first adapter

    for i in range(0, len(lines) - 1):

        diff = lines[i+1] - lines[i]
        diffs[diff - 1] += 1

    diffs[2] += 1 # last adapter to device

    print("Diffs:" , diffs)
    print("Result: ", diffs[0] * diffs[2])

def part_2():

    def find_jump_indices(i : int, all : []) -> []:

        jump_indices = []
        if (test := i + 1) < len(all):
            if all[test] - all[i] <= 3:
                jump_indices.append(test)
        if (test := i + 2) < len(all):
            if all[test] - all[i] <= 3:
                jump_indices.append(test)
        if (test := i + 3) < len(all):
            if all[test] - all[i] <= 3:
                jump_indices.append(test)
        return jump_indices

    lines = AOC.get_input_lines("10", AOC.format_to_int)
    lines.sort()

    lines.insert(0,0)
    lines.append(lines[len(lines) - 1] + 3)

    # TEST
    # lines = [0,1,2,3,6]

    print(lines)

    branches_from_here = [0] * len(lines)
    branches_from_here[len(lines) - 1] = 1

    for current_index in range((len(lines) - 1),-1,-1):
        indices = find_jump_indices(current_index, lines)
        for index in indices:
            branches_from_here[current_index] += branches_from_here[index]
    
    print("Branches from" , 0, branches_from_here[0])
    return

part_2()
