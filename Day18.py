# Advent of Code 2020 Day 18

import AOC

lines = AOC.get_input_lines(18, AOC.format_strip)

def math_to_string(full : str) -> str:

    print("Math input:", full)

    # part 2 -- if there are priority conflicts take the addition and resolve it
    while ((op_index := full.find("+")) != -1) and (full.find("*") != -1):

        op_start = 0
        for i in range(op_index - 2 , 0 , -1):
            if full[i] == " ":
                op_start = i + 1
                break

        op_end = len(full)
        for i in range(op_index + 2, len(full)):
            if full[i] == " ":
                op_end = i
                break

        full = full[0 : op_start] + math_to_string(full[op_start : op_end]) + full[op_end : len(full)]
    # end part 2

    ops = full.split(" ")
    result = 0
    current_op = "+"

    for op in ops:

        if op in "+*":
            current_op = op
        elif current_op == "+":
            result += int(op)
        elif current_op == "*":
            result *= int(op)

    return str(result)

def resolve_string(full : str) -> str:

    while (open_index := full.find("(")) != -1:
        opens = 1
        close_index = open_index + 1
        for i in range(open_index + 1, len(full)):
            if full[i] == "(":
                opens += 1
            elif full[i] == ")":
                opens -= 1
            if opens == 0:
                close_index = i
                break

        next_substring = full[open_index + 1 : close_index]
        full = full[0 : open_index] + resolve_string(next_substring) + full[close_index + 1 : len(full)]

    return math_to_string(full)

# Part 1 + 2
total = sum(int(resolve_string(line)) for line in lines)
print("Total:" , total)
