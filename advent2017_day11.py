import time

from utils import BaseCoord, read_data


class Coord(BaseCoord):
    def distance(self, other: "Coord"):
        distance_x = self.x - other.x
        distance_y = self.y - other.y
        distance_z = distance_x - distance_y
        return max(abs(distance_x), abs(distance_y), abs(distance_z))


DIRECTIONS = {
    "n": Coord(x=0, y=1),
    "ne": Coord(x=1, y=1),
    "se": Coord(x=1, y=0),
    "s": Coord(x=0, y=-1),
    "sw": Coord(x=-1, y=-1),
    "nw": Coord(x=-1, y=0),
}


def main():
    start = Coord(x=0, y=0)
    max_distance = 0
    curloc = start
    for direction in read_data().split(","):
        curloc += DIRECTIONS[direction]
        max_distance = max(max_distance, start.distance(curloc))
    print(f"Part one: {start.distance(curloc)}")
    print(f"Part two: {max_distance}")


if __name__ == "__main__":
    start = time.monotonic()
    main()
    print(f"Time: {time.monotonic()-start}")
