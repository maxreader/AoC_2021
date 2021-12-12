import numpy as np
input = open("day_11_input.txt", "r")
line = input.readline()

data = []
while line != "":
    data.append([int(char) for char in line if char != "\n"])
    line = input.readline()

data = np.array(data)
flashes = 0


def visit(flashed, i, j):
    if not flashed[i][j]:
        data[i][j] += 1
        if data[i][j] > 9:
            global flashes
            flashes += 1
            flashed[i][j] = True
            data[i][j] = 0
            for n in [-1, 0, 1]:
                for m in [-1, 0, 1]:
                    x = i+n
                    y = j+m
                    if (x == i and y == j) or x < 0 or y < 0 or x > 9 or y > 9:
                        continue
                    visit(flashed, x, y)


for _ in range(100):
    flashed = np.zeros((10, 10), dtype=bool)
    for i in range(10):
        for j in range(10):
            visit(flashed, i, j)


print(flashes)
