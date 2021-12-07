import numpy as np
input = open("day_3_input.txt", "r")
input = input.read().split("\n")

count = np.array([0]*12)
for i in input:
    if i == '':
        break
    j = np.array([int(x) for x in i], dtype=int)*2 - 1
    count += j

count = (count/abs(count)+1)/2
bits = [int(i) for i in count]
eps = sum([b << (11-i) for i, b in enumerate([int(i) for i in count])])
allbits = int("111111111111", 2)
gamma = eps ^ allbits
print(eps*gamma)
