import time
from itertools import chain
from typing import Dict, Iterable, List

from utils import read_data


class Pattern(tuple):
    def rotate(self) -> "Pattern":
        # taken from https://stackoverflow.com/a/8421412
        return Pattern(tuple(zip(*self[::-1])))

    def flipud(self) -> "Pattern":
        return Pattern(self[::-1])

    def fliplr(self) -> "Pattern":
        return Pattern(tuple(x[::-1] for x in self))

    def permutations(self) -> Iterable["Pattern"]:
        cur_pattern = self
        for _ in range(4):
            cur_pattern = cur_pattern.rotate()
            yield cur_pattern
            yield cur_pattern.fliplr()
            yield cur_pattern.flipud()


class Fractal:
    rules: Dict[Pattern, Pattern]
    grid: List[List[bool]]

    def __init__(self, raw_rules: str):
        self.rules = {}
        self.grid = [[False, True, False], [False, False, True], [True, True, True]]
        for rule in raw_rules.splitlines():
            rawfrom, rawto = rule.split(" => ", maxsplit=1)
            rulefrom = Pattern(tuple(c == "#" for c in x) for x in rawfrom.split("/"))
            ruleto = Pattern(tuple(c == "#" for c in x) for x in rawto.split("/"))
            for permutation in rulefrom.permutations():
                self.rules[permutation] = ruleto

    def permute(self):
        new_grid = []
        chunksize = 2 if len(self.grid) % 2 == 0 else 3
        for y in range(0, len(self.grid), chunksize):
            new_lines = [[] for _ in range(chunksize + 1)]
            for x in range(0, len(self.grid), chunksize):
                chunk = tuple(tuple(self.grid[r][x : x + chunksize]) for r in range(y, y + chunksize))
                permuted_chunk = self.rules[chunk]
                for i, line in enumerate(permuted_chunk):
                    new_lines[i].extend(line)
            new_grid.extend(new_lines)
        self.grid = new_grid

    def total_on(self):
        return sum(chain(*self.grid))


def main():
    fractal = Fractal(read_data())
    for i in range(18):
        fractal.permute()
        if i == 4:
            print(f"Part one: {fractal.total_on()}")
    print(f"Part two: {fractal.total_on()}")


if __name__ == "__main__":
    start = time.monotonic()
    main()
    print(f"Time: {time.monotonic()-start}")
