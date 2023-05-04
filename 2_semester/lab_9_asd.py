def BellmanFord(edges, N, src): # реализация со списком смежности
    inf = 10**9
    dist = [inf] * N
    dist[src] = 0

    for k in range(1, N):
        for j, i in edges.keys():
            if dist[j - 1] + edges[j, i] < dist[i - 1]:
                dist[i - 1] = dist[j - 1] + edges[j, i]

    CycleFound = False 
    for j, i in edges.keys(): # Проверка на отрицательный цикл
        if dist[j - 1] + edges[j, i] < dist[i - 1]: 
            CycleFound = True
            break

    if CycleFound:
        return "Обнаружен цикл"
    return dist


edges = {(1, 2): -1, (1, 4): 3, (2, 3): 3, (2, 5): 2, (2, 4): 2, (4, 5): -3, (5, 2): 1, (5, 3): 5}
print(BellmanFord(edges, 5, 0))

edges = {(1, 2): 6, (2, 3): 2, (3, 4): -10, (1, 4): 3, (4, 2): 5}
print(BellmanFord(edges, 4, 0))

