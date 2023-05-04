input_file = open("file", "r")
graph_nodes_count = int(input_file.readline())
nodes = [[] for i in range(graph_nodes_count)]

while True:
    line = input_file.readline()
    if not line:
        break
    dots = line.split()
    nodes[int(dots[0]) - 1].append(int(dots[1]))

print(nodes)


used = []
queue = []
components_count = 0
components = []

def bfs(i):
    used.append(i)
    component.append(i + 1)
    for j in range(len(nodes[i])):
        related_node = nodes[i][j] - 1
        if related_node not in used and related_node not in queue:
            queue.append(related_node)
    queue.pop(0)

for i in range(len(nodes)):
    if i not in used:
        components_count += 1
        component = []
        queue.append(i)
        while len(queue) != 0:
            bfs(queue[0])
        components.append(component)


print(components, components_count)
    