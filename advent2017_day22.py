INPUT = """.......##.#..####.#....##
..###....###.####..##.##.
#..####.#....#.#....##...
.#....#.#.#....#######...
.###..###.#########....##
##...#####..#####.###.#..
.#..##.###.#.#....######.
.#.##.#..####..#.##.....#
#.#..###..##..#......##.#
##.###.##.#.#...##.#.##..
##...#.######.#..##.#...#
....#.####..#..###.##..##
...#....#.###.#.#..#.....
..###.#.#....#.....#.####
.#....##..##.#.#...#.#.#.
...##.#.####.###.##...#.#
##.#.####.#######.##..##.
.##...#......####..####.#
#..###.#.###.##.#.#.##..#
#..###.#.#.#.#.#....#.#.#
####.#..##..#.#..#..#.###
##.....#..#.#.#..#.####..
#####.....###.........#..
##...#...####..#####...##
.....##.#....##...#.....#""".split("\n")


def location_status(set_dict, location):
    for status in set_dict:
        if tuple(location) in set_dict[status]:
            return status
    return '.'


def set_status(set_dict, location, new_status):
    for status in set_dict:
        if status == new_status:
            set_dict[status].add(tuple(location))
        else:
            set_dict[status].discard(tuple(location))
    return set_dict


def process_burst_v1(set_dict, direction, location):
    new_direction = list(direction)
    cur_loc_status = location_status(set_dict, location)
    infected_this_burst = False
    if cur_loc_status == '.':
        set_dict = set_status(set_dict, location, '#')
        infected_this_burst = True
        # Turn left
        new_direction[0], new_direction[1] = -new_direction[1], new_direction[0]
    elif cur_loc_status == '#':
        set_dict = set_status(set_dict, location, '.')
        # Turn right
        new_direction[0], new_direction[1] = new_direction[1], -new_direction[0]
    else:
        raise Exception("Unknown location status: %s" % cur_loc_status)

    new_location = [sum(x) for x in zip(new_direction, location)]
    return set_dict, new_direction, new_location, infected_this_burst


def process_burst_v2(set_dict, direction, location):
    new_direction = list(direction)
    cur_loc_status = location_status(set_dict, location)
    infected_this_burst = False
    if cur_loc_status == '.':
        set_dict = set_status(set_dict, location, 'W')
        # Turn left
        new_direction[0], new_direction[1] = -new_direction[1], new_direction[0]
    elif cur_loc_status == 'W':
        set_dict = set_status(set_dict, location, '#')
        infected_this_burst = True
        # No direction change
    elif cur_loc_status == '#':
        set_dict = set_status(set_dict, location, 'F')
        # Turn right
        new_direction[0], new_direction[1] = new_direction[1], -new_direction[0]
    elif cur_loc_status == 'F':
        set_dict = set_status(set_dict, location, '.')
        # Reverse direction
        new_direction[0], new_direction[1] = -new_direction[0], -new_direction[1]
    else:
        raise Exception("Unknown location status: %s" % cur_loc_status)

    new_location = [sum(x) for x in zip(new_direction, location)]
    return set_dict, new_direction, new_location, infected_this_burst

INFECTED_NODES = set()
for i, line in enumerate(INPUT):
    for j, char in enumerate(line):
        if char == "#":
            INFECTED_NODES.add((i-12, j-12))

set_dict = {'#': set(INFECTED_NODES), 'W': set(), 'F': set()}
current_direction = [-1, 0]
current_location = [0, 0]
infection_count = 0

for i in xrange(10000):
    infected_set, current_direction, current_location, new_infection = process_burst_v1(set_dict,
                                                                                        current_direction,
                                                                                        current_location)
    if new_infection:
        infection_count += 1

print("Final infection count for v1: %d" % infection_count)

set_dict = {'#': set(INFECTED_NODES), 'W': set(), 'F': set()}
current_direction = [-1, 0]
current_location = [0, 0]
infection_count = 0

for i in xrange(10000000):
    infected_set, current_direction, current_location, new_infection = process_burst_v2(set_dict,
                                                                                        current_direction,
                                                                                        current_location)
    if new_infection:
        infection_count += 1
    if (i + 1) % 1000000 == 0:
        print("Infection count is %d after %d bursts" % (infection_count, i + 1))

print("Final infection count for v2: %d" % infection_count)
