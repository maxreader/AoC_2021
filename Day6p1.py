from timeit import default_timer as timer
import numpy as np
start = timer()


class Link (object):
    def __init__(self, data, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous


class CircularList(object):
    # Constructor
    def __init__(self):
        self.first = None

    # Insert an element (value) in the list
    def insert(self, data):
        new_link = Link(data)
        if self.first == None:
            self.first = new_link
            new_link.next = new_link
            new_link.previous = new_link
        else:
            new_link.next = self.first
            new_link.previous = self.first.previous
            self.first.previous.next = new_link
            self.first.previous = new_link

    def sum(self):
        first = self.first
        current = first.next
        total = first.data
        while current != first:
            total += current.data
            current = current.next
        return total

        # Return a string representation of a Circular List
    def __str__(self):
        first = self.first
        output = ''
        output += str(first.data) + "\n"
        current = first.next
        while current != first:
            output += str(current.data) + "\n"
            current = current.next
        return output


input = open("day_6_input.txt", "r")
raw = np.array([int(x) for x in input.readline().split(",")])
fish = np.concatenate([[0], np.unique(raw, return_counts=True)[1], [0, 0, 0]])
fishCircle = CircularList()
for i in fish:
    fishCircle.insert(i)
readyFish = fishCircle.first
tiredFish = readyFish.previous.previous
for i in range(256):
    tiredFish.data += readyFish.data
    readyFish = readyFish.next
    tiredFish = tiredFish.next
print(fishCircle.sum())
end = timer()
print(end-start)
