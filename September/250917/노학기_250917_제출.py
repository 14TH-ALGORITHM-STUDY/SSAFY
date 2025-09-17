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

def build_wall(wall_cnt):
    # 벽 3개가 세워지면 바이러스를 퍼트려 본다.
    if wall_cnt == 3:
        bfs()
        return

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1 # 벽을 세우고
                build_wall(wall_cnt + 1) # 다시 두번째 벽 세우러 간다
                graph[i][j] = 0


# #인덱스를 이용해서 접근
# def build_wall(cnt, start):
#     if cnt == 3:
#         bfs()
#         return
#
#     # start 인덱스부터 탐색을 시작하여 중복을 방지
#     for i in range(start, N * M):
#         r = i // M  # 현재 인덱스를 행(row)으로 변환
#         c = i % M  # 현재 인덱스를 열(column)으로 변환
#
#         if graph[r][c] == 0:
#             graph[r][c] = 1
#             # 다음 벽은 현재 위치(i) 다음부터 찾아야 함
#             build_wall(cnt + 1, i + 1)
#             graph[r][c] = 0  # 백트래킹


    # # --- 메인 로직: for문 중첩으로 3개의 벽 조합 찾기 ---
    # # 1. 빈칸 후보들 중에서 3개를 순서 없이 고름
    # for i in range(len(empty_cells)):
    #     # 2. 두 번째 벽은 첫 번째 벽 다음 위치부터 고름
    #     for j in range(i + 1, len(empty_cells)):
    #         # 3. 세 번째 벽은 두 번째 벽 다음 위치부터 고름
    #         for k in range(j + 1, len(empty_cells)):
    #             # 3개의 벽 위치 좌표를 가져옴
    #             r1, c1 = empty_cells[i]
    #             r2, c2 = empty_cells[j]
    #             r3, c3 = empty_cells[k]
    #
    #             # 벽 3개 설치
    #             graph[r1][c1] = 1
    #             graph[r2][c2] = 1
    #             graph[r3][c3] = 1
    #
    #             # bfs로 안전 영역 크기 계산
    #             bfs()
    #
    #             # 설치했던 벽 다시 허물기 (다음 조합을 위해 원상 복구)
    #             graph[r1][c1] = 0
    #             graph[r2][c2] = 0
    #             graph[r3][c3] = 0


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
