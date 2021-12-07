import numpy as np
input = open("day_1_input.txt", "r")
input_list = np.fromstring(input.read(), dtype="int", sep="\n")
n_plus_one = np.roll(input_list, 1)
difference = (input_list-n_plus_one)[1:]
count = np.sum(difference >= 0)
print(count)
