# 1. 모든 다리 길이의 합의 최소값
#   -> MST(Minimum Spanning Tree)
# 2. MST 를 사용하기 위한 자료구조
#   -> (w, u, v)
# 3. 이 문제에서 w, u, v 를 정의 하려면
#    u, v 로 구분될 수있는 노드들이 포함될 집합(섬)들을 구분할 라벨링이 필요하고
#    그 집합 내에서도 node 가 될 수 있는 후보들(가장자리)를 정의하는게 필요하다.
# 4. 라벨링
#    모든 node 를 순회하며, 인접한 곳이 땅(1)이라면 같은 집합에 포함시킨다.
#    이 과정에서 이미 방문한 곳은 방문하면 안된다.
#    같은 집합의 기준은 인덱스로 한다.
#    산출물은 섬이 구분된 배열이다.
#    + 후에 탐색을 위해서 라벨링이 완료된 배열판도 필요
# 5. 후보 선정 및 간선 탐색
#    후보가 될 수 있으려면, 바다로 나갈 수 있어야 한다.
#    같은 섬이라면 탐색을 중지
#    바다로 나갈 수 있다는 것은 인접한 노드가 0이여야 한다.
#    직선 탐색을 해보고 간선이 이루어진다면 이제 후보다.
#    거리를 w 시작점 u 도착점 v 형태로 산출물을 만든다.
#    + 특이점: 섬의 모든 칸이 시작점
from collections import deque


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


# 유틸 함수
def is_land(y, x):
    if board[y][x] == 0:
        return False
    return True


# 라벨링 bfs 함수
def labeling_bfs(pos, label_id):
    q = deque([pos])
    y, x = pos
    visited[y][x] = True
    board[y][x] = label_id
    islands[label_id].append((y, x))

    while q:
        y, x = q.popleft()
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if not (0 <= ny < N and 0 <= nx < M):
                continue
            if visited[ny][nx]:
                continue
            if not is_land(ny, nx):
                continue

            visited[ny][nx] = True
            board[ny][nx] = label_id
            islands[label_id].append((ny, nx))
            q.append((ny, nx))


# 탐색
def search(label):
    # 섬의 모든 칸이 시작점
    for (y, x) in islands[label]:
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            length = 0

            # 직선으로 쭉 감
            while 0 <= ny < N and 0 <= nx < M:
                # 같은 섬 만나면 중단
                if board[ny][nx] == label:
                    break

                # 다른 섬 만남
                if board[ny][nx] > 0 and board[ny][nx] != label:
                    # 다리 길이는 2 이상이어야 함
                    if length >= 2:
                        edges.append((length, label, board[ny][nx]))
                    # 다른 섬을 만났으면 무조건 이 방향 탐색 끝
                    break

                # 바다인 경우 계속 전진
                if board[ny][nx] == 0:
                    length += 1
                    ny += dy[d]
                    nx += dx[d]
                else:
                    # 이 경우는 거의 없음(예외용)
                    break


def find_set(x):
    if x == parents[x]:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    rx = find_set(x)
    ry = find_set(y)

    if rx == ry:
        return False

    # 작은 루트로 합치기 (아무 규칙이나 하나만 잡으면 됨)
    if rx < ry:
        parents[ry] = rx
    else:
        parents[rx] = ry
    return True


# 입력부
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 라벨링
visited = [[False] * M for _ in range(N)]
# 문제에서 섬 최대 6개라서 7칸 짜리 만든 네 스타일 유지
islands = [[] for _ in range(7)]
label_num = 1
for row in range(N):
    for col in range(M):
        if not is_land(row, col):
            continue
        if visited[row][col]:
            continue

        labeling_bfs((row, col), label_num)
        label_num += 1

island_cnt = label_num - 1  # 실제 섬 개수

# 후보 선정 및 간선 탐색
edges = []
for island in range(1, island_cnt + 1):
    search(island)

# MST
edges.sort()

cnt = 0
result = 0

parents = [i for i in range(island_cnt + 1)]

for w, u, v in edges:
    # 서로 다른 집합이면 다리 채택
    if union(u, v):
        cnt += 1
        result += w

# 섬이 k개면 k-1개의 다리가 있어야 모두 연결된 것
if cnt == island_cnt - 1:
    print(result)
else:
    print(-1)
