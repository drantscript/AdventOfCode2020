# Advent of Code 2020 Day 9

import AOC

def is_valid(value : int , previous_set : []) -> bool:
    for a in previous_set:
        for b in previous_set:
            if a != b and (a + b == value):
                return True
    return False

def sums_to_value(value : int , sum_list : []) -> bool:
    total = 0
    for number in sum_list:
        total += number
    return total == value

def part_1(lines : []):

    PREAMBLE_LEN = 25

    for i in range(PREAMBLE_LEN , len(lines)):
        if not is_valid(lines[i] , lines[i - PREAMBLE_LEN : i]):
            print("First invalid number:" , lines[i])
            return lines[i]

    print("ERROR no invalid number found")
    return 0

def part_2(lines : []):

    target = part_1(lines)
    for i in range(0 , len(lines)):
        current_index = i
        test_total = lines[current_index]

        while test_total < target:
            current_index += 1
            test_total += lines[current_index]

        if target == test_total:
            print("Found sum values:" , lines[i : current_index + 1])
            
            min = 0
            max = 0
            for value in lines[i : current_index + 1]:
                if value < min or min == 0:
                    min = value
                if value > max or max == 0:
                    max = value

            print("Min:" , min , "Max:" , max)
            print("Result:" , min + max)

            return
           

    print("ERROR no sum found")
    return

# Main
lines = AOC.get_input_lines(9, AOC.format_to_int)
part_1(lines)
part_2(lines)
