import heapq
INF = int(1e9)

def dijkstra(start):
    distance = [INF] * (N + 1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for next_node, cost in graph[now]:
            new_cost = dist + cost
            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(q, (new_cost, next_node))

    return distance


# 입력
N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)] # 0 부터 시작하지만 인덱스 값으로 활용하고 싶어서 padding (one based padding)

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
# print(graph)

v1, v2 = map(int, input().split())

# 다익스트라 3번
dist1 = dijkstra(1)
# print(dijkstra(1))
distv1 = dijkstra(v1)
# print(dijkstra(v1))
distv2 = dijkstra(v2)
# print(dijkstra(v2))

# 두 가지 경로 경우 계산
path1 = dist1[v1] + distv1[v2] + distv2[N]
path2 = dist1[v2] + distv2[v1] + distv1[N]
# print(path1,path2)
result = min(path1, path2)

# INF가 포함되어 있으면 -1
print(result if result < INF else -1)