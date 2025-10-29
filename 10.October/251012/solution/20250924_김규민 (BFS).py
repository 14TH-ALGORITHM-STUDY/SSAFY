#미로 크기 N*M
#상, 하, 좌, 우 이동 가능
# 빈방: 0, 벽: 1
#(1,1)에서 (N,M)으로 이동하려면 벽을 최소 몇개 부숴야 하는지?


from collections import deque

def bfs(N, M, arr):
   

    dist = [[-1] * M for _ in range(N)] # 벽 부순 횟수를 넣을 배열 생성

     # dist에 처음 값을 -1을 넣는 이유는 방문체크도 함께 하려고
    # 10e9를 넣어도 카운트 하는 부분의 조건만 바꿔준다면 동일하게 값 나옴
    #         if 0 <= nx < N and 0 <= ny < M:
    #                   new_count = dist[x][y] + arr[nx][ny]
    #                   if new_count < dist[nx][ny]: 
    #  -> 여기 if문에서 새 경로가 더 작으면 갱신되기 때문에, 방문 체크가 필요 없음
    #                      dist[nx][ny] = new_count
    #                      q.append((nx, ny))

    dist[0][0] = 0  # 시작점 값 0

    q = deque()
    q.append((0, 0))  # (처음 좌표값 0,0 삽입)

    while q:
        x, y = q.popleft()

        #상, 하, 좌, 우 이동 지정
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx, ny = x + dx, y + dy

            #범위 안에 있을 경우
            if 0 <= nx < N and 0 <= ny < M:
                #다음 칸의 값 누적
                new_count = dist[x][y] + arr[nx][ny]
                #아직 방문하지 않았거나 더 적은 횟수로 벽을 부술 수 있는 경우
                if dist[nx][ny] == -1 or new_count < dist[nx][ny]:
                    # 벽 부순 누적 값 넣기
                    dist[nx][ny] = new_count
                    # 좌표 넣기
                    q.append((nx, ny))

    return dist[N-1][M-1] # 도작 치점 값 반환


M, N = map(int, input().split())  # M: 열, N: 행
arr = [list(map(int, input().strip())) for _ in range(N)] #입력 배열

result = bfs(N, M, arr)
print(result)
