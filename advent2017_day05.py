from utils import read_data
import time


def main():
    jump_list = [int(x) for x in read_data().split("\n")]

    p1_list = jump_list.copy()
    current_index = 0
    steps_taken = 0

    while 0 <= current_index < len(p1_list):
        current_jump = p1_list[current_index]
        p1_list[current_index] += 1
        current_index += current_jump
        steps_taken += 1

    print(f"Part one: {steps_taken}")

    current_index = 0
    steps_taken = 0

    while 0 <= current_index < len(jump_list):
        current_jump = jump_list[current_index]
        if current_jump >= 3:
            jump_list[current_index] -= 1
        else:
            jump_list[current_index] += 1
        current_index += current_jump
        steps_taken += 1

    print(f"Part two: {steps_taken}")


if __name__ == '__main__':
    start = time.monotonic()
    main()
    print(f"Time: {time.monotonic()-start}")
