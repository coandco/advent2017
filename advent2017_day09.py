import re
import time

from utils import read_data


def score(stream):
    depth = 0
    total = 0
    for char in stream:
        if char == "{":
            depth += 1
        elif char == "}":
            total += depth
            depth -= 1
        else:  # Probably a comma, safe to ignore
            pass
    return total


def count_garbage(stream):
    garbage_list = re.findall(r"<([^>]*)>", stream)
    return sum(len(x) for x in garbage_list)


def main():
    pzl_input = read_data()
    notted = re.sub(r"!.", "", pzl_input)
    degarbaged = re.sub(r"<[^>]*>", "", notted)
    print(f"Part one: {score(degarbaged)}")
    print(f"Part two: {count_garbage(notted)}")


if __name__ == "__main__":
    start = time.monotonic()
    main()
    print(f"Time: {time.monotonic()-start}")
