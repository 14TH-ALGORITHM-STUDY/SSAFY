import sys
from collections import deque

# sys.stdin = open("1261.algospot.txt", "r")
input = sys.stdin.readline

dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)


def dijkstra(start):
    dq = deque([start])
    dist = [[float("inf")] * M for _ in range(N)]
    dist[0][0] = 0

    while dq:
        r, c = dq.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if not (0 <= nr < N and 0 <= nc < M):
                continue

            cost = dist[r][c] + grid[nr][nc]

            if cost >= dist[nr][nc]:
                continue

            dist[nr][nc] = cost

            if grid[nr][nc] == 0:
                dq.appendleft((nr, nc))
            else:
                dq.append((nr, nc))

    return dist[N - 1][M - 1]


M, N = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(N)]

ans = dijkstra((0, 0))

print(ans)
