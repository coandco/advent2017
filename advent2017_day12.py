import re
import time
from collections import defaultdict
from typing import Dict, Set

from utils import read_data

DIGITS = re.compile(r"\d+")


class Pipes:
    pipes: Dict[int, Set[int]]

    def __init__(self, raw_pipes: str):
        self.pipes = defaultdict(set)
        for line in raw_pipes.splitlines():
            name, *connections = (int(x) for x in DIGITS.findall(line))
            self.pipes[name] = set(connections)

    def pipe_group(self, start_pipe, group=None):
        if group is None:
            group = {start_pipe}
        for pipe in self.pipes[start_pipe]:
            if pipe not in group:
                group.add(pipe)
                group = self.pipe_group(pipe, group)
        return group


def main():
    pipes = Pipes(read_data())
    base_group = pipes.pipe_group(0)
    print(f"Part one: {len(base_group)}")
    leftover_pipes = set(pipes.pipes) - base_group
    num_groups = 1
    while leftover_pipes:
        leftover_pipes -= pipes.pipe_group(next(iter(leftover_pipes)))
        num_groups += 1
    print(f"Part two: {num_groups}")


if __name__ == "__main__":
    start = time.monotonic()
    main()
    print(f"Time: {time.monotonic()-start}")
