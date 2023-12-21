from utils import read_data
import time


def main():
    data = read_data().strip()
    length = len(data)
    part_one = [int(data[i]) for i in range(length) if data[i] == data[(i+1) % length]]
    part_two = [int(data[i]) for i in range(length) if data[i] == data[(i + length//2) % length]]
    print(f"Part one: {sum(part_one)}")
    print(f"Part two: {sum(part_two)}")


if __name__ == '__main__':
    start = time.monotonic()
    main()
    print(f"Time: {time.monotonic()-start}")