adjacency_matrix = [
    [0, 7, 9, 0, 0, 14],
    [7, 0, 10, 15, 0, 0],
    [9, 10, 0, 11, 0, 2],
    [0, 15, 11, 0, 6, 0],
    [0, 0, 0, 6, 0, 9],
    [14, 0, 2, 0, 9, 0]
]


def findMinimum(s, matrix, used): # Ищем ближайшего соседа до текущей ноды
    _min = 9999
    index_min = 0
    for i in range(len(matrix[s])):
        weight = matrix[s][i] 
        if i not in used and weight != 0:
            if weight < _min:
                _min = weight
                index_min = i

    return index_min

def dijkstra(s, matrix): # Алгоритм Дейкстры 
    used = [] # Использованные вершины
    short_path = [[9999, ''] for i in range(len(matrix))] # Короткий путь
    short_path[s] = [0, ''] # Короткий путь из заданной вершины в нее саму же

    while len(used) != len(short_path): # Пока не все вершины окажутся пройденными

        for i in range(len(matrix[s])):
            if not matrix[s][i] == 0 and i not in used: # Есть ребро между двумя вершинами и i - неисп. вершина
                weight = matrix[s][i] # Вес ребра

                if short_path[i][0] > weight + short_path[s][0]: # Если найден более краткий путь до ребра, то в результат записываем его
                    short_path[i][1] = short_path[s][1] + (str(s) + ' ') # Список вершин пути
                    short_path[i][0] = weight + short_path[s][0]         # Длина пути
        
        used.append(s)

        s = findMinimum(s, adjacency_matrix, used)
    
    return short_path

node = 0

res = dijkstra(node, adjacency_matrix)
print(f'Расстояния от вершины {node} до:\n')
for second_node in range(len(res)):
    print(f'{second_node}: {res[second_node]}')