# Advent of Code 2020 Day 15

import AOC

lines = AOC.get_input_lines(16, AOC.format_strip)
    
ranges = []
my_ticket = []
other_tickets = []

# extra for part_2
fields = []
field_index_has_departure = []

parse_section = 1
for line in lines:

    if line == "":

        parse_section += 1
        
    elif parse_section == 1:

        value_split = line.split(": ")[1]
        range_split = value_split.split(" or ")
        ranges.append([int(v) for v in range_split[0].split("-")])
        ranges.append([int(v) for v in range_split[1].split("-")])

        # extra for part_2
        fields.append([[int(v) for v in range_split[0].split("-")],[int(v) for v in range_split[1].split("-")]])
        field_index_has_departure.append("departure" in line.split(": ")[0])

    elif parse_section == 2 and ":" not in line:

        my_ticket = [int(v) for v in line.split(",")]

    elif parse_section == 3 and ":" not in line:
        
        other_tickets.append([int(v) for v in line.split(",")])

def in_ranges(v : int) -> bool:
    for r in ranges:
        if r[0] <= v <= r[1]:
            return True
    return False

def part_1():

    # print("ranges", ranges)
    # print("my ticket", my_ticket)
    # print("other tickets", other_tickets)

    invalid_values = []

    for ticket in other_tickets:
        for value in ticket:
            if not in_ranges(value):
                invalid_values.append(value)          

    # print("invalid values", invalid_values)

    sum = 0
    for value in invalid_values:
        sum += value

    print("Sum:", sum)

    return

def part_2():

    # print("ranges", ranges)
    # print("fields", fields)
    # print("my ticket", my_ticket)
    # print("other tickets", other_tickets)

    valid_tickets = []

    for ticket in other_tickets:
        valid = True
        for value in ticket:
            if not in_ranges(value):
                valid = False
                break
        if valid:
            valid_tickets.append(ticket)

    # print("valid tickets", valid_tickets)

    def in_field(value : int, field_index : int) -> bool:
        for f in fields[field_index]:
            if f[0] <= value and value <= f[1]:
                return True
        return False

    count = len(valid_tickets[0])
    # print("field count", count)

    # All fields are possible at all ticket indices so far
    ticket_index_possible_fields = []
    for i in range(0, count):
        ticket_index_possible_fields.append(list(range(0,count)))

    for ticket in valid_tickets:
        for ticket_index in range(0,count):
            for field_index in range(0,count):
                if not in_field(ticket[ticket_index], field_index) and field_index in ticket_index_possible_fields[ticket_index]:
                    ticket_index_possible_fields[ticket_index].remove(field_index)
                    # print("removed", fields[field_index], "from value", valid_tickets[ticket_index])

    # print("Possible fields:", ticket_index_possible_fields)

    ticket_index_real_fields = {}
    consumed_fields = []

    # lets just assume this will work
    while len(consumed_fields) < count:

        # find fields that only have one value option and save those
        for i, index in enumerate(ticket_index_possible_fields):
            if len(index) == 1:
                ticket_index_real_fields[i] = index[0]
                consumed_fields.append(index[0])

        # clean all possible fields of confirmed values
        for i, index in enumerate(ticket_index_possible_fields):
            for field in consumed_fields:
                if field in ticket_index_possible_fields[i]:
                    ticket_index_possible_fields[i].remove(field)

    # print("Final fields:", ticket_index_real_fields)

    keys = list(ticket_index_real_fields.keys())
    values = list(ticket_index_real_fields.values())
    result = 1

    for i in range(0, count):
        if field_index_has_departure[values[i]]:
            result *= my_ticket[keys[i]]

    print("Result:", result)

    return

# Main
part_1()
part_2()