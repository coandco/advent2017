import math

INPUT = 289326

SIZE_OF_GRID = int(math.ceil(math.sqrt(INPUT)))

if SIZE_OF_GRID % 2 == 0:
    SIZE_OF_GRID += 1


def spiral():
    x, y = 0, 0
    dx, dy = 0, -1
    while True:
        # For three of the corners, we turn when X=Y.  For the fourth, we have to go one beyond to start the next
        # bigger spiral.
        if abs(x) == abs(y) and (dx, dy) != (1, 0) or x > 0 and y == 1-x:
            dx, dy = -dy, dx              # corner, change direction

        yield x, y
        x, y = x+dx, y+dy


def sum_adjacent(existing_values, current_coord):
    coords_to_sum = [[(current_coord[0]+i, current_coord[1]+j) for i in xrange(-1, 2) if i != 0 or j != 0]
                     for j in xrange(-1, 2)]

    total = 0
    for i in coords_to_sum:
        for j in i:
            total += existing_values.get(j, 0)

    return total


coords_gen = spiral()

values_dict = {}

for index, coords in enumerate(coords_gen):
    #print("%d is at %r" % (index+1, coords))
    if coords == (0, 0):
        values_dict[coords] = 1
    else:
        values_dict[coords] = sum_adjacent(values_dict, coords)

    if values_dict[coords] > INPUT:
        print("Coords %r have value %d which is larger than input %d" % (coords, values_dict[coords], INPUT))
        break

    #if index == INPUT - 1:
    #    print("Coords: %r, Distance: %d" % (coords, abs(coords[0]) + abs(coords[1])))
