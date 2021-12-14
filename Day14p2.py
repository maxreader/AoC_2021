input = open("day_14_input.txt", "r")
line = input.readline()

polymer = line.strip()
line = input.readline()
line = input.readline().strip()

letterIndex = []
polymerLookup = [[0 for x in range(26)] for y in range(26)]

while line != "":
    char1 = line[0]
    char2 = line[1]
    result = line[-1]
    if char1 not in letterIndex:
        letterIndex.append(char1)
    if char2 not in letterIndex:
        letterIndex.append(char2)
    if result not in letterIndex:
        letterIndex.append(result)
    y = letterIndex.index(char1)
    x = letterIndex.index(char2)
    z = letterIndex.index(result)
    polymerLookup[y][x] = z
    line = input.readline().strip()

numberOfLetters = len(letterIndex)


currentPairs = [[0 for x in range(numberOfLetters)]
                for y in range(numberOfLetters)]

for i in range(len(polymer)-1):
    first = polymer[i]
    second = polymer[i+1]
    y = letterIndex.index(first)
    x = letterIndex.index(second)
    currentPairs[y][x] += 1

for _ in range(40):
    newPairs = [[0 for x in range(numberOfLetters)]
                for y in range(numberOfLetters)]
    for y, row in enumerate(currentPairs):
        for x, pair in enumerate(row):
            if pair > 0:
                z = polymerLookup[y][x]
                newPairs[y][z] += pair
                newPairs[z][x] += pair
    currentPairs = newPairs

letterCount = [sum(row) for row in currentPairs]
letterCount[letterIndex.index(polymer[-1])] += 1

letterMax = max(letterCount)
letterMin = min(letterCount)

print(letterMax-letterMin)
