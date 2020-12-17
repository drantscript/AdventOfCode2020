# Advent of Code 2020 Day 17

import AOC

INACTIVE = False
ACTIVE = True

X = 0
Y = 1
Z = 2
W = 3

STATE = 0
DESIRED = 1

input = "17" # 17
lines = AOC.get_input_lines(input, AOC.format_strip)

for line in lines:
    print(line)

def text_to_dimension(input : []) -> {}:

    dimension = {}
    for i, line in enumerate(lines):
        y = i
        for j, char in enumerate(line):
            x = j
            z = 0
            w = 0
            dimension[(x,y,z,w)] = [ACTIVE,INACTIVE] if char == "#" else [INACTIVE,INACTIVE]

    return dimension

dimension = text_to_dimension(lines)

def dimension_to_text(dimension : {}) -> []:

    x_range= [0,0]
    y_range = [0,0]
    z_range = [0,0]
    w_range = [0,0]

    for point in dimension.keys():

        if point[X] < x_range[0]:
            x_range[0] = point[X]
        if point[X] > x_range[1]:
            x_range[1] = point[X]

        if point[Y] < y_range[0]:
            y_range[0] = point[Y]
        if point[Y] > y_range[1]:
            y_range[1] = point[Y]

        if point[Z] < z_range[0]:
            z_range[0] = point[Z]
        if point[Z] > z_range[1]:
            z_range[1] = point[Z]

        if point[W] < w_range[0]:
            w_range[0] = point[W]
        if point[W] > w_range[1]:
            w_range[1] = point[W]

    print("Dimension to text:")
    for w in range(w_range[0], w_range[1] + 1):
        for z in range(z_range[0], z_range[1] + 1):
            print("z =", z, "w =", w)
            lines = []
            for y in range(y_range[0], y_range[1] + 1):
                line = []
                for x in range(x_range[0], x_range[1] + 1):
                    line.append("#" if dimension[(x,y,z,w)][STATE] else ".")
                lines.append(line)

            for line in lines:
                print("".join(line))
    return

def get_neighbors(coord : tuple) -> []:
    
    coords = []

    coords.append((coord[0], coord[1], coord[2] + 1))
    coords.append((coord[0], coord[1], coord[2] - 1))

    coords.append((coord[0], coord[1] + 1, coord[2]    ))
    coords.append((coord[0], coord[1] + 1, coord[2] + 1))
    coords.append((coord[0], coord[1] + 1, coord[2] - 1))
    coords.append((coord[0], coord[1] - 1, coord[2]    ))
    coords.append((coord[0], coord[1] - 1, coord[2] + 1))
    coords.append((coord[0], coord[1] - 1, coord[2] - 1))

    coords.append((coord[0] + 1, coord[1],     coord[2]    ))
    coords.append((coord[0] + 1, coord[1],     coord[2] + 1))
    coords.append((coord[0] + 1, coord[1],     coord[2] - 1))
    coords.append((coord[0] + 1, coord[1] + 1, coord[2]    ))
    coords.append((coord[0] + 1, coord[1] + 1, coord[2] + 1))
    coords.append((coord[0] + 1, coord[1] + 1, coord[2] - 1))
    coords.append((coord[0] + 1, coord[1] - 1, coord[2]    ))
    coords.append((coord[0] + 1, coord[1] - 1, coord[2] + 1))
    coords.append((coord[0] + 1, coord[1] - 1, coord[2] - 1))

    coords.append((coord[0] - 1, coord[1],     coord[2]    ))
    coords.append((coord[0] - 1, coord[1],     coord[2] + 1))
    coords.append((coord[0] - 1, coord[1],     coord[2] - 1))
    coords.append((coord[0] - 1, coord[1] + 1, coord[2]    ))
    coords.append((coord[0] - 1, coord[1] + 1, coord[2] + 1))
    coords.append((coord[0] - 1, coord[1] + 1, coord[2] - 1))
    coords.append((coord[0] - 1, coord[1] - 1, coord[2]    ))
    coords.append((coord[0] - 1, coord[1] - 1, coord[2] + 1))
    coords.append((coord[0] - 1, coord[1] - 1, coord[2] - 1))

    return coords

def get_neighbors_4d(coord : tuple) -> []:
    
    coords = []

    coords_3d = get_neighbors(coord)

    for coord_3d in coords_3d:
        coords.append((coord_3d[0], coord_3d[1], coord_3d[2], coord[3]))

    for coord_3d in coords_3d:
        coords.append((coord_3d[0], coord_3d[1], coord_3d[2], coord[3] + 1))

    for coord_3d in coords_3d:
        coords.append((coord_3d[0], coord_3d[1], coord_3d[2], coord[3] - 1))

    coords.append((coord[0] , coord[1] , coord[2] , coord[3] + 1))
    coords.append((coord[0] , coord[1] , coord[2] , coord[3] - 1))

    return coords

def desired_state(coord : tuple) -> bool:

    active_neighbors = 0
    for neighbor in get_neighbors_4d(coord):
        if neighbor not in dimension:
            # Any two-step distant neighbors are guaranteed to be invalid still
            dimension[neighbor] = [INACTIVE,INACTIVE]
        elif dimension[neighbor][STATE] == ACTIVE:
            active_neighbors += 1

    if dimension[coord][STATE] == ACTIVE and (active_neighbors == 2 or active_neighbors == 3):
        return ACTIVE
    elif dimension[coord][STATE] == INACTIVE and (active_neighbors == 3):
        return ACTIVE

    return INACTIVE

def cycle_dimension():

    coords = list(dimension.keys())

    # Generate neighbors that need to be iterated over
    for coord in coords:
        for neighbor in get_neighbors_4d(coord):
            if neighbor not in dimension:
                dimension[neighbor] = [INACTIVE,INACTIVE]

    coords = list(dimension.keys())

    # Flag all live coordinates for updates
    for coord in coords:
        dimension[coord][DESIRED] = desired_state(coord)

    # Do the updates
    for coord in coords:
        dimension[coord][STATE] = dimension[coord][DESIRED]
        dimension[coord][DESIRED] = INACTIVE

dimension_to_text(dimension)

def part_both():

    cycles = 6
    for _ in range(0, cycles):
        cycle_dimension()
    
    # Danger may get large
    # dimension_to_text(dimension)

    active = 0
    for coord in dimension.keys():
        active += dimension[coord][STATE] == ACTIVE

    print("Final active (after {} cycles): {}".format(str(cycles), str(active)))

# Main
part_both()
