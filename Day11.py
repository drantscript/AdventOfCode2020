# Advent of Code 2020 Day 11

import AOC

EMPTY = "L"
OCCUPIED = "#"
FLOOR = "."

X = 0
Y = 1

def is_visible_with_step(start_x : int, start_y : int, step_x : int , step_y : int, seats : []) -> str:
    
    Y_MAX = len(seats)
    X_MAX = len(seats[start_y])

    def in_valid_range(position : [], seats : []) -> bool:
        return position[X] >= 0 and position[X] < X_MAX and position[Y] >= 0 and position[Y] < Y_MAX
    
    test = [start_x,start_y]
    test[X] += step_x
    test[Y] += step_y

    while in_valid_range(test, seats):

        if seats[test[Y]][test[X]] == OCCUPIED:
            return True
        elif seats[test[Y]][test[X]] == EMPTY:
            return False

        test[X] += step_x
        test[Y] += step_y

    return False

def occupy_seat(x : int, y : int, seats : []) -> str:
    
    Y_MAX = len(seats) - 1
    X_MAX = len(seats[y]) - 1
    total = 0

    if x < X_MAX and seats[y][x+1] == OCCUPIED:
        total += 1
    if x > 0 and seats[y][x-1] == OCCUPIED:
        total += 1
    if y < Y_MAX:
        total += 1 if seats[y+1][x] == OCCUPIED else 0
        if x > 0 and seats[y+1][x-1] == OCCUPIED:
            total += 1
        if x < X_MAX and seats[y+1][x+1] == OCCUPIED:
            total += 1
    if y > 0:
        total += 1 if seats[y-1][x] == OCCUPIED else 0
        if x > 0 and seats[y-1][x-1] == OCCUPIED:
            total += 1
        if x < X_MAX and seats[y-1][x+1] == OCCUPIED:
            total += 1

    if seats[y][x] == OCCUPIED:
        return OCCUPIED if total < 4 else EMPTY
    else:
        return OCCUPIED if total == 0 else EMPTY

def occupy_seat_part2(x : int, y : int, seats : []) -> str:

    total_visible = 0

    if is_visible_with_step(x, y, 1, 0, seats):
        total_visible += 1
    if is_visible_with_step(x, y, 1, 1, seats):
        total_visible += 1
    if is_visible_with_step(x, y, 1, -1, seats):
        total_visible += 1
    if is_visible_with_step(x, y, 0, 1, seats):
        total_visible += 1
    if is_visible_with_step(x, y, 0, -1, seats):
        total_visible += 1
    if is_visible_with_step(x, y, -1, 0, seats):
        total_visible += 1
    if is_visible_with_step(x, y, -1, 1, seats):
        total_visible += 1
    if is_visible_with_step(x, y, -1, -1, seats):
        total_visible += 1
    
    if seats[y][x] == OCCUPIED:
        return OCCUPIED if total_visible < 5 else EMPTY
    else:
        return OCCUPIED if total_visible == 0 else EMPTY

def count_occupied(seats : []) -> int:
    
    count = 0
    for y in range(0, len(seats)):
        for x in range(0, len(seats[y])):
            if seats[y][x] == OCCUPIED:
                count += 1
    return count

def part_2():

    lines = AOC.get_input_lines("11", AOC.format_strip)
    old_seats = []
    for line in lines:
        old_seats.append(list(line))

    anything_changed = True
    while anything_changed:

        new_seats = [x[:] for x in old_seats]
        anything_changed = False

        for y in range(0, len(old_seats)):
            for x in range(0, len(old_seats[y])):
                if old_seats[y][x] != FLOOR:

                    new_seat = occupy_seat_part2(x , y , old_seats)

                    if new_seat != new_seats[y][x]:
                        new_seats[y][x] = new_seat
                        anything_changed = True

        old_seats = [x[:] for x in new_seats]

    print("Final:")
    for row in range(0, len(new_seats)):
        print("".join(new_seats[row]))
    print("")

    print("Occupied:", count_occupied(new_seats))
    return

# Main
part_2()
