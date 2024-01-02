import re
import time
from collections import defaultdict

from utils import read_data

DIGITS = re.compile(r"\d+")


def pipe_group(pipe_dict, start_pipe, group=None):
    if group is None:
        group = {start_pipe}
    for pipe in pipe_dict[start_pipe]:
        if pipe not in group:
            group.add(pipe)
            group = pipe_group(pipe_dict, pipe, group)
    return group


def main():
    pipe_dict = defaultdict(set)
    for line in read_data().splitlines():
        name, *connections = (int(x) for x in DIGITS.findall(line))
        pipe_dict[name] = set(connections)
    base_group = pipe_group(pipe_dict, 0)
    print(f"Part one: {len(base_group)}")
    leftover_pipes = set(pipe_dict.keys()) - base_group
    num_groups = 1
    while len(leftover_pipes) > 0:
        next_group = pipe_group(pipe_dict, next(iter(leftover_pipes)))
        leftover_pipes = leftover_pipes - next_group
        num_groups += 1
    print(f"Part two: {num_groups}")


if __name__ == "__main__":
    start = time.monotonic()
    main()
    print(f"Time: {time.monotonic()-start}")
