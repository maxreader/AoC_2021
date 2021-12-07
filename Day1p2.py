import numpy as np
input = open("day_1_input.txt", "r")
input_list = np.fromstring(input.read(), dtype="int", sep="\n")
n_plus_3 = np.roll(input_list, 3)
difference = (input_list-n_plus_3)[3:]
count = np.sum(difference > 0)
print(count)
