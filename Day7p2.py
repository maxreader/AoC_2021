import numpy as np
input = open("day_7_input.txt", "r")
raw = np.array([int(x) for x in input.readline().split(",")])

raw = np.sort(raw)


def tri_sum(n):
    return n*(n+1)/2


fuel = min((sum((tri_sum(abs(x-y)) for x in raw))
            for y in range(max(raw))))


print(fuel)
