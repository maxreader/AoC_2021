from timeit import default_timer as timer

input = open("day_8_input.txt", "r")
line = input.readline()
data = []
while line != "":
    parts = line.split("|")
    parts[0] = parts[0].split()
    parts[1] = parts[1].split()
    data.append(parts)
    line = input.readline()

start = timer()
lengths = {2: 1, 3: 7, 4: 4, 7: 8}


def translate_line(outputs):
    digitDict = {}
    second_pass = []
    third_pass = []
    for output in outputs:
        length = len(output)
        if length in lengths.keys():
            digitDict[lengths[length]] = output
        elif length == 5:
            second_pass.append(output)
        else:
            third_pass.append(output)

    for output in second_pass:
        length = len(output)
        if all(x in output for x in digitDict[1]):
            digitDict[3] = output
        elif all(x in output for x in [x for x in digitDict[4] if x not in digitDict[1]]):
            digitDict[5] = output
        else:
            digitDict[2] = output
    for output in third_pass:
        if all(x in output for x in digitDict[5]):
            if all(x in output for x in digitDict[1]):
                digitDict[9] = output
            else:
                digitDict[6] = output
        else:
            digitDict[0] = output
    return {x: y for y, x in digitDict.items()}


total = 0
for entry in data:
    key = entry[0]
    points = [None]*10
    for i, point in enumerate(key):
        lst = [char for char in point]
        lst.sort()
        points[i] = "".join(lst)
    digitDict = translate_line(points)

    number = ""
    for output in entry[1]:
        output = [char for char in output]
        output.sort()
        digit = digitDict["".join(output)]
        number += str(digit)
    total += int(number)
print(total)
end = timer()
print(end-start)
