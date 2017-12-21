import numpy
import math

def hash_to_num(char):
    return 1 if char == '#' else 0


INPUT = """../.. => .../#../#..
#./.. => ###/#.#/.#.
##/.. => ###/.##/##.
.#/#. => .#./..#/...
##/#. => ##./.##/#..
##/## => #.#/###/.##
.../.../... => #.#./.#.#/#.#./###.
#../.../... => #..#/.###/##../##..
.#./.../... => #.##/####/.###/....
##./.../... => ####/.#../#.##/#.##
#.#/.../... => ..../#.../.##./#.##
###/.../... => .###/.#../...#/.#..
.#./#../... => .###/#..#/#.../#...
##./#../... => ..##/...#/#.##/..##
..#/#../... => #.##/.#../...#/..##
#.#/#../... => #.##/..##/..../##.#
.##/#../... => .###/.###/#.../....
###/#../... => #.../####/.#.#/....
.../.#./... => ...#/##.#/...#/###.
#../.#./... => #.#./####/.#../##.#
.#./.#./... => #..#/.##./..##/...#
##./.#./... => ###./#.#./#.../###.
#.#/.#./... => ..#./###./####/.#.#
###/.#./... => .#.#/#..#/..#./#..#
.#./##./... => ####/##../##../..##
##./##./... => #.../..##/#.#./....
..#/##./... => ..../#..#/.#../#..#
#.#/##./... => ###./..##/#.#./#...
.##/##./... => ...#/#..#/####/...#
###/##./... => ..../#.##/###./...#
.../#.#/... => #.../#.../...#/#...
#../#.#/... => ##../#..#/.##./.##.
.#./#.#/... => ##../.###/#.##/#.#.
##./#.#/... => ##.#/.#.#/#.#./..#.
#.#/#.#/... => .##./...#/...#/.#..
###/#.#/... => ####/..#./###./#.##
.../###/... => #..#/.#.#/#.##/..#.
#../###/... => .#../##../##../#.##
.#./###/... => #.#./...#/#.#./#.##
##./###/... => #.#./#..#/.###/.###
#.#/###/... => ..#./...#/..#./#..#
###/###/... => ##../###./####/....
..#/.../#.. => ##../.#../#.#./.##.
#.#/.../#.. => .##./##.#/.#../#...
.##/.../#.. => ####/..#./#..#/##..
###/.../#.. => #.#./..../..#./####
.##/#../#.. => ..##/..##/.##./##..
###/#../#.. => #..#/#..#/.##./.#..
..#/.#./#.. => #..#/#.##/##../#..#
#.#/.#./#.. => .#.#/.#.#/.##./.#.#
.##/.#./#.. => ####/#.##/..../.###
###/.#./#.. => #..#/.#.#/.##./....
.##/##./#.. => ###./##../#..#/....
###/##./#.. => ...#/.#../.#../....
#../..#/#.. => ###./#.../..##/#...
.#./..#/#.. => .#../#.##/.##./..#.
##./..#/#.. => ..#./.##./..../..##
#.#/..#/#.. => #.#./###./.#.#/#..#
.##/..#/#.. => ####/..##/###./.#.#
###/..#/#.. => ##.#/.##./.###/###.
#../#.#/#.. => ..../#.##/.#.#/#..#
.#./#.#/#.. => .###/..../.###/#.##
##./#.#/#.. => ####/..##/#.##/#.##
..#/#.#/#.. => ..#./..##/####/#...
#.#/#.#/#.. => .##./.#.#/.#.#/##..
.##/#.#/#.. => ##.#/##.#/#.##/.###
###/#.#/#.. => #..#/.##./#.##/.###
#../.##/#.. => ####/...#/..##/##..
.#./.##/#.. => .##./#.##/...#/#...
##./.##/#.. => .##./..#./###./....
#.#/.##/#.. => .#.#/##.#/..#./##.#
.##/.##/#.. => ###./####/.##./####
###/.##/#.. => ..#./##.#/.#../..#.
#../###/#.. => ##../#.##/#.../.#.#
.#./###/#.. => ..#./#.##/...#/...#
##./###/#.. => .###/###./.##./###.
..#/###/#.. => #.../..../#.../#...
#.#/###/#.. => .###/...#/...#/..#.
.##/###/#.. => #.#./..../###./.#.#
###/###/#.. => #..#/#.../#.##/##.#
.#./#.#/.#. => .#../##../..##/#.##
##./#.#/.#. => #.##/#.#./#..#/##.#
#.#/#.#/.#. => #..#/.###/..../###.
###/#.#/.#. => #.#./.#.#/####/#.#.
.#./###/.#. => ..##/..#./..##/###.
##./###/.#. => ##../#.#./#.#./.#..
#.#/###/.#. => ####/.##./####/#.#.
###/###/.#. => ####/..#./####/....
#.#/..#/##. => ###./..#./.#../...#
###/..#/##. => #.#./#.##/#..#/##..
.##/#.#/##. => ..../.#../..../....
###/#.#/##. => .###/..#./#.#./####
#.#/.##/##. => ..../.#.#/#.#./...#
###/.##/##. => ##../.#../.#.#/..##
.##/###/##. => ..#./#.#./##../..##
###/###/##. => ..#./###./#.#./..##
#.#/.../#.# => #.#./..../#.##/.#.#
###/.../#.# => #.##/#.../..##/...#
###/#../#.# => ####/.###/..#./.#.#
#.#/.#./#.# => ..#./#..#/#..#/##..
###/.#./#.# => ..../##../.#.#/##.#
###/##./#.# => ..##/..##/.#../####
#.#/#.#/#.# => ####/...#/#.#./#.#.
###/#.#/#.# => #.##/...#/..#./...#
#.#/###/#.# => #.##/####/#..#/..##
###/###/#.# => .##./.##./.##./.#..
###/#.#/### => .#../..../..../.###
###/###/### => #.#./#.#./###./###.""".split("\n")


