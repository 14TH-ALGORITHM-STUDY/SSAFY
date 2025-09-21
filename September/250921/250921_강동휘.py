import sys


# sys.stdin = open("1647_city_division_plan.txt", "r")
input = sys.stdin.readline


def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb:
        return False
    if rank[ra] < rank[rb]:
        parent[ra] = rb
    elif rank[ra] > rank[rb]:
        parent[rb] = ra
    else:
        parent[rb] = ra
        rank[ra] += 1
    return True


N, M = map(int, input().split())
edges = []
for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

parent = list(range(N + 1))
rank = [0] * (N + 1)

total = 0
max_edge = 0
cnt = 0

for c, a, b in edges:
    if union(a, b):
        total += c
        max_edge = max(max_edge, c)
        cnt += 1
        if cnt == N - 1:
            break

print(total - max_edge)
