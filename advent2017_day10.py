from itertools import izip_longest
import operator

INPUT = """106,16,254,226,55,2,1,166,177,247,93,0,255,228,60,36"""

SALT = [17, 31, 73, 47, 23]
V2_INPUT = [ord(x) for x in INPUT] + SALT


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
    return izip_longest(*args, fillvalue=fillvalue)

knot_hash = list(range(256))


index = 0
skip = 0
for instruction in INPUT.split(","):
    knot_hash, index, skip = handle_instruction(knot_hash, index, skip, int(instruction))

print("Knot hash v1 is %r" % knot_hash)
print("First two items of knot hash v1 are %r, multiplied equal %d" % (knot_hash[:2], knot_hash[0] * knot_hash[1]))

knot_hash = list(range(256))
index = 0
skip = 0

for i in xrange(64):
    for instruction in V2_INPUT:
        knot_hash, index, skip = handle_instruction(knot_hash, index, skip, int(instruction))

print("Knot hash v2 after permutation: %r" % knot_hash)

reduced_hash = []
for chunk in grouper(knot_hash, 16):
    # print("Chunk is %r" % list(chunk))
    xor_value = reduce(operator.xor, chunk, 0)
    # print("XOR of chunk is %r" % xor_value)
    reduced_hash.append(xor_value)

print("Reduced v2 hash is %r" % reduced_hash)
print("Hex string of v2 hash is %s" % ''.join([format(x, '02x') for x in reduced_hash]))

