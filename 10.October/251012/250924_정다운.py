import sys
import heapq

input = sys.stdin.readline

M, N = map(int, input().split())
grid = [input().strip() for _ in range(N)]

INF = 10**4 # N, M이 최대 100이므로 모든 칸을 다 더해도 10000을 넘지 않으므로 최댓값 10**4로 설정
dist = [[INF]*M for _ in range(N)] # 각 위치까지 최소 벽 부순 횟수 (가중치)
dist[0][0] = 0

pq = [(0, 0, 0)] # (부순 벽 개수, r, c)
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

while pq:
    cost, r, c = heapq.heappop(pq)
    if cost > dist[r][c]:
        continue
    if r == N-1 and c == M-1:
        break
    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M:
            w = 1 if grid[nr][nc] == '1' else 0 # 벽을 만나면 가중치 1, 아니면 0
            ncst = cost + w
            if ncst < dist[nr][nc]:
                dist[nr][nc] = ncst
                heapq.heappush(pq, (ncst, nr, nc))

print(dist[N-1][M-1])