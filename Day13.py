# Advent of Code 2020 Day 13

import AOC
from operator import itemgetter, attrgetter

def part_1():
    lines = AOC.get_input_lines(13, AOC.format_strip)
    earliest_timestamp = int(lines[0])
    buses = list(map(int, lines[1].replace(",x","").split(",")))

    print(earliest_timestamp)
    print(buses)

    best_wait = -1
    best_bus = -1

    for bus in buses:
        wait = -(earliest_timestamp % bus) + bus
        print("Bus {} Wait {}".format(bus, wait))
        if wait < best_wait or best_wait == -1:
            best_wait = wait
            best_bus = bus

    print("Result: ", best_bus * best_wait)

def part_2():

    def for_calculate(buses : []):

        # buses = [(17,0),(13,2),(19,3)]
        print(buses) 

        STEP = 0
        OFFSET = 1
        
        time = 0
        step = buses[0][STEP]
        
        for i in range(1, len(buses)):

            while not (time + buses[i][OFFSET]) % buses[i][STEP] == 0:
                time += step

            step *= buses[i][STEP]
    
        print("Result:", time)

    lines = AOC.get_input_lines("13", AOC.format_strip)
    slots = lines[1].split(",")
    buses = []

    for i in range(0, len(slots)):
        if slots[i] != "x":
            buses.append((int(slots[i]),i))

    print("Buses: {}".format(buses))

    for_calculate(buses)

# Main
part_1()
part_2()
