################################################################################
# 📌 파일명 규칙 : 날짜_이름.py   (예: 250806_김싸피.py)
# 📌 commit 규칙 : [이름]_날짜_제출 (예: [권순재]_250806_제출)
# 
# ⚠️ git pull 후 git clone (충돌 방지)
# ⚠️ 반드시 스켈레톤 파일을 복사하여 개인 파일로 작성
# ⚠️ 입출력 예시는 반드시 테스트 후 제출
# ⚠️ 제출 전 코드 최종 점검 (입력 형식, 조건 처리 등)
################################################################################
from collections import deque

def build_wall(wall_cnt, build_list):
    # 벽 3개가 세워지면 바이러스를 퍼트려 본다.
    if wall_cnt == 3:
        bfs()
        return

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1 # 벽을 세우고
                build_wall(wall_cnt+1, build_list + ) # 다시 두번째 벽 세우러 간다
                graph[i][j] = 0

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
build_wall(0, [])

print(max_safe_area)