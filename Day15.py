# Advent of Code 2020 Day 15

import AOC


def part_1():
    
    lines = AOC.get_input_lines(15, AOC.format_strip)
    numbers = lines[0].split(",")

    # part_1
    total_count = 2020

    # part_2
    total_count = 30000000

    # test
    #numbers = ["0","3","6"]
    #total_count = 10

    turn = 1
    spoken = []
    spoken_history = {}

    def add_or_append_history(number : str):
        if number in spoken_history.keys():
            spoken_history[number].append(turn)
        else:
            spoken_history[number] = [turn]

    for number in numbers:

        spoken.append(number)
        add_or_append_history(number)
        turn += 1

    while turn <= total_count:  

        number = 0
        if len(spoken_history[spoken[-1]]) > 1:
            number = spoken_history[spoken[-1]][-1] - spoken_history[spoken[-1]][-2]

        # print("Turn {}, Number {}, Repeat {}".format(turn, number, last_was_repeat))
        spoken.append(str(number))
        add_or_append_history(str(number))
        
        if turn % 10000000 == 0:
            print(turn , float(turn) / 30000000 , "%")

        turn += 1

    print("Spoken:", spoken)
    print("Last:", spoken[-1])

# Main
part_1()
