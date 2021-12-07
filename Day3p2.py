import numpy as np
input = open("day_3_input.txt", "r")
input = input.read().split("\n")

l = len(input)
bits = np.zeros((len(input)-1, 12), dtype=int)
for i, line in enumerate(input):
    if line == '':
        break
    bits[i] = np.array([int(x)*2 - 1 for x in line], dtype=int)

# m = 1, most common bit (Oxygen), v.v.


def sort(data, n, m):
    if len(data) == 1 or n == 12:
        return data[0, :]
    else:
        s = sum(data[:, n])
        mode = 2*m - 1 if s >= 0 else 1-2*m
        filteredData = data[data[:, n] == mode]
        return sort(filteredData, n+1, m)


O2_rating = sort(bits, 0, 1)
O2_rating = sum([b << (11-i)
                 for i, b in enumerate([int((i+1)/2) for i in O2_rating])])
CO2_rating = sort(bits, 0, 0)
CO2_rating = sum([b << (11-i)
                  for i, b in enumerate([int((i+1)/2) for i in CO2_rating])])
print(O2_rating*CO2_rating)
