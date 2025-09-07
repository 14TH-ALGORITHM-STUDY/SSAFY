from collections import deque

N, M = map(int, input().split())
grid = [list(input().strip()) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(sx, sy):
    visited = [[-1]*M for _ in range(N)]  
    q = deque()
    q.append((sx, sy))
    visited[sx][sy] = 0
    max_dist = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if grid[nx][ny] == 'L' and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    max_dist = max(max_dist, visited[nx][ny])
                    q.append((nx, ny))
    return max_dist

answer = 0
for i in range(N):
    for j in range(M):
        if grid[i][j] == 'L':
            answer = max(answer, bfs(i, j))

print(answer)
