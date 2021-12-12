from data_structures import Graph, Stack
input = open("day_12_input.txt", "r")
line = input.readline()

cave_graph = Graph()

cave_count = 0
while line != "":
    nodes = [x.strip() for x in line.split("-")]
    for node in nodes:
        if not cave_graph.has_vertex(node):
            cave_graph.add_vertex(node)
            cave_count += 1
    cave_graph.add_undirected_edge(nodes[0], nodes[1])
    line = input.readline()


def traverse_caves(cave_graph, visited, cave):
    label = cave_graph.Vertices[cave].get_label()
    if label == "end":
        return 1

    if visited.contains(cave):
        return 0

    if label.islower():
        visited.push(cave)
    next_caves = cave_graph.get_neighbors(label)
    x = 0
    for next_cave in next_caves:
        x += traverse_caves(cave_graph, visited, next_cave)
    if label.islower():
        visited.pop()
    return x


visited = Stack()
path_count = traverse_caves(cave_graph, visited, cave_graph.get_index("start"))
print(path_count)
