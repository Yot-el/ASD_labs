graph = []

with open('adjacency_matrix.txt') as file:
    i = 0
    for line in file:
        Edges = list(map(int, line.split()))
        for j in range(0, len(Edges)):
            if i == j:
                continue

            elif Edges[j] != 0:
                edge = [Edges[j], set([i, j])]
                if edge not in graph:
                    graph.append(edge)

        i += 1

def weightSort( arrElem ):
    return arrElem[0]

graph.sort(key = weightSort)

def KruskalAlgo(graph):
    res_nodes = []
    res_tree = []
    
    for edge in graph:
        inter_nodes = [] # Порядковые номера множеств, которые содержат вершины ребра edge (их всегда будет <= 2)
        cycle = 0 # Проверка на цикл
        for j in range(len(res_nodes)) :
            if edge[-1].issubset(res_nodes[j]): # Обе вершины ребра содержатся в множестве выбранных вершин -> цикл, в этом случае никуда не добавляем ребро (ни в дерево, ни во множество вершин)
                cycle = 1
                break
            elif (len(res_nodes[j].intersection(edge[-1])) == 1): # Одна из вершин ребра содержится во множестве выбранных вершин -> объединяем множества, добавляем порядковый номер множества в список
                res_nodes[j].update(edge[-1])
                inter_nodes.append(j)
        # Если в итоге вышло, что ребро имеет вершины в обоих множествах - объединяем их, удаляя одно из них
        if len(inter_nodes) == 2:
            res_nodes[inter_nodes[0]].update(res_nodes[inter_nodes[1]])
            res_nodes.pop(inter_nodes[1])
        # Ни одно из множеств не содержит одну вершину ребра - создается новое множество
        elif len(inter_nodes) == 0 and cycle != 1:
            res_nodes.append(edge[-1])
        if not cycle:
            res_tree.append([edge[0], edge[1].copy()])
    
    return res_tree


res = KruskalAlgo(graph)
print('Kruskal tree is:')
for edge in res:
    print(f'Edge: {edge[1]}, weight: {edge[0]}')



