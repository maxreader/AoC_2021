import data_structures as ds
import numpy as np
input = open("day_13_input.txt", "r")
line = input.readline()

max_x = 0
max_y = 0

coordinates = []
while line != "\n":
    point = line.split(',')
    x = int(point[0])
    y = int(point[1])
    max_x = max(max_x, x)
    max_y = max(max_y, y)
    coordinates.append([int(point[0]), int(point[1])])
    line = input.readline()

line = input.readline().strip()


while line != "":

    foldline = int(line[13:])
    if line[11] == "y":
        for i, point in enumerate(coordinates):
            if point[1] > foldline:
                coordinates[i] = [point[0], 2*foldline - point[1]]
    else:
        for i, point in enumerate(coordinates):
            if point[0] > foldline:
                coordinates[i] = [2*foldline - point[0], point[1]]
    line = input.readline().strip()


output = [["." for x in range(max_x+1)] for y in range(max_y+1)]

for point in coordinates:
    output[point[1]][point[0]] = "#"

count = 0
for row in output:
    for i in row:
        if i == "#":
            count += 1
print(count)

for row in output[:7]:
    print(row[:8*5])
