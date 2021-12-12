import numpy as np
input = open("day_11_input.txt", "r")
line = input.readline()

data = []
while line != "":
    data.append([int(char) for char in line if char != "\n"])
    line = input.readline()

data = np.array(data)
