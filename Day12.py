# Advent of Code 2020 Day 12

import AOC

X = 0
Y = 1
compass = {"N":[0,1], "E":[1,0], "S":[0,-1], "W":[-1,0]}
rotation = {"R":1, "L":-1}
compass_str = "".join(compass.keys())
rotate_str = "".join(rotation.keys())

def part_1():

    position = [0,0]
    facing = "E"
    print("Initial:", position[X], position[Y], facing)

    lines = AOC.get_input_lines(12, AOC.format_strip)
    for line in lines:

        action = str(line[:1])
        value = int(line[1:])

        if action in compass_str:
            position[X] += compass[action][X] * value
            position[Y] += compass[action][Y] * value

        if action == "F":
            position[X] += compass[facing][X] * value
            position[Y] += compass[facing][Y] * value

        if action in rotate_str:
            steps = int(int(rotation[action] * value) / 90)
            total_steps = len(compass_str)
            facing = compass_str[(total_steps + compass_str.find(facing) + steps) % total_steps]
        
        print("Position: {},{} Direction: {}".format(position[X], position[Y], facing))
    print("Manhattan Distance:", abs(position[X]) + abs(position[Y]))

def part_2():

    def rotate_90(xy : [], clockwise : int) -> []:
        return [clockwise * xy[1] , -clockwise * xy[0]]

    ship = [0,0]
    waypoint_relative = [10,1]
    print("Initial:", ship[X], ship[Y])

    lines = AOC.get_input_lines("12", AOC.format_strip)
    for line in lines:

        action = str(line[:1])
        value = int(line[1:])

        if action in compass_str:
            waypoint_relative[X] += compass[action][X] * value
            waypoint_relative[Y] += compass[action][Y] * value

        if action == "F":
            ship[X] += waypoint_relative[X] * value
            ship[Y] += waypoint_relative[Y] * value

        if action in rotate_str:
            for _ in range(0, int(int(abs(rotation[action]) * value) / 90)):
                waypoint_relative = rotate_90(waypoint_relative, rotation[action])
        
        print("Position: {},{} Waypoint: {} {}".format(ship[X], ship[Y], waypoint_relative[X], waypoint_relative[Y]))
    print("Manhattan Distance:", abs(ship[X]) + abs(ship[Y]))

# Main
part_1()
part_2()