# 목표: 모든 'L'(육지) 칸을 시작점으로 BFS를 수행하여
#       각 시작점에서 도달 가능한 육지들까지의 "최단 거리" 중 최댓값을 구한다.
# 핵심: 최단 거리는 DFS가 아닌 BFS로만 '보장'되므로 BFS 사용이 정석.

from collections import deque
import sys

# 입력 가속(선택): 데이터가 많아도 안전하게 처리
input = sys.stdin.readline

# N: 행(세로), M: 열(가로)
N, M = map(int, input().split())

# 지도 입력
grid = [list(input().strip()) for _ in range(N)]

# 4방향 이동(상하좌우). dx, dy는 동일 인덱스끼리 짝으로 사용.
# 예) i=0일 때 (x+dx[0], y+dy[0]) => (x+1, y) (아래로 한 칸)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(sx, sy):
    """
    (sx, sy)에서 시작하는 BFS.
    - visited[r][c]에는 (sx,sy)로부터 (r,c)까지의 '최단 거리'를 기록.
    - 방문하지 않은 칸은 -1로 두어 방문여부 + 거리를 한 번에 관리.
    - 큐(선입선출)를 사용해 '거리 레벨' 순서대로 탐색 => 최단 거리 보장.
    반환값: (sx,sy)에서 도달 가능한 육지들 중 최장 최단거리(max_dist).
    """

    # 방문 겸 최단거리 기록용 2차원 배열. 처음엔 전부 미방문(-1)
    visited = [[-1] * M for _ in range(N)]

    # BFS용 큐. collections.deque: O(1)에 popleft 가능
    q = deque()

    # 시작점 enqueue 및 방문/거리 0으로 초기화
    q.append((sx, sy))
    visited[sx][sy] = 0

    # 이 시작점에서 얻을 수 있는 최장 최단거리
    max_dist = 0

    # 큐가 빌 때까지(= 더 이상 확장할 칸이 없을 때까지) 진행
    while q:
        x, y = q.popleft()  # 큐 맨 앞(가장 먼저 들어온) 좌표를 꺼낸다
        # ↑ BFS는 '레벨(거리)' 순서대로 탐색되므로,
        #   이 시점의 visited[x][y]는 이미 최단 거리로 확정된 값

        # 현재 칸 (x,y)에서 4방향 이웃을 확인
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 1) 지도 범위를 벗어나면 스킵
            if not (0 <= nx < N and 0 <= ny < M):
                continue

            # 2) 바다는 건널 수 없으므로 스킵
            if grid[nx][ny] != 'L':
                continue

            # 3) 이미 방문했다면 스킵 (visited != -1)
            if visited[nx][ny] != -1:
                continue

            # 여기까지 왔다면: 육지이면서 아직 방문하지 않은 유효한 이웃
            # → (x,y)의 최단거리 + 1 이 (nx,ny)의 최단거리
            visited[nx][ny] = visited[x][y] + 1

            # 최장 최단거리 갱신 시도
            # (BFS라 방문 순간의 거리는 곧 최단거리이므로 바로 비교 가능)
            if visited[nx][ny] > max_dist:
                max_dist = visited[nx][ny]

            # 다음 레벨 탐색을 위해 큐에 삽입(나중에 꺼내 탐색)
            q.append((nx, ny))
            # ※ 직관: 큐의 상태는 "앞쪽 = 더 가까운 칸들, 뒤쪽 = 방금 발견한 더 먼 칸들"

    # (sx,sy)에서 가장 멀리 도달한 칸까지의 최단거리
    return max_dist


# 전체 정답(모든 시작점 BFS 중 최대값)
answer = 0

# 모든 좌표를 시작점 후보로 순회
for i in range(N):
    for j in range(M):
        # 바다는 시작점이 될 수 없음 → 스킵
        if grid[i][j] != 'L':
            continue

        # (i,j)가 육지라면 BFS 실행.
        # BFS는 해당 시작점 기준으로만 visited를 만들고 사용 → 서로 간섭 없음.
        # 반환된 최장 최단거리로 전역 최대값 갱신
        dist = bfs(i, j)
        if dist > answer:
            answer = dist

# 출력: 두 육지 사이의 가장 긴 최단거리
print(answer)

# ──────────────────────────────────────────────────────────────────────────
# 복잡도 분석:
#  - N, M ≤ 50 → 칸 수 최대 2500.
#  - 매 육지 칸에서 BFS를 수행(최대 ~2500회)하더라도,
#    각 BFS는 O(N*M) = O(2500). 따라서 최악 O((N*M)^2) ≈ 6,250,000
# 요약:
#  - BFS는 '레벨(거리)' 순으로 확장되므로, 방문 순간의 거리는 최단거리 보장.
#  - visited에 거리(=레벨)를 기록하면, 별도 거리배열 없이 방문체크와 거리계산을 동시에 처리 가능.
#  - 큐에 넣는다는 건 "다음에(혹은 그 다음에) 탐색할 후보"로 등록한다는 뜻.
