# Finding the number and composition of connectivity components 
# in a given graph using depth-first search

def dfs(i):
    component.append(i + 1)
    used.append(i + 1)
    for j in range(len(nodes[i])):
        if (nodes[i][j]) not in used:
            dfs(nodes[i][j] - 1)

input_file = open("test.txt", "r")
graph_nodes_count = int(input_file.readline())
nodes = [[] for i in range(graph_nodes_count)]

while True:
    line = input_file.readline()
    if not line:
        break
    dots = line.split()
    nodes[int(dots[0]) - 1].append(int(dots[1]))

used = []
component_count = 0
components = []

for i in range(len(nodes)):
    component = []
    if i not in used:
        dfs(i)
        component_count += 1
    if component:
        components.append(component)

print(components, component_count)
    