class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)] # матрица смежности
        for (src, dest) in edges: # добавление ребер в граф (неориентированный)
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)

# Функция для присвоения цвета вершинам графа
def colorGraph(graph, n):
    result = {}
    for u in range(n): # Назначение цвета вершинам
        #Смотрим на цвета вершин, смежных вершине u, если они уже покрашены
        assigned = set([result.get(i) for i in graph.adjList[u] if i in result])
        # проверка первого доступного цвета
        color = 1
        for c in assigned:
            if color != c:
                break
            color = color + 1
        # назначает вершине u первый доступный цвет
        result[u] = color
    for v in range(n):
        print(f'Color assigned to vertex {v} is {colors[result[v]]}')

if __name__ == '__main__':
    # Цвета
    colors = ['', 'blue', 'green', 'red', 'yellow', 'orange', 'pink',
            'black', 'brown', 'white']
    # Список ребер
    '''
    edges = [(0, 1), (0, 2), (0, 3), (1, 4), (1, 8), (2, 6), (2, 7), (3, 5), (3, 9), (4, 5), (4, 7), (5, 6), (6, 8), (7, 9), (8, 9)]
    edges = [(0, 1), (1, 2), (3, 2), (3, 4), (4, 1)]'''
    edges = [(3, 5), (2, 3), (4, 3), (1, 2), (1, 3), (0, 1), (5, 0), (4, 0), (1, 5)]
    # количество вершин в графе
    n = 6
    # строит граф по заданным ребрам
    graph = Graph(edges, n)
    colorGraph(graph, n)