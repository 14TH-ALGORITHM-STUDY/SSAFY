import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

def find_parents(x):
    if x == parents[x]:
        return x

    parents[x] = find_parents(parents[x])
    return parents[x]

def union(x, y):
    rx = find_parents(x)
    ry = find_parents(y)

    if rx == ry:
        return

    if rx < ry:
        parents[ry] = rx
    else:
        parents[rx] = ry

N, M = map(int, input().split())
edges = []
for _ in range(M):
    n1, n2, w = map(int, input().split())
    edges.append((n1, n2, w))

edges.sort(key=lambda x : x[2])

parents = [i for i in range(N+1)]
cnt = 0
min_w_sum = 0 
large_w = 0

for u, v, w in edges:
    if find_parents(u) != find_parents(v):
        union(u, v)
        cnt += 1
        min_w_sum += w
        large_w = w

    if cnt == N:
        break

print(min_w_sum - large_w)



