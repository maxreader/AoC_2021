import numpy as np
input = open("day_2_input.txt", "r")
input = input.read().split("\n")

directions = {"forward": np.array([1, 0]),
              "up": np.array([0, 1]),
              "down": np.array([0, -1])}

coord = np.array([0, 0])
for i in input:
    if i == '':
        break
    j = i.split()
    direction = directions[j[0]]
    displacement = direction * int(j[1])
    coord += displacement

print(coord[0]*coord[1])
