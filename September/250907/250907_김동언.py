from collections import deque

def bfs(position):
    global max_long #출력할 값인 최대 이동거리를 수정할 수 있게 global 선언
    
    q = deque() #덱으로 선언
    q.append(position) #시작좌표 넣어주기
    visit = [[-1]*max_col for _ in range(max_row)] #방문 표시할 빈배열
    visit[position[0]][position[1]] = 0 #visit에 시작좌표 방문처리 1로 바꿈

    move_list = [[1,0],[-1,0],[0,1],[0,-1]] #현위치에서 탐색할 4방향 델타

    while q: #q에 값이 있다면 계속 반복
        before = q.popleft() #가장 먼저 들어왔던 값을 꺼내줌 (bfs니까!)
        for r, c in move_list: #위에서 선언한 델타와 for문 사용해서 4방향 탐색
            new_r, new_c = before[0] + r, before[1] + c
            #탐색할 좌표가 지도를 벗어나지는 않는지, 이미 방문했던 곳은 아닌지 확인
            if (0<=new_r<max_row) and (0<=new_c<max_col) and (visit[new_r][new_c] == -1):
                if gold_map[new_r][new_c] == "L": #탐색한 곳이 "L"인지 확인
                    q.append([new_r, new_c]) #"L"이라면 추가로 탐색을 이어가야하니 q에 추가해줌
                    visit[new_r][new_c] = visit[before[0]][before[1]] + 1 #방문표시도 해줌
                    max_long = max(max_long, visit[new_r][new_c]) #바로바로 max_long과 비교하며 최장거리도 최신화 해줌


max_row, max_col = map(int, input().split()) #지도의 최대행, 최대열
gold_map = [list(input()) for _ in range(max_row)] #보물지도

max_long = -1 #출력할 값, 최대 이동거리

for row in range(max_row): #보물지도 순회
    for col in range(max_col): #보물지도 순회
        if gold_map[row][col] == "L": #순회하던 중 현위치의 값이 "L"인 곳을 발견하면 bfs 실행
            position = [row, col]
            bfs(position) #현재위치 좌표를 넣고 bfs 실행
print(max_long) #bfs 탐색이 완료되고 최종 max_long 출력