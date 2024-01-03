import time
from math import sqrt

from advent2017_day18 import Assembly
from utils import read_data


class Coprocessor(Assembly):
    num_mul: int = 0

    def __init__(self, raw_program: str, debug: bool = False):
        super().__init__(raw_program)
        self.ops = {"set": self.do_set, "sub": self.do_sub, "mul": self.do_mul, "jnz": self.do_jnz}
        self.registers = {x: 0 for x in "abcdefgh"}
        if debug:
            self.registers["a"] = 1

    def do_jnz(self, reg: str, value: str):
        reg = self.registers[reg] if reg in self.registers else int(reg)
        value = self.registers[value] if value in self.registers else int(value)
        self.program_counter += 1 if reg == 0 else value

    def do_sub(self, reg: str, value: str):
        value = self.registers[value] if value in self.registers else int(value)
        self.registers[reg] -= value
        self.program_counter += 1

    def do_mul(self, reg: str, value: str):
        value = self.registers[value] if value in self.registers else int(value)
        self.registers[reg] *= value
        self.num_mul += 1
        self.program_counter += 1

    def run(self) -> int:
        while 0 <= self.program_counter < len(self.program):
            op, *args = self.program[self.program_counter]
            self.ops[op](*args)
        return self.num_mul


def is_prime(n: int) -> bool:
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def main():
    coprocessor = Coprocessor(read_data())
    print(f"Part one: {coprocessor.run()}")
    num_primes = 0
    start = (int(coprocessor.program[0][2]) * 100) + 100000
    for i in range(start, start + 17001, 17):
        if not is_prime(i):
            num_primes += 1
    print(f"Part two: {num_primes}")


if __name__ == "__main__":
    start = time.monotonic()
    main()
    print(f"Time: {time.monotonic()-start}")
