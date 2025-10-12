#미로 크기 N*M
#상, 하, 좌, 우 이동 가능
# 빈방: 0, 벽: 1
#(1,1)에서 (N,M)으로 이동하려면 벽을 최소 몇개 부숴야 하는지?
from heapq import heappush, heappop


def dijkstra(N, M, arr):
    dist = [[10e9] * M for _ in range(N)]  # 벽 부순 횟수를 넣을 배열
    dist[0][0] = 0 #시작점 값 0
    pq = [(0, 0, 0)]  # (벽 부순 횟수, x, y)

    while pq:
        block, x, y = heappop(pq)

        # 이미 더 적은 비용으로 방문한 적이 있다면 스킵
        if block > dist[x][y]:
            continue

        #상,하,좌,우 이동 지정
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx, ny = x + dx, y + dy 

            # 범위를 벗어났으면 스킵
            if not (0 <= nx < N and 0 <= ny < M):
                continue

            # 다음 칸의 벽 여부에 따라서 누적할 변수
            next_block = block + arr[nx][ny]

            # 더 적은 횟수로 벽을 부술 수 있다면 해라
            if next_block < dist[nx][ny]:
                dist[nx][ny] = next_block
                heappush(pq, (next_block, nx, ny))

    return dist[N-1][M-1]  # 도착 지점 값 반환

M, N = map(int, input().split()) # M이 열이고 N이 행임 크랙 조심.
arr = [list(map(int, input().strip())) for _ in range(N)] #입력 배열

result = dijkstra(N, M, arr)
print(result)