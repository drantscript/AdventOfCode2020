# Advent of Code 2020 Day 8

import AOC

CMD = 0
VAL = 1

def get_code() -> []:

    lines = AOC.get_input_lines(8, AOC.format_strip)
    code = []
    for line in lines:
        line.replace("+","")
        split = line.split(" ")
        code.append(split)

    return code

def run_code(code : [] , log_errors = False) -> bool:

    acc = 0
    line = 0
    lines_run = []

    while line < len(code):

        if line in lines_run:
            if log_errors:
                print("ERROR loop detected on line:", line)
                print("Current accumulated value:", acc)
            return False

        lines_run.append(line)
        if code[line][CMD] == "acc":
            acc += int(code[line][VAL])
            line += 1
        elif code[line][CMD] == "jmp":
            line += int(code[line][VAL])
        elif code[line][CMD] == "nop":
            line += 1
        else:
            print("ERROR undefined CMD:", code[line])

    print("SUCCESS")
    print("Current accumulated value:", acc)
    return True

def swap_cmd(cmd : str) -> str:
    if cmd == "nop":
        return "jmp"
    elif cmd == "jmp":
        return "nop"
    return cmd

# Main
code = get_code()

# Part 1
run_code(code, log_errors=True)

# Part 2
for line in range(0, len(code)):
    
    # Try swapping the command
    code[line][CMD] = swap_cmd(code[line][CMD])

    # Try to run code
    if run_code(code, log_errors=False):
        print("Succeeded changing line:", line)
        break

    # Swap back
    code[line][CMD] = swap_cmd(code[line][CMD])
