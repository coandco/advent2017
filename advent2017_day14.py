import itertools
import operator

import numpy as np
from scipy.ndimage import label

INPUT = "oundnydw"

SALT = [17, 31, 73, 47, 23]


def rotate(to_rotate, amount):
    actual_amount = amount % len(to_rotate)
    return to_rotate[actual_amount:] + to_rotate[:actual_amount]


def reverse(to_reverse):
    return to_reverse[::-1]


def handle_instruction(queue_in, index, skip, length):
    rotated = rotate(queue_in, index)
    rotated[:length] = reverse(rotated[:length])
    return rotate(rotated, -index), index+length+skip, skip+1


def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return itertools.izip_longest(*args, fillvalue=fillvalue)


def knot_hash(input, iterations, salt):
    my_hash = list(range(256))
    index = 0
    skip = 0

    salted_input = [ord(x) for x in input] + salt

    for i in xrange(iterations):
        for instruction in salted_input:
            my_hash, index, skip = handle_instruction(my_hash, index, skip, int(instruction))

    print("Knot hash v2 after permutation: %r" % my_hash)

    reduced_hash = []

    for chunk in grouper(my_hash, 16):
        # print("Chunk is %r" % list(chunk))
        xor_value = reduce(operator.xor, chunk, 0)
        # print("XOR of chunk is %r" % xor_value)
        reduced_hash.append(xor_value)
    return reduced_hash


total_bits = 0
binary_grid = []
for i in xrange(128):
    line_hash = knot_hash("%s-%d" % (INPUT, i), 64, SALT)
    binary_hash = [[int(y) for y in format(x, "08b")] for x in line_hash]
    # Flatten list
    binary_hash = list(itertools.chain.from_iterable(binary_hash))
    binary_grid.append(binary_hash)
    print("Hash for line %03d is %r" % (i, line_hash))
    bits_in_line = len([x for x in binary_hash if x == 1])
    print("Number of on bits in hash: %d" % bits_in_line)
    total_bits += bits_in_line

print("Total on bits for all lines: %d" % total_bits)

numpy_bin_grid = np.array(binary_grid)
_, count = label(numpy_bin_grid)
print("Total groups: %d" % count)
