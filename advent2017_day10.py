import operator
import time
from functools import reduce
from itertools import zip_longest
from typing import Any, Iterable, List

from utils import read_data


def rotate(to_rotate: List[int], amount: int) -> List[int]:
    actual_amount = amount % len(to_rotate)
    return to_rotate[actual_amount:] + to_rotate[:actual_amount]


def reverse(to_reverse: List[int]):
    return to_reverse[::-1]


def grouper(iterable: Iterable, n: int, fillvalue: Any = None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def handle_instruction(queue_in: List[int], index: int, skip: int, length: int):
    rotated = rotate(queue_in, index)
    rotated[:length] = reverse(rotated[:length])
    return rotate(rotated, -index), index + length + skip, skip + 1


def get_reduced_hash(knot_hash: List[int]):
    reduced_hash = []
    for chunk in grouper(knot_hash, 16):
        xor_value = reduce(operator.xor, chunk, 0)
        reduced_hash.append(xor_value)
    return reduced_hash


def main():
    knot_hash = list(range(256))
    index = skip = 0
    for instruction in [int(x) for x in read_data().split(",")]:
        knot_hash, index, skip = handle_instruction(knot_hash, index, skip, instruction)
    print(f"Part one: {knot_hash[0] * knot_hash[1]}")

    p2_input = [ord(x) for x in read_data()] + [17, 31, 73, 47, 23]
    knot_hash = list(range(256))
    index = skip = 0
    for _ in range(64):
        for instruction in p2_input:
            knot_hash, index, skip = handle_instruction(knot_hash, index, skip, instruction)
    reduced_hash = get_reduced_hash(knot_hash)
    print(f"Part two: {''.join(format(x, '02x') for x in reduced_hash)}")


if __name__ == "__main__":
    start = time.monotonic()
    main()
    print(f"Time: {time.monotonic()-start}")
