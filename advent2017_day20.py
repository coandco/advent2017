import re
import time
from collections import defaultdict, deque
from itertools import chain
from typing import List, NamedTuple

from utils import BaseCoord3D as Coord3D
from utils import read_data

DIGITS = re.compile("[0-9-]+")


class Particle(NamedTuple):
    p: Coord3D
    v: Coord3D
    a: Coord3D

    @staticmethod
    def from_line(line: str):
        px, py, pz, vx, vy, vz, ax, ay, az = (int(x) for x in DIGITS.findall(line))
        return Particle(Coord3D(x=px, y=py, z=pz), Coord3D(x=vx, y=vy, z=vz), Coord3D(x=ax, y=ay, z=az))

    def update(self) -> "Particle":
        new_v = self.v + self.a
        new_p = self.p + new_v
        return Particle(new_p, new_v, self.a)


class Swarm:
    particles: List[Particle]

    def __init__(self, raw_particles: str):
        self.particles = [Particle.from_line(x) for x in raw_particles.splitlines()]

    def lowest_accel(self) -> int:
        origin = Coord3D(0, 0, 0)
        index, particle = min(((i, p) for i, p in enumerate(self.particles)), key=lambda x: origin.distance(x[1].a))
        return index

    def collide(self) -> int:
        remaining = set(self.particles)
        last_3 = deque(maxlen=3)
        while len(last_3) < 3 or last_3[-1] == 1000 or not all(x == last_3[0] for x in last_3):
            remaining = {x.update() for x in remaining}
            positions = defaultdict(list)
            for particle in remaining:
                positions[particle.p].append(particle)
            collisions = set(chain(*[v for v in positions.values() if len(v) > 1]))
            remaining -= collisions
            last_3.append(len(remaining))
        return len(remaining)


def main():
    swarm = Swarm(read_data())
    print(f"Part one: {swarm.lowest_accel()}")
    print(f"Part two: {swarm.collide()}")


if __name__ == "__main__":
    start = time.monotonic()
    main()
    print(f"Time: {time.monotonic()-start}")
