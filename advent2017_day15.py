INPUT_A = 277
INPUT_B = 349


def gen_value(start, factor, multiple=1):
    current = (start * factor) % 2147483647
    while current % multiple != 0:
        current = (current * factor) % 2147483647
    while True:
        yield current
        current = (current * factor) % 2147483647
        while current % multiple != 0:
            current = (current * factor) % 2147483647


gen_a = gen_value(INPUT_A, 16807)
gen_b = gen_value(INPUT_B, 48271)
total_matches = 0
for i in xrange(40000000):
    string_a = format(next(gen_a), "#032b")[-16:]
    string_b = format(next(gen_b), "#032b")[-16:]
    if string_a == string_b:
        total_matches += 1
    if i % 1000000 == 0:
        print("V1 iterated %d times, %d matches so far" % (i, total_matches))

print("Total matches for v1: %d" % total_matches)

gen_a = gen_value(INPUT_A, 16807, 4)
gen_b = gen_value(INPUT_B, 48271, 8)
total_matches = 0
for i in xrange(5000000):
    string_a = format(next(gen_a), "#032b")[-16:]
    string_b = format(next(gen_b), "#032b")[-16:]
    if string_a == string_b:
        total_matches += 1
    if i % 1000000 == 0:
        print("V2 iterated %d times, %d matches so far" % (i, total_matches))

print("Total matches for v2: %d" % total_matches)
