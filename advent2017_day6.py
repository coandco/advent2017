INPUT = """4	1	15	12	0	9	9	5	5	8	7	3	14	5	12	3"""

seen_banks = []


def rotate(banks):
    max_num = max(banks)
    # Get the lowest-numbered index that has the max amount in it
    max_cell = sorted([x for x, y in enumerate(banks) if y == max_num])[0]
    to_distribute = banks[max_cell]
    banks[max_cell] = 0

    current_cell = max_cell
    while to_distribute > 0:
        current_cell = (current_cell + 1) % len(banks)
        banks[current_cell] += 1
        to_distribute -= 1


BANKS = [int(x) for x in INPUT.split()]

iterations = 0
while BANKS not in seen_banks:
    print("BANKS is %r" % BANKS)
    seen_banks.append(list(BANKS))
    rotate(BANKS)
    print("new BANKS is %r" % BANKS)
    iterations += 1

print ("Total iterations: %d" % iterations)

print("Indexes of final item: %r" % (iterations - sorted([x for x, y in enumerate(seen_banks) if seen_banks[x] == BANKS])[0]))



