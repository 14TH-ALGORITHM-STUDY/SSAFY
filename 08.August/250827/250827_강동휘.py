import sys
from collections import deque


dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def find_start(arr, N):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 9:
                return i, j
    return -1, -1

def bfs_find_prey(arr, N, si, sj, size):
    dist = [[-1] * N for _ in range(N)]
    q = deque([(si, sj)])
    dist[si][sj] = 0

    best_d = float('inf')
    best_i = best_j = -1

    while q:
        i, j = q.popleft()
        if dist[i][j] > best_d:
            continue

        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and dist[ni][nj] == -1:
                if arr[ni][nj] <= size:
                    dist[ni][nj] = dist[i][j] + 1
                    if 0 < arr[ni][nj] < size:
                        d = dist[ni][nj]
                        if d < best_d or (d == best_d and (ni, nj) < (best_i, best_j)):
                            best_d, best_i, best_j = d, ni, nj
                    q.append((ni, nj))

    if best_d < float('inf'):
        return best_i, best_j, best_d
    return None

def solve(N, arr):
    si, sj = find_start(arr, N)
    arr[si][sj] = 0

    size = 2
    eaten = 0
    total_time = 0

    while True:
        prey = bfs_find_prey(arr, N, si, sj, size)
        if prey is None:
            break
        ti, tj, d = prey

        total_time += d
        eaten += 1
        arr[ti][tj] = 0
        si, sj = ti, tj

        if eaten == size:
            size += 1
            eaten = 0

    return total_time

N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
print(solve(N, arr))
