import collections
from copy import deepcopy

INPUT = """42/37
28/28
29/25
45/8
35/23
49/20
44/4
15/33
14/19
31/44
39/14
25/17
34/34
38/42
8/42
15/28
0/7
49/12
18/36
45/45
28/7
30/43
23/41
0/35
18/9
3/31
20/31
10/40
0/22
1/23
20/47
38/36
15/8
34/32
30/30
30/44
19/28
46/15
34/50
40/20
27/39
3/14
43/45
50/42
1/33
6/39
46/44
22/35
15/20
43/31
23/23
19/27
47/15
43/43
25/36
26/38
1/10""".split("\n")

CONNECTORS = []
for line in INPUT:
    values = line.split('/')
    CONNECTORS.append((int(values[0]), int(values[1]), int(values[0]) + int(values[1])))

SORTED_CONNECTORS = collections.defaultdict(lambda: [])
for connector in CONNECTORS:
    if connector not in SORTED_CONNECTORS[connector[0]]:
        SORTED_CONNECTORS[connector[0]].append(connector)
    if connector not in SORTED_CONNECTORS[connector[1]]:
        SORTED_CONNECTORS[connector[1]].append(connector)


def find_strongest_bridge(input_connector, taken_list, current_total, available_connectors):
    best_sequence = taken_list
    best_total = current_total
    #print("Evaluating %r,  total %d" % ([x[2] for x in taken_list], current_total))
    for i, connector in enumerate(SORTED_CONNECTORS[input_connector]):
        if connector not in available_connectors:
            continue
        new_available = set(available_connectors)
        new_available.remove(connector)
        new_sequence = list(taken_list)
        new_sequence.append((connector[0], i, "%s/%s" % (connector[0], connector[1])))
        input_number = connector[1] if connector[0] == input_connector else connector[0]
        total, candidate_sequence = find_strongest_bridge(input_number, new_sequence,
                                                          current_total + connector[2], new_available)
        if total > best_total:
            best_sequence = candidate_sequence
            best_total = total
    return best_total, best_sequence


def find_longest_bridge(input_connector, taken_list, current_total, available_connectors, longest_bridge):
    #print("Evaluating %r,  total %d" % ([x[2] for x in taken_list], current_total))
    connectors_to_try = [x for x in SORTED_CONNECTORS[input_connector] if x in available_connectors]
    if len(connectors_to_try) == 0:
        if longest_bridge is None or len(taken_list) > len(longest_bridge):
            longest_bridge = taken_list
        if len(taken_list) == len(longest_bridge) and current_total > sum([x[1] for x in longest_bridge]):
            longest_bridge = taken_list
    else:
        for connector in connectors_to_try:
            new_available = set(available_connectors)
            new_available.remove(connector)
            new_sequence = list(taken_list)
            new_sequence.append((connector[0], connector[2], "%s/%s" % (connector[0], connector[1])))
            input_number = connector[1] if connector[0] == input_connector else connector[0]
            longest_bridge = find_longest_bridge(input_number, new_sequence,
                                                            current_total + connector[2], new_available,
                                                            longest_bridge)

    return longest_bridge


available_connectors = set(CONNECTORS)
total, sequence = find_strongest_bridge(0, [], 0, available_connectors)

print("Total of best bridge is %d, sequence is %r" % (total, [x[2] for x in sequence]))

available_connectors = set(CONNECTORS)
longest_bridge = find_longest_bridge(0, [], 0, available_connectors, None)

print("Total of longest bridge is %d, sequence is %r " % (sum([x[1] for x in longest_bridge]), longest_bridge))
