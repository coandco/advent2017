import time
from typing import Set

from advent2017_day10 import calc_hash, get_reduced_hash
from utils import BaseCoord as Coord
from utils import read_data


def get_group(on_bits: Set[Coord], start: Coord) -> Set[Coord]:
    group = {start}
    queue = [start]
    while queue:
        curloc = queue.pop()
        for neighbor in curloc.cardinal_neighbors():
            if neighbor not in group and neighbor in on_bits:
                group.add(neighbor)
                queue.append(neighbor)
    return group


def count_groups(on_bits: Set[Coord]):
    remaining = on_bits.copy()
    num_groups = 0
    while remaining:
        num_groups += 1
        remaining -= get_group(remaining, next(iter(remaining)))
    return num_groups


def main():
    on_bits = set()
    key = read_data()
    for y in range(128):
        line_hash = get_reduced_hash(calc_hash(f"{key}-{y}", 64))
        line_1s = [i for i, x in enumerate(f"{int(line_hash, 16):0128b}") if x == "1"]
        on_bits |= {Coord(x=x, y=y) for x in line_1s}

    print(f"Part one: {len(on_bits)}")
    print(f"Part two: {count_groups(on_bits)}")


if __name__ == "__main__":
    start = time.monotonic()
    main()
    print(f"Time: {time.monotonic()-start}")
