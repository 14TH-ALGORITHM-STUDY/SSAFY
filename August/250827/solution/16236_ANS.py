import sys
from collections import deque

input = sys.stdin.readline

# 상, 좌, 우, 하 (거리 동률일 때 "위쪽, 그다음 왼쪽" 우선에 자연스럽게 유리)
DIRS = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def find_start(board, N):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 9:
                board[i][j] = 0  # 시작 위치는 빈칸으로 변경
                return i, j
    return -1, -1

def bfs_find_prey(board, N, si, sj, size):
    """현재 위치(si, sj)에서 먹을 수 있는 물고기 중
       최단거리/위쪽/왼쪽 우선순위로 '한 마리'를 찾는다.
       반환: (ti, tj, dist) 또는 None
    """
    dist = [[-1] * N for _ in range(N)]
    q = deque([(si, sj)])
    dist[si][sj] = 0

    best_d = None
    best_i = best_j = -1

    while q:
        i, j = q.popleft()

        # 이미 최적 거리(best_d)를 찾았다면 그보다 더 먼 칸은 볼 필요 없음
        if best_d is not None and dist[i][j] > best_d:
            continue

        for di, dj in DIRS:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and dist[ni][nj] == -1:
                # 지나갈 수 있는 칸: 물고기 크기 <= 현재 상어 크기
                if board[ni][nj] <= size:
                    dist[ni][nj] = dist[i][j] + 1
                    # 먹을 수 있는 물고기: 0 < 크기 < size
                    if 0 < board[ni][nj] < size:
                        if best_d is None or dist[ni][nj] < best_d or \
                           (dist[ni][nj] == best_d and (ni, nj) < (best_i, best_j)):
                            best_d, best_i, best_j = dist[ni][nj], ni, nj
                    q.append((ni, nj))

    if best_d is None:
        return None
    return best_i, best_j, best_d

def main():
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    si, sj = find_start(board, N)
    size = 2
    eaten = 0
    total_time = 0

    while True:
        prey = bfs_find_prey(board, N, si, sj, size)
        if prey is None:
            break
        ti, tj, d = prey

        total_time += d          # 이동 시간 누적
        eaten += 1               # 한 마리 먹음
        board[ti][tj] = 0        # 먹은 자리 비우기
        si, sj = ti, tj          # 위치 갱신

        if eaten == size:        # 성장 체크
            size += 1
            eaten = 0

    print(total_time)

if __name__ == "__main__":
    main()
