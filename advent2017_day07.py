import re
import time
from typing import Dict, List, Optional

from utils import read_data

DIGITS = re.compile(r"\d+")
NAMES = re.compile(r"[a-z]+")


class Program:
    parent: Optional[str]
    name: str
    children: List[str]
    weight: int
    combined_weight: int

    def __init__(self, name: str, weight: int = 0, children: List[str] = None):
        self.parent = None
        self.name = name
        self.children = children
        self.weight = weight
        self.combined_weight = 0


class Tower:
    tower: Dict[str, Program]
    root: str

    def __init__(self, raw_input: str):
        self.tower = {}
        for line in raw_input.splitlines():
            name, *children = NAMES.findall(line)
            weight = DIGITS.findall(line)[0]
            self.tower[name] = Program(name, int(weight), children)

        for program in self.tower:
            for child in self.tower[program].children:
                self.tower[child].parent = self.tower[program].name

        self.root = next(x for x in self.tower.values() if x.parent is None).name
        self.calc_weights(self.root)

    def calc_weights(self, program_name: str):
        for child in self.tower[program_name].children:
            self.tower[program_name].combined_weight += self.calc_weights(child)

        self.tower[program_name].combined_weight += self.tower[program_name].weight
        return self.tower[program_name].combined_weight

    def find_imbalance(self) -> int:
        current_program = self.root
        off_by = None
        while True:
            children_weights = {}
            for child in self.tower[current_program].children:
                if self.tower[child].combined_weight not in children_weights:
                    children_weights[self.tower[child].combined_weight] = []
                children_weights[self.tower[child].combined_weight].append(child)
            if len(children_weights) == 1:
                return self.tower[current_program].weight + off_by
            else:
                sorted_weights = sorted(children_weights, key=lambda x: len(children_weights[x]))
                if off_by is None:
                    off_by = sorted_weights[1] - sorted_weights[0]
                current_program = children_weights[sorted_weights[0]][0]


def main():
    tower = Tower(read_data())
    print(f"Part one: {tower.root}")
    print(f"Part two: {tower.find_imbalance()}")


if __name__ == "__main__":
    start = time.monotonic()
    main()
    print(f"Time: {time.monotonic()-start}")
