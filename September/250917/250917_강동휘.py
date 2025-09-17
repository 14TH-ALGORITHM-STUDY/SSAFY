from collections import deque


# 단계별로 생각해보기
# 1. 먼저 벽 3개를 세울 수 있는 경우를 모두 고려한다.
#  - 벽을 세울 수 있는 공간(빈공간을 따로 좌표 저장한다)
#  - 빈 공간에서 3가지 경우의 벽을 세운다.
# 2. 벽이 세워진 경우에서 바이러스가 갈수 있는 범위를 모두 바이러스로 채운다.
# 3. 결과물의 배열에서 빈 칸은 곧 안전구역이므로 갯수를 카운팅한다.
# 4. 안전구역의 최댓값을 구한다.

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs():
    grid = [row[:] for row in matrix]
    q = deque(virus)

    while q:
        tr, tc = q.popleft()
        for i in range(4):
            nr = tr + dr[i]
            nc = tc + dc[i]

            if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] == 0:
                grid[nr][nc] = 2
                q.append((nr, nc))

    safe_zone = 0
    for row in grid:
        safe_zone += row.count(0)

    return safe_zone


def sol(cnt, start):
    global ans

    # 종료 조건
    if cnt == 3:
        ans = max(ans, bfs())
        return

    # 가지치기
    if len(empty) - start < 3 - cnt:
        return

    for i in range(start, len(empty)):
        row, col = empty[i]

        # 빈 공간이 아니라면
        if matrix[row][col] != 0:
            continue

        matrix[row][col] = 1  # 벽 세우기
        sol(cnt + 1, i + 1)  # 다음 칸으로
        matrix[row][col] = 0  # 원복


N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

# 빈공간의 좌표와 바이러스의 좌표 저장
empty = []
virus = []
for r in range(N):
    for c in range(M):
        if matrix[r][c] == 0:
            empty.append((r, c))
        elif matrix[r][c] == 2:
            virus.append((r, c))

ans = 0
walls = []
sol(0, 0)
print(ans)
