from timeit import default_timer as timer
start = timer()
input = open("day_9_input.txt", "r")
data = []
line = input.readline()
while line != "":
    data.append([int(char) for char in line if char.isdigit()])
    line = input.readline()

height = len(data)
width = len(data[0])

total_risk = 0
for i, row in enumerate(data):
    for j, n in enumerate(row):
        if n == 9:
            continue
        above = data[i-1][j] if i > 0 else 10
        below = data[i+1][j] if i < height-1 else 10
        left = data[i][j-1] if j > 0 else 10
        right = data[i][j+1] if j < width-1 else 10
        if not any(x < n for x in (above, below, left, right)):
            total_risk += n + 1

print(total_risk)
end = timer()
print(end-start)
