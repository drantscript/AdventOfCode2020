# Advent of Code 2020 Day 5

import AOC

def parse_ticket(line : str):

    ROWS = 128
    SEATS = 8

    row = line[0:7:1] # 6
    seat = line[7:10:1] # 3

    ticket = {}
    ticket["row"] = 0
    ticket["seat"] = 0
    ticket["id"] = 0

    increment = ROWS
    for c in row:
        increment = increment / 2
        if c == "B":
            ticket["row"] += increment

    increment = SEATS
    for c in seat:
        increment = increment / 2
        if c == "R":
            ticket["seat"] += increment

    ticket["id"] = (int(ticket["row"]) * 8) + int(ticket["seat"])
    return ticket

def get_highest_id(tickets : []):

    highest_id = 0
    for ticket in tickets:
        if int(ticket["id"]) > highest_id:
            highest_id = int(ticket["id"])

    return highest_id

def part_1(tickets : []):
    
    print("Highest ID:" , get_highest_id(tickets))
    return

def part_2(tickets : []):

    ids = []
    for ticket in tickets:
        ids.append(int(ticket["id"]))

    passed_first = False
    for value in range(0, get_highest_id(tickets)):
        if value in ids:
            passed_first = True
        elif passed_first and (int(value) not in ids):
            print("Found open seat:", value)
    return

# Main
tickets = []
lines = AOC.get_input_lines(5, AOC.format_strip)
for line in lines:
    tickets.append(parse_ticket(line))

part_1(tickets)
part_2(tickets)






    


