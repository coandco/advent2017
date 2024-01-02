import string
import time
from collections import deque
from typing import Callable, Deque, Dict, Iterable, List, Optional

from utils import read_data


class Assembly:
    registers: Dict[str, int]
    ops: Dict[str, Callable]
    last_sound: Optional[int]
    program: List[List[str]]
    program_counter: int

    def __init__(self, raw_program: str):
        self.program = [x.split() for x in raw_program.splitlines()]
        self.registers = {x: 0 for x in string.ascii_lowercase}
        self.last_sound = None
        self.program_counter = 0
        self.ops = {
            "snd": self.do_snd,
            "rcv": self.do_rcv,
            "set": self.do_set,
            "add": self.do_add,
            "mul": self.do_mul,
            "mod": self.do_mod,
            "jgz": self.do_jgz,
        }

    def run(self) -> int:
        while 0 <= self.program_counter < len(self.program):
            op, *args = self.program[self.program_counter]
            if op == "rcv" and self.registers[args[0]] != 0:
                break
            self.ops[op](*args)

        return self.last_sound

    def do_snd(self, reg: str):
        self.last_sound = self.registers[reg]
        self.program_counter += 1

    def do_set(self, reg: str, value: str):
        value = self.registers[value] if value in self.registers else int(value)
        self.registers[reg] = value
        self.program_counter += 1

    def do_add(self, reg: str, value: str):
        value = self.registers[value] if value in self.registers else int(value)
        self.registers[reg] += value
        self.program_counter += 1

    def do_mul(self, reg: str, value: str):
        value = self.registers[value] if value in self.registers else int(value)
        self.registers[reg] *= value
        self.program_counter += 1

    def do_mod(self, reg: str, value: str):
        value = self.registers[value] if value in self.registers else int(value)
        self.registers[reg] %= value
        self.program_counter += 1

    def do_jgz(self, reg: str, value: str):
        reg = self.registers[reg] if reg in self.registers else int(value)
        value = self.registers[value] if value in self.registers else int(value)
        self.program_counter += value if reg > 0 else 1

    def do_rcv(self, reg: str):
        raise NotImplementedError


class MultiAssembly(Assembly):
    input_queue: Deque[int]
    halted: bool = False
    num_sent: int = 0

    def __init__(self, raw_program: str, instance_num: int):
        super().__init__(raw_program)
        self.registers["p"] = instance_num
        self.input_queue = deque()

    def run(self) -> Iterable[int]:
        while 0 <= self.program_counter < len(self.program):
            op, *args = self.program[self.program_counter]
            if op == "snd":
                yield self.registers[args[0]]
            elif op == "rcv" and len(self.input_queue) == 0:
                self.halted = True
                return
            self.ops[op](*args)

    def do_snd(self, reg: str):
        self.num_sent += 1
        self.program_counter += 1

    def do_rcv(self, reg: str):
        value = self.input_queue.popleft()
        self.registers[reg] = value
        self.program_counter += 1


def main():
    raw_program = read_data()
    assembly = Assembly(raw_program)
    print(f"Part one: {assembly.run()}")
    assemblies = [MultiAssembly(raw_program, 0), MultiAssembly(raw_program, 1)]
    cur_instance = 0
    while not all(x.halted for x in assemblies):
        sent_values = list(assemblies[cur_instance].run())
        if sent_values:
            assemblies[not cur_instance].input_queue.extend(sent_values)
            assemblies[not cur_instance].halted = False
        cur_instance = not cur_instance
    print(f"Part two: {assemblies[1].num_sent}")


if __name__ == "__main__":
    start = time.monotonic()
    main()
    print(f"Time: {time.monotonic()-start}")
