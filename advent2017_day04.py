import time
from collections import Counter

from utils import read_data


def main():
    num_valid_v1 = 0
    num_valid_v2 = 0

    for line in read_data().split("\n"):
        words = line.split()
        sorted_words = ["".join(sorted(x)) for x in line.split()]
        counts = Counter(words)
        anagram_counts = Counter(sorted_words)
        if counts.most_common()[0][1] == 1:
            num_valid_v1 += 1
        if anagram_counts.most_common()[0][1] == 1:
            num_valid_v2 += 1

    print(f"Part one: {num_valid_v1}")
    print(f"Part two: {num_valid_v2}")


if __name__ == "__main__":
    start = time.monotonic()
    main()
    print(f"Time: {time.monotonic()-start}")
