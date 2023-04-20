graph = []
graph = [
        [0, 7, 0, 0, 0, 5, 0],
        [7, 0, 8, 7, 0, 9, 0],
        [0, 8, 0, 5, 0, 0, 0],
        [0, 7, 5, 0, 8, 15, 9],
        [0, 0, 0, 8, 0, 6, 11],
        [5, 9, 0, 15, 6, 0, 0],
        [0, 0, 0, 9, 11, 0, 0]
        ]


def findEdges(current_node, edges, used, graph):
    for i in range(len(graph[current_node])):
        weight = graph[current_node][i]
        if weight != 0 and i not in used:
            edges.append([current_node, i, weight])

def findMin(edges, used, res_tree):
    min_edge = [0, 0, 9999]
    for edge in edges:
        if edge[0] not in used or edge[1] not in used: # Если у нас не образуется цикл (т.е. обе вершины уже использованы)
            if edge[2] < min_edge[2]: # Сравниваем веса ребер и выбираем минимальное
                min_edge = edge.copy()

    res_tree.append(min_edge)
    if min_edge[0] in used:
        return min_edge[1]
    else:
        return min_edge[0]


def primAlgo(graph, i):
    used = []                           # Использованные вершины
    edges = []                          # Рассматриваемые ребра
    res_tree = []                       # Минимальное остовное дерево

    current_node = 0
    used.append(current_node)

    while len(used) != i:
        findEdges(current_node, edges, used, graph) # Находим все ребра из текущей вершины и записываем их в edges
        next_node = findMin(edges, used, res_tree) # Находим ближайшую вершину к любой из использованных
        current_node = next_node             # Переходим к следующей вершине
        used.append(current_node)          # Убираем текущую вершину из еще не использованных

    return res_tree

# 7 - кол-во вершин графа
res = primAlgo(graph, 7)
print('Prim tree is:')
for edge in res:
    print(f'Edge: {edge[0]} - {edge[1]}, weight: {edge[2]}')
