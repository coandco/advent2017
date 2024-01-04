from collections import defaultdict
from typing import List, NamedTuple, Dict, Set, Optional

from utils import read_data
import time


class Connector(NamedTuple):
    first: int
    second: int
    sum: int

    @staticmethod
    def from_str(raw_connector: str) -> "Connector":
        first, second = (int(x) for x in raw_connector.split("/"))
        return Connector(first, second, first + second)


class ComponentSoup:
    all_connectors: Set[Connector]
    sorted_components: Dict[int, Set[Connector]]

    def __init__(self, raw_connectors: str):
        self.connectors = {Connector.from_str(x) for x in raw_connectors.splitlines()}
        self.sorted_components = defaultdict(lambda: set())
        for connector in self.connectors:
            self.sorted_components[connector.first].add(connector)
            self.sorted_components[connector.second].add(connector)

    def _find_strongest_bridge(self, start: int, total: int, available: Set[Connector]) -> int:
        best_total = total
        for connector in (x for x in self.sorted_components[start] if x in available):
            new_available = available - {connector}
            input_number = connector.second if connector.first == start else connector.first
            new_total = self._find_strongest_bridge(input_number, total + connector.sum, new_available)
            best_total = max(new_total, best_total)
        return best_total

    def find_strongest_bridge(self) -> int:
        return self._find_strongest_bridge(0, 0, self.connectors)

    def _find_longest_bridge(
        self,
        start: int,
        path: List[int],
        available: Set[Connector],
        longest_bridge: Optional[List[int]],
    ):
        connectors_to_try = [x for x in self.sorted_components[start] if x in available]
        if not connectors_to_try:
            if longest_bridge is None or len(path) > len(longest_bridge):
                longest_bridge = path
            if len(path) == len(longest_bridge) and sum(path) > sum(longest_bridge):
                longest_bridge = path
        else:
            for connector in connectors_to_try:
                new_available = available - {connector}
                new_path = path + [connector.sum]
                input_number = connector.second if connector.first == start else connector.first
                longest_bridge = self._find_longest_bridge(input_number, new_path, new_available, longest_bridge)

        return longest_bridge

    def find_longest_bridge(self):
        return self._find_longest_bridge(0, [], self.connectors, None)


def main():
    soup = ComponentSoup(read_data())
    print(f"Part one: {soup.find_strongest_bridge()}")
    print(f"Part two: {sum(soup.find_longest_bridge())}")


if __name__ == "__main__":
    start = time.monotonic()
    main()
    print(f"Time: {time.monotonic()-start}")