def permutation_generator(pattern):
    for i in xrange(4):
        rotated_pattern = numpy.rot90(pattern, i)
        yield rotated_pattern
        yield numpy.fliplr(rotated_pattern)
        yield numpy.flipud(rotated_pattern)


def expand_rules(rules):
    expanded_rules = {}
    for rule in rules:
        for permutation in permutation_generator(rule[0]):
            if permutation.tobytes() not in expanded_rules.keys():
                expanded_rules[permutation.tobytes()] = rule[1]
    return expanded_rules


def blockshaped(arr, nrows, ncols):
    """
    Return an array of shape (n, nrows, ncols) where
    n * nrows * ncols = arr.size

    If arr is a 2D array, the returned array should look like n subblocks with
    each subblock preserving the "physical" layout of arr.

    Cribbed from https://stackoverflow.com/a/16858283
    """
    h, w = arr.shape
    return (arr.reshape(h//nrows, nrows, -1, ncols)
               .swapaxes(1, 2)
               .reshape(-1, nrows, ncols))


def stitch_chunks(chunks):
    # If our list of chunks is only one element long, no stitching is required.
    if chunks.shape[0] == 1:
        return chunks[0]
    grid_size = int(math.sqrt(chunks.shape[0]))
    shaped_chunks = chunks.reshape(grid_size, grid_size, chunks.shape[1], chunks.shape[1])
    stitched_chunks = None
    for row_to_stitch in shaped_chunks:
        stitched_row = numpy.concatenate(row_to_stitch, 1)
        if stitched_chunks is None:
            stitched_chunks = stitched_row
        else:
            stitched_chunks = numpy.concatenate((stitched_chunks, stitched_row), 0)
    return stitched_chunks


def run_iteration(expanded_rules, current_grid):
    if current_grid.shape[0] % 2 == 0:
        divisor = 2
    elif current_grid.shape[0] % 3 == 0:
        divisor = 3
    else:
        print("Divisor should equal 2 or 3.  We shouldn't be here.")
        return None

    chunks = blockshaped(current_grid, divisor, divisor)
    transformed_chunks = []
    for chunk in chunks:
        transformed_chunks.append(expanded_rules[chunk.tobytes()])
    return stitch_chunks(numpy.array(transformed_chunks))


TEST_STRINGS = ".#./..#/###, .#./#../###, #../#.#/##., ###/..#/.#., .##/..#/###"
TEST_PATTERNS = [numpy.array([[hash_to_num(x) for x in y] for y in z.split('/')]) for z in TEST_STRINGS.split(', ')]

STARTING_PATTERN_STRING = ".#./..#/###"
STARTING_PATTERN = numpy.array([[hash_to_num(x) for x in y] for y in STARTING_PATTERN_STRING.split('/')])

RULES = []

for line in INPUT:
    left, right = line.split(' => ')
    left_rows = [[hash_to_num(x) for x in y] for y in left.split('/')]
    right_rows = [[hash_to_num(x) for x in y] for y in right.split('/')]
    RULES.append((numpy.array(left_rows), numpy.array(right_rows)))

EXPANDED_RULES = expand_rules(RULES)

# Using numpy.array here to force a copy of the starting pattern to occur, so we don't mutate it
current_grid = numpy.array(STARTING_PATTERN)

for i in xrange(18):
    current_grid = run_iteration(EXPANDED_RULES, current_grid)
    #print("Grid after iteration %d: \n%s" % (i, current_grid))
    #print("Shape of grid after iteration %d: %s" % (i, current_grid.shape))
    if i == 4:
        print("Number of activated pixels after five iterations: %d" % numpy.count_nonzero(current_grid))

print("Number of activated pixels after 18 iterations: %d" % numpy.count_nonzero(current_grid))

print current_grid


