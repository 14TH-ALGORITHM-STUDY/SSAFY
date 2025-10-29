from collections import deque

# 수정 아이디어 스케치
def build_wall(cnt, start):
    if cnt == 3:
        bfs()
        return

    # start 인덱스부터 탐색을 시작하여 중복을 방지
    for i in range(start, N * M):
        r = i // M  # 현재 인덱스를 행(row)으로 변환
        c = i % M   # 현재 인덱스를 열(column)으로 변환

        if graph[r][c] == 0:
            graph[r][c] = 1
            # 다음 벽은 현재 위치(i) 다음부터 찾아야 함
            build_wall(cnt + 1, i + 1)
            graph[r][c] = 0 # 백트래킹

def bfs():
    global max_safe_area
    queue = deque()
    tmp_graph = [row[:] for row in graph]

    for i in range(N):
        for j in range(M):
            if tmp_graph[i][j] == 2:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if tmp_graph[nx][ny] == 0: # 감염가능 여부
                    tmp_graph[nx][ny] = 2
                    queue.append((nx, ny))

    cnt = 0
    for i in range(N): # 행 순회하며 0 개수 세기
        cnt += tmp_graph[i].count(0)

    max_safe_area = max(max_safe_area, cnt)

# 상 하 좌 우
dx = [0,0,1,-1]
dy = [1,-1,0,0]

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

max_safe_area = 0
build_wall(0, 0)

print(max_safe_area)
