n = int(input()) # количество предметов
K = int(input()) # максимальная вместимость рюкзака
W = list(map(int, input().split())) # список весов предметов от 0 до n
P = list(map(int, input().split())) # список цен предметов от 0 до n

F = [ [0]*(K+1) for i in range(n)] # Строим таблицу весов и кол-ва предметов
for i in range(n):
    for k in range(1, K+1):
        if k >= W[i]:
            F[i][k] = max(F[i - 1][k], F[i - 1][k - W[i]] + P[i])
        else:
            F[i][k] = F[i - 1][k]

for line in F:
    print(line)
res = []
k = K-1
for i in range(n-1, 0, -1):
    if F[i][k] != F[i - 1][k]:
        res.append(i)
        k -= W[i]

print(W)
print(P)
print(res)