import collections

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


def process_burst(set_dict, direction, location, transform):
    new_direction = list(direction)
    cur_loc_status = set_dict[tuple(location)]
    set_dict[tuple(location)] = transform[cur_loc_status]
    if cur_loc_status == '.':
        # Turn left
        new_direction[0], new_direction[1] = -new_direction[1], new_direction[0]
    elif cur_loc_status == 'W':
        # No direction change
        pass
    elif cur_loc_status == '#':
        # Turn right
        new_direction[0], new_direction[1] = new_direction[1], -new_direction[0]
    elif cur_loc_status == 'F':
        # Reverse direction
        new_direction[0], new_direction[1] = -new_direction[0], -new_direction[1]
    else:
        raise Exception("Unknown location status: %s" % cur_loc_status)

    infected_this_burst = (transform[cur_loc_status] == '#')
    new_location = [sum(x) for x in zip(new_direction, location)]
    return new_direction, new_location, infected_this_burst


starting_dict = collections.defaultdict(lambda: '.')
for i, line in enumerate(INPUT):
    for j, char in enumerate(line):
        if char == "#":
            starting_dict[tuple([i - (len(line) // 2), j - (len(line) // 2)])] = '#'

set_dict = starting_dict.copy()
cur_dir = [-1, 0]
cur_loc = [0, 0]
infection_count = 0
V1_TRANSFORM = {'.': '#', '#': '.'}

for i in xrange(10000):
    cur_dir, cur_loc, new_infection = process_burst(set_dict, cur_dir, cur_loc, V1_TRANSFORM)
    if new_infection:
        infection_count += 1

print("Final infection count for v1: %d" % infection_count)

set_dict = starting_dict.copy()
cur_dir = [-1, 0]
cur_loc = [0, 0]
infection_count = 0
V2_TRANSFORM = {'.': 'W', 'W': '#', '#': 'F', 'F': '.'}

for i in xrange(10000000):
    cur_dir, cur_loc, new_infection = process_burst(set_dict, cur_dir, cur_loc, V2_TRANSFORM)
    if new_infection:
        infection_count += 1
    if (i + 1) % 1000000 == 0:
        print("Infection count is %d after %d bursts" % (infection_count, i + 1))

print("Final infection count for v2: %d" % infection_count)
