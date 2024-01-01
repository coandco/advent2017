from typing import List

from utils import read_data
import time


def rotate(banks: List[int]):
    max_num = max(banks)
    # Get the lowest-numbered index that has the max amount in it
    max_cell = sorted(x for x, y in enumerate(banks) if y == max_num)[0]
    to_distribute = banks[max_cell]
    banks[max_cell] = 0

    current_cell = max_cell
    while to_distribute > 0:
        current_cell = (current_cell + 1) % len(banks)
        banks[current_cell] += 1
        to_distribute -= 1


def main():
    banks = [int(x) for x in read_data().split()]
    seen_banks = []
    iterations = 0
    while banks not in seen_banks:
        seen_banks.append(banks[:])
        rotate(banks)
        iterations += 1
    print(f"Part one: {iterations}")
    print(f"Part two: {iterations - sorted([x for x, y in enumerate(seen_banks) if seen_banks[x] == banks])[0]}")


if __name__ == '__main__':
    start = time.monotonic()
    main()
    print(f"Time: {time.monotonic()-start}")
