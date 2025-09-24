################################################################################
# 📌 파일명 규칙 : 날짜_이름.py   (예: 250806_김싸피.py)
# 📌 commit 규칙 : [이름]_날짜_제출 (예: [권순재]_250806_제출)
#
# ⚠️ git pull 후 git clone (충돌 방지)
# ⚠️ 반드시 스켈레톤 파일을 복사하여 개인 파일로 작성
# ⚠️ 입출력 예시는 반드시 테스트 후 제출
# ⚠️ 제출 전 코드 최종 점검 (입력 형식, 조건 처리 등)
################################################################################
import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())
miro = [list(input().strip()) for _ in range(n)]

# 각 칸까지의 최소 비용(부순 벽의 개수)을 저장할 배열
# 초깃값은 매우 큰 수로 설정하여 방문하지 않았음을 표시
dist = [[-1] * m for _ in range(n)]

q = deque()

# 시작점 (0, 0) 설정
q.append((0, 0))
dist[0][0] = 0
# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    x, y = q.popleft()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if dist[nx][ny] == -1:
                # 다음 칸이 빈 방일 경우 (비용 0)
                if miro[nx][ny] == '0':
                    # 비용이 들지 않으므로 덱의 맨 앞에 추가 (우선 탐색)
                    q.appendleft((nx, ny))
                    dist[nx][ny] = dist[x][y]

                # 다음 칸이 벽일 경우 (비용 1)
                else:
                    # 비용이 발생하므로 덱의 맨 뒤에 추가
                    q.append((nx, ny))
                    dist[nx][ny] = dist[x][y] + 1

print(dist[n-1][m-1])