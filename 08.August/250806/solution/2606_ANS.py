def dfs(v):
    vstd[v] = True
    for i in g[v]:
        if not vstd[i]:
            dfs(i)

C = int(input())
L = int(input())
g = [[] for i in range(C + 1)]
vstd = [False] * (C + 1)

for i in range(L):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

dfs(1)
print(sum(vstd) - 1)