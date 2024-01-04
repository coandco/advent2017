import re
import time
from collections import defaultdict
from typing import Dict, List, NamedTuple, Tuple

from utils import read_data

DIGITS = re.compile(r"[0-9-]+")


class Substate(NamedTuple):
    value: int
    offset: int
    next: str

    @staticmethod
    def from_str(raw_substate: List[str]) -> "Substate":
        value = int(raw_substate[0][-2])
        offset = 1 if raw_substate[1].rsplit(maxsplit=1)[1] == "right." else -1
        next = raw_substate[2][-2]
        return Substate(value, offset, next)


class State(NamedTuple):
    name: str
    substates: Tuple[Substate, Substate]

    @staticmethod
    def from_str(raw_state: str) -> "State":
        lines = raw_state.splitlines()
        name = lines[0][-2]
        substates = (Substate.from_str(lines[2:5]), Substate.from_str(lines[6:9]))
        return State(name, substates)


class TuringMachine:
    start_state: str
    cur_loc: int
    diag_after: int
    rules: Dict[str, State]
    tape: Dict[int, int]

    def __init__(self, raw_instructions: str):
        preamble, *raw_states = raw_instructions.split("\n\n")
        lines = preamble.splitlines()
        self.diag_after, *_ = (int(x) for x in DIGITS.findall(lines[1]))
        self.rules = {(state := State.from_str(x)).name: state for x in raw_states}
        self.start_state = lines[0][-2]
        self.cur_loc = 0
        self.tape = defaultdict(int)

    def run(self) -> int:
        tape = defaultdict(int)
        state = self.start_state
        loc = 0
        for i in range(self.diag_after):
            current_rule = self.rules[state]
            current_value = tape[loc]
            tape[loc] = current_rule.substates[current_value].value
            loc += current_rule.substates[current_value].offset
            state = current_rule.substates[current_value].next
        return sum(tape.values())


def main():
    machine = TuringMachine(read_data())
    print(f"Part one: {machine.run()}")


if __name__ == "__main__":
    start = time.monotonic()
    main()
    print(f"Time: {time.monotonic()-start}")
