import time
from math import prod
from typing import Dict

from utils import read_data


class Firewall:
    layers: Dict[int, int]

    def __init__(self, raw_layers: str):
        self.layers = {}
        for line in raw_layers.splitlines():
            depth, range = (int(x) for x in line.split(": "))
            self.layers[depth] = range

    # To determine if a particular layer is at the top at a particular time, I examined some examples.
    # For a range of two, the "is this at the top at a particular time" pattern goes True, False, True, False...
    # For a range of three, it goes True, False, False, False, True...
    # For a range of four, it goes True, False, False, False, False, False, True...
    # This can be generalized as "one True every n time increments, where n is (range - 1) * 2"
    @staticmethod
    def is_caught(range: int, cur_time: int) -> bool:
        return True if range == 1 else (cur_time % ((range - 1) * 2)) == 0

    def traverse(self, delay: int = 0, fail_early: bool = False):
        caught_instances = []
        max_layer = max(self.layers.keys()) + 1  # Layers start at 0
        for i in range(max_layer):
            # If we get caught
            if i in self.layers.keys() and self.is_caught(self.layers[i], i + delay):
                caught_instances.append((i, self.layers[i]))
                if fail_early:
                    break
        return caught_instances


def main():
    firewall = Firewall(read_data())
    caught_instances = firewall.traverse()
    print(f"Part one: {sum(prod(x) for x in caught_instances)}")
    delay = 0
    while caught_instances:
        delay += 1
        caught_instances = firewall.traverse(delay, fail_early=True)
    print(f"Part two: {delay}")


if __name__ == "__main__":
    start = time.monotonic()
    main()
    print(f"Time: {time.monotonic()-start}")
