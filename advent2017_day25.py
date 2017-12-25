import collections

INPUT = {'A': [(1,  1, 'B'), (0,  1, 'F')],
         'B': [(0, -1, 'B'), (1, -1, 'C')],
         'C': [(1, -1, 'D'), (0,  1, 'C')],
         'D': [(1, -1, 'E'), (1,  1, 'A')],
         'E': [(1, -1, 'F'), (0, -1, 'D')],
         'F': [(1,  1, 'A'), (0, -1, 'E')]}

EXAMPLE = {'A': [(1,  1, 'B'), (0, -1, 'B')],
           'B': [(1, -1, 'A'), (1,  1, 'A')]}


def advance_state(tape, location, state, rules):
    current_value = tape[location]
    tape[location] = rules[state][current_value][0]
    return tape, location + rules[state][current_value][1], rules[state][current_value][2]


tape = collections.defaultdict(lambda: 0)
current_location = 0
current_state = 'A'

for i in xrange(6):
    tape, current_location, current_state = advance_state(tape, current_location, current_state, EXAMPLE)
    print("Iter: %d, Loc: %d, State: %s, Tape: %r" % (i, current_location, current_state, tape))

print("Example checksum: %d" % sum(tape.values()))

tape = collections.defaultdict(lambda: 0)
current_location = 0
current_state = 'A'

for i in xrange(12425180):
    tape, current_location, current_state = advance_state(tape, current_location, current_state, INPUT)
    if i % 1e6 == 0:
        print("Iter: %d, Loc: %d, State: %s" % (i, current_location, current_state))

print("Final checksum: %d" % sum(tape.values()))

