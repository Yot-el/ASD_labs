# Finding the number and composition of strongly connected components 
# in a given orgraph using depth-first search.

# Using Kosaraju algorithm

input_file = open("test_2.txt", "r")
graph_nodes_count = int(input_file.readline())
nodes = [[] for i in range(graph_nodes_count)]

while True:
    line = input_file.readline()
    if not line:
        break
    dots = line.split()
    nodes[int(dots[0]) - 1].append(int(dots[1]))

# DFS, marking the vertices.
# A vertice is considered "marked" when it is assigned a recursion exit time.

def dfs(i, time):
    time += 1
    used[i] = time
    for j in range(len(nodes[i])):
        if used[nodes[i][j]-1] == 0:
            time = dfs(nodes[i][j] - 1, time)
    used[i] = time
    return (time + 1)

used = [0 for i in range(graph_nodes_count)]
time = 0

for i in range(len(nodes)):
    if used[i] == 0:
        time = dfs(i, time)

# Inverting the edges of the graph
nodes_inverted = [[] for i in range(graph_nodes_count)] 
for i in range(len(nodes)):
    for j in range(len(nodes[i])):
        nodes_inverted[nodes[i][j] - 1].append(i+1)

# DFS in descending order of vertices labels
component_count = 0
components = []
used_inverted = []

def dfs_inverted(i):
    component.append(i + 1)
    used_inverted.append(i + 1)
    for j in range(len(nodes_inverted[i])):
        if (nodes_inverted[i][j]) not in used_inverted:
            dfs_inverted(nodes_inverted[i][j] - 1)

for i in range(len(used)):
    i = used.index(max(used))
    used[i] = 0
    component = []
    if i not in used_inverted:
        dfs_inverted(i)
        component_count += 1
    if component:
        components.append(component)

print(components, component_count)


