k = int(input()) # Кол-во вершин
adjMatrix = [[0]*k for i in range(k)] # Матрица смежности
s = list(map(int, input().split()))


for i in range(0, len(s)-1, 2): # Заполнение матрицы
    m = s[i] - 1
    n = s[i+1] - 1
    adjMatrix[m][n] = 1
    adjMatrix[n][m] = 1

# Эйлеров цикл существует тогда и только тогда, когда граф связный или будет являться связным, если удалить из него все изолированные вершины, и в нём отсутствуют вершины нечётной степени.

def isConnected(matrix): # Проверка на связность
    components = []
    q = []
    used = [0 for i in range(len(matrix))]

    for i in range(len(matrix)):
        if used[i] == 0:
            component = []
            q.append(i)
            while len(q):
                i = q.pop(0)
                used[i] = 1
                component.append(i)
                for j in range(len(matrix)):
                    edge = matrix[i][j]
                    if edge and used[j] == 0 and j not in q:
                        q.append(j)
            
            components.append(component)

    for i in range(len(components)):
        if len(components[i]) == 1: # Изолированная вершина
            components.pop(i)
    
    if len(components) != 1:
        return False
    return True


def isCycle(matrix): # Проверка на четность степеней
    i = 0
    q = []
    k = [0 for i in range(len(matrix))] # Массив степеней вершин
    q.append(i)

    while(len(q)):
        Node = q.pop(0)
        for j in range(len(matrix)): # j - следующая вершина
            edge = matrix[Node][j]   # ребро i-j

            if edge:
                k[Node] += 1
                if k[j] == 0 and j not in q: # если j еще не рассмотрена и не добавлена в очередь
                    q.append(j)
        
        if k[Node] % 2 != 0: # Найдена вершина с нечетной степенью
            return 'Not Cycle'
        
    return 'Cycle'

if isConnected(adjMatrix):
    print(isCycle(adjMatrix))



