from timeit import default_timer as timer
start = timer()
input = open("day_10_input.txt", "r")
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


openers = [x for x in "([{<"]
closers = [x for x in ")]}>"]
points = [1, 2, 3, 4]

sums = []
while line != "":
    stack = Stack()
    thisSum = 0
    invalid = False
    for char in line:
        if char in openers:
            stack.push(char)
        elif char in closers:
            i = closers.index(char)
            if openers.index(stack.peek()) != i:
                invalid = True
                break
            else:
                stack.pop()
    if not invalid:
        while not stack.is_empty():
            previous = stack.pop()
            i = openers.index(previous)
            thisSum = thisSum*5 + points[i]
        sums.append(thisSum)
    line = input.readline()
sums.sort()
print(sums[(len(sums)-1)//2])
end = timer()
print(end - start)
