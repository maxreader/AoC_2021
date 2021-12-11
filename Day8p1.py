from timeit import default_timer as timer
start = timer()
input = open("day_8_input.txt", "r")
line = input.readline()
data = []
while line != "":
    parts = line.split("|")
    parts[0] = parts[0].split()
    parts[1] = parts[1].split()
    data.append(parts)
    line = input.readline()


lengths = {2: 1, 3: 7, 4: 4, 7: 8}
count = 0
for entry in data:
    output = entry[1]
    for value in output:
        length = len(value)
        if length in lengths:
            count += 1
print(count)
end = timer()
print(end-start)
