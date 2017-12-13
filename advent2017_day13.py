INPUT = """0: 3
1: 2
2: 4
4: 6
6: 4
8: 6
10: 5
12: 6
14: 9
16: 6
18: 8
20: 8
22: 8
24: 8
26: 8
28: 8
30: 12
32: 14
34: 10
36: 12
38: 12
40: 10
42: 12
44: 12
46: 12
48: 12
50: 12
52: 14
54: 14
56: 12
62: 12
64: 14
66: 14
68: 14
70: 17
72: 14
74: 14
76: 14
82: 14
86: 18
88: 14
96: 14
98: 44"""

EXAMPLE = """0: 3
1: 2
4: 4
6: 4"""


# To determine if a particular layer is at the top at a particular time, I examined some examples.
# For a range of two, the "is this at the top at a particular time" pattern goes True, False, True, False...
# For a range of three, it goes True, False, False, False, True...
# For a range of four, it goes True, False, False, False, False, False, True...
# This can be generalized as "one True every n time increments, where n is (range - 1) * 2"
def is_caught(range, cur_time):
    if range == 1:
        return True
    else:
        return (cur_time % ((range-1)*2)) == 0


def traverse(firewall, delay=0):
    caught_instances = []
    max_layer = max(firewall.keys()) + 1  # Layers start at 0

    for i in xrange(max_layer):
        # If we get caught
        if i in firewall.keys() and is_caught(firewall[i], i+delay):
            caught_instances.append((i, firewall[i]))

    return caught_instances

LAYERS = {}

for line in INPUT.split("\n"):
    depth, range = line.split(": ")
    LAYERS[int(depth)] = int(range)

caught_instances = traverse(LAYERS)

print("Caught instances: %r" % caught_instances)
severity = sum([x[0] * x[1] for x in caught_instances])
print("Total severity: %d" % severity)

delay = 0
while True:
    caught_instances = traverse(LAYERS, delay)
    if len(caught_instances) == 0:
        break
    else:
        # print("Tested delay of %d, got %r" % (delay, caught_instances))
        delay += 1

print("Min delay for uncaught traversal: %d" % delay)