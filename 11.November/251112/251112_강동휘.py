from heapq import heappop, heappush


def dijkstra(start):
    hq = []
    dists = [float('inf')] * (N + 1)  # 1-based padding
    dists[start] = 0
    heappush(hq, (0, start))  # dist, node

    while hq:
        dist, cur = heappop(hq)  # 누적 거리값, 현재 위치

        if dist > dists[cur]:
            continue

        for nxt, w in graph[cur]:
            nd = dist + w

            if nd > dists[nxt]:
                continue

            dists[nxt] = nd
            heappush(hq, (nd, nxt))

    return dists


# 입력부
N, E = map(int, input().split())

graph = [[] for _ in range(N + 1)]  # 1-based padding

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

dist_from_1 = dijkstra(1)
dist_from_v1 = dijkstra(v1)
dist_from_v2 = dijkstra(v2)

path1 = dist_from_1[v1] + dist_from_v1[v2] + dist_from_v2[N]
path2 = dist_from_1[v2] + dist_from_v2[v1] + dist_from_v1[N]

ans = min(path1, path2)
print(ans if ans < float('inf') else -1)
