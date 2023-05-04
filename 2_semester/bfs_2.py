input_file = open("file", "r")
graph_nodes_count = int(input_file.readline())
nodes = [[] for i in range(graph_nodes_count)]

while True:
    line = input_file.readline()
    if not line:
        break
    dots = line.split()
    nodes[int(dots[0]) - 1].append(int(dots[1]))


used = []
queue = []
main_node = int(input()) - 1 #От какого элемента графа надо просчитать кратчайшие пути
queue.append(main_node)



short_path = [[] for i in range(graph_nodes_count)] #Список кратчайших путей
short_path[main_node].append(main_node + 1)

def bfs(i):
    used.append(i)
    for j in range(len(nodes[i])):
        related_node = nodes[i][j] - 1
        if related_node not in used and related_node not in queue:
            check_path(related_node, i) #Считаем кратчайший путь в вершину
            queue.append(related_node)
    queue.pop(0)


def check_path(cur_node, prev_node):
    if cur_node != main_node:
        short_path[cur_node] = short_path[prev_node].copy()
        short_path[cur_node].append(cur_node + 1)


while len(queue) != 0:
    bfs(queue[0])

for i in range(len(short_path)):
    print(f'{i+1}: {short_path[i]}')
