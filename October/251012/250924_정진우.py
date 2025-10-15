from collections import deque

def bfs(N,M,arr):
    visited = [[-1] * N for _ in range(M)]
    q = deque()
    q.append((0,0))
    visited[0][0] = 0
    dr = [1,-1,0,0]
    dc = [0,0,1,-1]

    while q:
        x,y = q.popleft()

        if x == M-1 and y == N-1:
            return visited[x][y]

        for i in range(4):
            nx,ny = x + dr[i], y + dc[i]

            if 0 <= nx < M and 0 <= ny < N:
                new_cnt = visited[x][y] + arr[nx][ny]
                if visited[nx][ny] == -1:
                    visited[nx][ny] = new_cnt
                    if arr[nx][ny] == 0:
                        q.appendleft((nx,ny))
                    else :
                        q.append((nx,ny))
                elif new_cnt < visited[nx][ny]:
                    visited[nx][ny] = new_cnt
                    if arr[nx][ny] == 0:
                        q.appendleft((nx,ny))
                    else :
                        q.append((nx,ny))
    return -1


N, M = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(M)]

print(bfs(N,M,arr))