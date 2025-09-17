from collections import deque

# 바이러스를 퍼뜨리고 안전 영역 크기를 계산하는 함수 (이전과 동일)
def bfs():
    global max_safe_area

    temp_graph = [row[:] for row in graph]
    queue = deque()

    for i in range(n):
        for j in range(m):
            if temp_graph[i][j] == 2:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and temp_graph[nx][ny] == 0:
                temp_graph[nx][ny] = 2
                queue.append((nx, ny))

    current_safe_area = sum(row.count(0) for row in temp_graph)
    max_safe_area = max(max_safe_area, current_safe_area)


# --- 입력 및 초기 설정 ---
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
empty_cells = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            empty_cells.append((i, j))

max_safe_area = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# --- 메인 로직: for문 중첩으로 3개의 벽 조합 찾기 ---
# 1. 빈칸 후보들 중에서 3개를 순서 없이 고름
for i in range(len(empty_cells)):
    # 2. 두 번째 벽은 첫 번째 벽 다음 위치부터 고름
    for j in range(i + 1, len(empty_cells)):
        # 3. 세 번째 벽은 두 번째 벽 다음 위치부터 고름
        for k in range(j + 1, len(empty_cells)):
            # 3개의 벽 위치 좌표를 가져옴
            r1, c1 = empty_cells[i]
            r2, c2 = empty_cells[j]
            r3, c3 = empty_cells[k]

            # 벽 3개 설치
            graph[r1][c1] = 1
            graph[r2][c2] = 1
            graph[r3][c3] = 1

            # bfs로 안전 영역 크기 계산
            bfs()

            # 설치했던 벽 다시 허물기 (다음 조합을 위해 원상 복구)
            graph[r1][c1] = 0
            graph[r2][c2] = 0
            graph[r3][c3] = 0

print(max_safe_area)