from utils import read_data
import time


def gen_value(next: int, factor: int, multiple=1):
    while True:
        next = (next * factor) % 2147483647
        if next % multiple == 0:
            yield next & 0xffff


def main():
    starts = [int(x.split()[-1]) for x in read_data().splitlines()]
    gen_a, gen_b = gen_value(starts[0], 16807), gen_value(starts[1], 48271)
    print(f"Part one: {sum(next(gen_a) == next(gen_b) for _ in range(40_000_000))}")
    gen_a, gen_b = gen_value(starts[0], 16807, 4), gen_value(starts[1], 48271, 8)
    print(f"Part two: {sum(next(gen_a) == next(gen_b) for _ in range(5_000_000))}")
    

if __name__ == '__main__':
    start = time.monotonic()
    main()
    print(f"Time: {time.monotonic()-start}")
