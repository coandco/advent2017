from typing import Dict, Optional, Tuple

from utils import read_data, BaseCoord as Coord
import time

DIRECTIONS = {'N': Coord(x=0, y=-1), 'E': Coord(x=1, y=0), 'S': Coord(x=0, y=1), 'W': Coord(x=-1, y=0)}
RIGHT_TURN = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
LEFT_TURN = {'N': 'W', 'E': 'N', 'S': 'E', 'W': 'S'}


class Tubes:
    grid: Dict[Coord, str]
    start: Coord
    max_x: int
    max_y: int

    def __init__(self, raw_grid: str):
        self.grid = {}
        lines = raw_grid.splitlines()
        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                if char != " ":
                    self.grid[Coord(x=x, y=y)] = char
        self.start = next(k for k, v in self.grid.items() if k.y == 0)
        self.max_y, self.max_x = len(lines), len(lines[0])

    def plus_turn(self, coord: Coord, curdir: str) -> Optional[str]:
        if self.grid[coord] != "+":
            return None
        for direction in (RIGHT_TURN[curdir], LEFT_TURN[curdir]):
            if coord + DIRECTIONS[direction] in self.grid:
                return direction
        return None

    def follow_line(self) -> Tuple[str, int]:
        letters_seen = []
        steps_taken = 0
        curloc = self.start
        curdir = 'S'

        while curloc in self.grid:
            if self.grid[curloc] in ('-', '|'):
                curloc += DIRECTIONS[curdir]
                steps_taken += 1
            elif self.grid[curloc] == '+':
                curdir = self.plus_turn(curloc, curdir)
                curloc += DIRECTIONS[curdir]
                steps_taken += 1
            else:
                letters_seen.append(self.grid[curloc])
                curloc += DIRECTIONS[curdir]
                steps_taken += 1

        return ''.join(letters_seen), steps_taken


def main():
    tubes = Tubes(read_data())
    letters, steps = tubes.follow_line()
    print(f"Part one: {letters}")
    print(f"Part two: {steps}")


if __name__ == '__main__':
    start = time.monotonic()
    main()
    print(f"Time: {time.monotonic()-start}")
