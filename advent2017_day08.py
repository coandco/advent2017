import re
import time
from typing import Dict

from utils import read_data

COMPARISONS = {
    "<": lambda x, y: x < y,
    "<=": lambda x, y: x <= y,
    ">": lambda x, y: x > y,
    ">=": lambda x, y: x >= y,
    "==": lambda x, y: x == y,
    "!=": lambda x, y: x != y,
}
DIGITS = re.compile(r"[0-9-]+")
WORDS = re.compile(r"[a-z]+")
OPERATION = re.compile(r"[<>=!]+")


class Program:
    registers: Dict[str, int]
    all_time_max: int = 0

    def __init__(self, raw_program: str):
        self.registers = {}
        for line in raw_program.splitlines():
            register, operation, _, cmpreg = WORDS.findall(line)
            value, cmpvalue = (int(x) for x in DIGITS.findall(line))
            cmpop, *_ = OPERATION.findall(line)
            self.process_instruction(register, operation, value, cmpreg, cmpop, cmpvalue)

    def process_instruction(self, register: str, operation: str, value: int, cmpreg: str, cmpop: str, cmpvalue: int):
        register_value = self.registers.get(register, 0)
        if operation == "dec":
            value *= -1

        if COMPARISONS[cmpop](self.registers.get(cmpreg, 0), cmpvalue):
            register_value += value
            if register_value > self.all_time_max:
                self.all_time_max = register_value
            self.registers[register] = register_value


def main():
    program = Program(read_data())
    print(f"Part one: {max(program.registers.values())}")
    print(f"Part two: {program.all_time_max}")


if __name__ == "__main__":
    start = time.monotonic()
    main()
    print(f"Time: {time.monotonic()-start}")
