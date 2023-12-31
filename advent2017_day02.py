import time
from itertools import combinations
from typing import List

from utils import read_data


def calc_checksum_two(num_list: List[int]) -> int:
    return next(i // j for x in combinations(num_list, 2) if (i := max(x)) % (j := min(x)) == 0 and i // j > 0)


def main():
    parsed_lines = [[int(x) for x in line.split()] for line in read_data().splitlines()]
    part_one_checksums = [max(x) - min(x) for x in parsed_lines]
    print(f"Part one: {sum(part_one_checksums)}")
    part_two_checksums = [calc_checksum_two(x) for x in parsed_lines]
    print(f"Part two: {sum(part_two_checksums)}")


if __name__ == "__main__":
    start = time.monotonic()
    main()
    print(f"Time: {time.monotonic()-start}")
