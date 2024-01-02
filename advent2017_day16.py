from typing import List

from utils import read_data
import time


def spin(line: List[str], number: int):
    return line[-number:] + line[:-number]


def exchange(line: List[str], index_one: int, index_two: int):
    line[index_one], line[index_two] = line[index_two], line[index_one]
    return line


def manual_dance(line: List[str], moves: str):
    new_line = list(line)
    for instruction in moves.split(","):
        if instruction.startswith("s"):
            new_line = spin(new_line, int(instruction[1:]))
        elif instruction.startswith("x"):
            index_one, index_two = [int(x) for x in instruction[1:].split("/")]
            new_line = exchange(new_line, index_one, index_two)
        elif instruction.startswith("p"):
            index_one, index_two = [new_line.index(x) for x in instruction[1:].split("/")]
            new_line = exchange(new_line, index_one, index_two)
    return new_line


def main():
    original_line = list("abcdefghijklmnop")
    moves = read_data()
    line = manual_dance(original_line, moves)

    print(f"Part one: {''.join(line)}")

    # Find some number of permutations that returns the list to its original state
    current_line = list(original_line)
    cycle_length = 0

    while True:
        current_line = manual_dance(current_line, moves)
        cycle_length += 1
        if current_line == original_line:
            break

    # Now we only need to do 1000000000 % cycle_length iterations to calculate
    current_line = list(original_line)
    for i in range(1000000000 % cycle_length):
        current_line = manual_dance(current_line, moves)

    print(f"Part two: {''.join(current_line)}")


if __name__ == "__main__":
    start = time.monotonic()
    main()
    print(f"Time: {time.monotonic()-start}")
