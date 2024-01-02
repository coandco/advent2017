import time

from utils import read_data


class Link:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class CircularLinkedList:
    def __init__(self, initial_element):
        self.head = Link(initial_element, None)
        self.head.next = self.head
        self.cur_index = self.head
        self.length = 1

    def advance(self, amount):
        for _ in range(amount):
            self.cur_index = self.cur_index.next

    def insert_after(self, data):
        new_link = Link(data, self.cur_index.next)
        self.cur_index.next = new_link
        self.cur_index = new_link
        self.length += 1


class FauxCircularLinkedList:
    def __init__(self):
        self.length = 1
        self.head = Link(None)
        self.head.next = self.head
        self.cur_index = self.head
        self.faux_index = 0

    def advance(self, amount):
        self.faux_index = (self.faux_index + amount) % self.length

    def insert_after(self, data):
        if self.faux_index == 0:
            self.head.data = data
        self.length += 1
        self.faux_index += 1


def spin(linked_list, current_max: int, step: int):
    linked_list.advance(step)
    new_max = current_max + 1
    linked_list.insert_after(new_max)
    return new_max


def main():
    spin_list = CircularLinkedList(0)
    spin_max = 0
    steps = int(read_data())
    for i in range(2017):
        spin_max = spin(spin_list, spin_max, steps)

    print(f"Part one: {spin_list.cur_index.next.data}")

    spin_list = FauxCircularLinkedList()
    spin_max = 0
    for i in range(50000000):
        spin_max = spin(spin_list, spin_max, steps)

    print(f"Part two: {spin_list.head.next.data}")


if __name__ == "__main__":
    start = time.monotonic()
    main()
    print(f"Time: {time.monotonic()-start}")
