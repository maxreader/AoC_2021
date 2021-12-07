import numpy as np
input = open("day_7_input.txt", "r")
raw = np.array([int(x) for x in input.readline().split(",")])

raw = np.sort(raw)
total = np.sum(raw)
delta = 1000
l = len(raw)
if l % 2:
    x = l/2
    print(raw[x])
else:
    x = l//2
    print(np.sum(np.abs(raw-raw[x])))
    print(raw[x])

    print(np.sum(np.abs(raw-raw[x+1])))
    print(raw[x+1])
