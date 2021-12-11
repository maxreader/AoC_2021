# from timeit import default_timer as timer
# start = timer()
input = open("day_9_input.txt", "r")
data = []
line = input.readline()
while line != "":
    data.append([int(char) for char in line if char != "\n"])
    line = input.readline()
# input_time = timer()
# print(input_time-start)
height = len(data)
width = len(data[0])

low_points = []
for i, row in enumerate(data):
    for j, n in enumerate(row):
        if n == 9:
            continue
        above = data[i-1][j] if i > 0 else 10
        below = data[i+1][j] if i < height-1 else 10
        left = data[i][j-1] if j > 0 else 10
        right = data[i][j+1] if j < width-1 else 10
        if not any(x < n for x in (above, below, left, right)):
            low_points.append((i, j))

visited = [[False for x in range(width)] for y in range(height)]
sizes = []

# mid = timer()
# print(mid - start)


def find_basin(point):
    (i, j) = point
    if visited[i][j]:
        return 0
    elif data[i][j] == 9:
        visited[i][j] = True
        return 0
    else:
        visited[i][j] = True
        neighbors = ((max(i-1, 0), j), (i, max(j-1, 0)),
                     (min(i+1, height-1), j), (i, min(j+1, width-1)))
        return 1 + sum(find_basin(x) for x in neighbors)


for point in low_points:
    sizes.append(find_basin(point))

sizes.sort()

prod = sizes[-1]*sizes[-2]*sizes[-3]
print(prod)
# end = timer()
# print(end-start)
