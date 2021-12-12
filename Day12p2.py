from data_structures import Graph
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


def traverse_caves(cave_graph, cave, double_visit):
    vertex = cave_graph.Vertices[cave]
    label = vertex.get_label()
    if label == "end":
        return 1

    if vertex.visited:
        x = 0
        if not double_visit and label != "start":
            for next_cave in cave_graph.get_neighbors(label):
                x += traverse_caves(cave_graph,
                                    next_cave, True)
        return x

    if label.islower():
        vertex.visited = True
    x = 0
    for next_cave in cave_graph.get_neighbors(label):
        x += traverse_caves(cave_graph, next_cave, double_visit)
    if label.islower():
        vertex.visited = False
    return x


path_count = traverse_caves(
    cave_graph, cave_graph.get_index("start"), False)
print(path_count)
