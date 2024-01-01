from collections import defaultdict
from typing import Iterable

from utils import read_data, BaseCoord
import time


class Coord(BaseCoord):
    def turn_left(self) -> 'Coord':
        return Coord(x=-self.y, y=self.x)


def spiral() -> Iterable[Coord]:
    curloc = Coord(x=0, y=0)
    curdir = Coord(x=0, y=-1)
    while True:
        # For three of the corners, we turn when X=Y.  For the fourth, we have to go one beyond to start the next
        # bigger spiral.
        if abs(curloc.x) == abs(curloc.y) and curdir != Coord(x=1, y=0) or curloc.x > 0 and curloc.y == 1-curloc.x:
            curdir = curdir.turn_left()              # corner, change direction

        yield curloc
        curloc += curdir


def adjacent_spiral() -> Iterable[int]:
    values = defaultdict(int)
    for coord in spiral():
        values[coord] = 1 if coord == (0, 0) else sum(values[x] for x in coord.neighbors())
        yield values[coord]


def main():
    puz_input = int(read_data())
    coords_at_input = next(x for i, x in enumerate(spiral(), start=1) if i == puz_input)
    print(f"Part one: {sum(abs(x) for x in coords_at_input)}")
    print(f"Part two: {next(x for x in adjacent_spiral() if x > puz_input)}")


if __name__ == '__main__':
    start = time.monotonic()
    main()
    print(f"Time: {time.monotonic()-start}")
