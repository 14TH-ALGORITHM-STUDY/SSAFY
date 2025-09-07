import sys
from collections import deque


# 2차원 배열에서 L, W 만 존재
# 상하좌우 이동 가능
# 최단 거리로 이동하는데 있어 가장 긴 시간이 걸리는 L 두 곳에 나뉘어 묻혀있다.
# 최단 거리를 출력하라
# 시간 제한 1초(2500 * 2500 = 6,250,000)
# BFS + 완전탐색

DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs_find_min_dist(si, sj):
    dist = [[-1] * M for _ in range(N)]
    q = deque([(si, sj)])
    dist[si][sj] = 0
    max_dist = 0

    while q:
        ci, cj = q.popleft()
        for di, dj in DIRS:
            ni, nj = ci + di, cj + dj
            if  0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] == 'L' and dist[ni][nj] == -1:
                    dist[ni][nj] = dist[ci][cj] + 1
                    max_dist = max(max_dist, dist[ni][nj])
                    q.append((ni, nj))

    return max_dist

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            ans = max(ans, bfs_find_min_dist(i, j))

print(ans)


