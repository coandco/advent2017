import time
from collections import defaultdict
from typing import Dict

from utils import BaseCoord as Coord
from utils import read_data

DIRECTIONS = {"N": Coord(x=0, y=-1), "E": Coord(x=1, y=0), "S": Coord(x=0, y=1), "W": Coord(x=-1, y=0)}
RIGHT_TURN = {"N": "E", "E": "S", "S": "W", "W": "N"}
LEFT_TURN = {"N": "W", "E": "N", "S": "E", "W": "S"}


class Cluster:
    grid: Dict[Coord, str]
    curloc: Coord
    curdir: str
    num_infected: int = 0
    transforms: Dict[str, str]

    def __init__(self, raw_grid: str, transforms: Dict[str, str]):
        self.grid = defaultdict(lambda: ".")
        lines = raw_grid.splitlines()
        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                if char == "#":
                    self.grid[Coord(x=x, y=y)] = char
        self.transforms = transforms
        self.curloc = Coord(x=len(lines) // 2, y=len(lines) // 2)
        self.curdir = "N"

    def step(self):
        status = self.grid[self.curloc]
        self.grid[self.curloc] = self.transforms[status]

        if status == ".":
            self.curdir = LEFT_TURN[self.curdir]
        elif status == "#":
            self.curdir = RIGHT_TURN[self.curdir]
        elif status == "F":
            self.curdir = RIGHT_TURN[RIGHT_TURN[self.curdir]]
        elif status == "W":
            pass
        else:
            raise Exception(f"Unknown grid status {status}")

        if self.grid[self.curloc] == "#":
            self.num_infected += 1

        self.curloc += DIRECTIONS[self.curdir]


def main():
    cluster = Cluster(read_data(), {"#": ".", ".": "#"})
    for _ in range(10_000):
        cluster.step()
    print(f"Part one: {cluster.num_infected}")
    cluster = Cluster(read_data(), {".": "W", "W": "#", "#": "F", "F": "."})
    for _ in range(10_000_000):
        cluster.step()
    print(f"Part two: {cluster.num_infected}")


if __name__ == "__main__":
    start = time.monotonic()
    main()
    print(f"Time: {time.monotonic()-start}")
