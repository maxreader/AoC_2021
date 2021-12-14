import string
from collections import Counter
import data_structures as ds
import numpy as np
input = open("day_14_input.txt", "r")
line = input.readline()

polymer = line.strip()
line = input.readline()
line = input.readline()

polymerDict = {}
while line != "":
    polymerDict[line[:2]] = line[-2:-1]
    line = input.readline()

letterCount = {n: 0 for n in string.ascii_uppercase}
for letter in polymer:
    if letterCount[letter]:
        letterCount[letter] += 1
    else:
        letterCount[letter] = 1


for _ in range(40):
    newPolymer = ""
    for i, letter in enumerate(polymer):
        newPolymer += letter
        if i+1 == len(polymer):
            break
        nextLetter = polymer[i+1]
        insertion = polymerDict[letter+nextLetter]
        newPolymer += insertion
        letterCount[insertion] += 1
    polymer = newPolymer
# print(polymer)

letterMax = 0
letterMin = 1000000

for k, v in letterCount.items():
    if v > letterMax:
        letterMax = v
    elif v < letterMin and v != 0:
        letterMin = v

print(letterMax-letterMin)
