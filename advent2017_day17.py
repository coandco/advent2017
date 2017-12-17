INPUT = 312


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
        for _ in xrange(amount):
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


def spin(linked_list, current_max, step):
    linked_list.advance(step)
    new_max = current_max + 1
    linked_list.insert_after(new_max)
    return new_max


spin_list = CircularLinkedList(0)
spin_max = 0
for i in xrange(2017):
    spin_max = spin(spin_list, spin_max, INPUT)
    #print("Spin %d resulted in array %r" % (i, [x for x in spin_list]))

print("Value immediately after last insert for v1: %d" % spin_list.cur_index.next.data)

spin_list = FauxCircularLinkedList()
spin_max = 0
for i in xrange(50000000):
    spin_max = spin(spin_list, spin_max, INPUT)
    if i % 500000 == 0:
        print("Reached %d" % i)

print("Value immediately after 0: %d" % spin_list.head.next.data)
