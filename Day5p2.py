import numpy as np
input = open("day_5_input.txt", "r")

line = input.readline()

vents = np.array([[0 for x in range(1000)] for y in range(1000)])
while line != "":
    i = line.split()
    x1, y1 = map(int, i[0].split(","))
    x2, y2 = map(int, i[2].split(","))

    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2)+1):
            vents[x1][y] += 1
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2)+1):
            vents[x][y1] += 1
    else:
        dx = 1 if (x2 > x1) else -1
        dy = 1 if (y2 > y1) else -1

        for k in range(1+abs(x2-x1)):
            vents[x1+dx*k][y1+dy*k] += 1

    line = input.readline()

count = np.count_nonzero(vents > 1)
print(count)
