input = open("day_10_input.txt", "r")
data = []
line = input.readline()


class Stack (object):
    def __init__(self):
        self.stack = []

    # add an item to the top of the stack
    def push(self, item):
        self.stack.append(item)

    # remove an item from the top of the stack
    def pop(self):
        return self.stack.pop()

    # check the item on the top of the stack
    def peek(self):
        return self.stack[-1]

    # check if the stack if empty
    def is_empty(self):
        return (len(self.stack) == 0)

    # return the number of elements in the stack
    def size(self):
        return (len(self.stack))


brackets = {")": "(", "}": "{", "}": "{", ">": "<"}
openers = [x for x in "([{<"]
closers = [x for x in ")]}>"]
points = [3, 57, 1197, 25137]

sum = 0
while line != "":
    stack = Stack()
    for char in line:
        if char in openers:
            stack.push(char)
        elif char in closers:
            i = closers.index(char)
            if openers.index(stack.peek()) != i:
                sum += points[i]
                break
            else:
                stack.pop()
    line = input.readline()
print(sum)
