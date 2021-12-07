import numpy as np
input = open("day_2_input.txt", "r")
input = input.read().split("\n")


def directions(x): return {"forward": np.array([1, x, 0]),
                           "up": np.array([0, 0, 1]),
                           "down": np.array([0, 0, -1])}


# x, y, aim
coord = np.array([0, 0, 0])
for i in input:
    if i == '':
        break
    j = i.split()
    delta = int(j[1])*directions(coord[2])[j[0]]
    coord += delta

print(coord[0]*coord[1])
