from collections import deque

def bfs(position):
    global how_long #시간이 얼마나 걸렸는지 저장할 변수
    global eat #먹은 물고기의 수를 저장할 변수
    global shark_size #아기 상어의 크기
    visit = [[-1] * n for _ in range(n)] #방문했는지 확인할 배열
    visit[position[0]][position[1]] = 0 #시작위치의 값은 0으로 변경
    q = deque() #큐
    q.append(position) #큐에 초기위치 넣기
    move_list = [(-1,0),(0,-1),(0,1),(1,0)] #4방향 델타
    most_short = n**2 #탐색 중 가장 짧은 시간을 저장
    find_fish_r = n #탐색 중 현재까지 가장 유력한 다음 위치의 행값
    find_fish_c = n #탐색 중 현재까지 가장 유력한 다음 위치의 열값

    while q: #큐에 값이 있을 때까지
        mom = q.popleft() #초기값 꺼내기
        for r, c in move_list: #초기 위치에서 갈 수 있는 곳 탐색(4방향)
            new_r = r + mom[0]
            new_c = c + mom[1]
            if (0<= new_r <n) and (0<= new_c <n) and (fish_map[new_r][new_c]<=shark_size) and (visit[new_r][new_c]==-1): #이동할 수 있는 곳인지 확인
                if 1<=fish_map[new_r][new_c]<shark_size: #상어보다 크기가 작은 물고기라면(먹을 수 있다면) 가장 조건에 부합하는지 확인한다.
                    if most_short < visit[mom[0]][mom[1]] +1: #현재까지 찾은 가장 짧은 거리보다 멀다면 탐색 종료 (이후로는 탐색해도 어차피 거리가 더 길어질테니!)
                        how_long += most_short #걸린 시간 추가해줌
                        eat += 1 #먹은 물고기 수 추가
                        fish_map[find_fish_r][find_fish_c] = 9 #이동한 상어의 위치 최신화
                        fish_map[position[0]][position[1]] = 0 #이동 전 상어의 위치 0으로 변경
                        if shark_size == eat: #먹은 물고기랑 상어 크기가 같으면 상어 크기 1 올려줌
                            shark_size += 1
                            eat = 0
                        return [find_fish_r, find_fish_c] #물고기를 먹은 위치 반환
                    
                    elif most_short > visit[mom[0]][mom[1]] +1: #현재까지 찾은 가장 짧은 거리보다 짧다면 거리, 좌표 최신화 (거리가 가장 가까우니 다른 조건 볼거 없이 1등 후보)
                        most_short = visit[mom[0]][mom[1]] +1 #거리 최신화
                        find_fish_r = new_r #좌표 최신화
                        find_fish_c = new_c #좌표 최신화
                    elif most_short == visit[mom[0]][mom[1]] +1: #현재까지 찾은 가장 짧은 거리와 같다면 다른 조건 확인해봐야함
                        if find_fish_r > new_r: #행이 더 높은지 확인
                            find_fish_r = new_r #높다면 좌표 최신화 (행이 높다면 열은 안봐도 됨)
                            find_fish_c = new_c
                        elif find_fish_r == new_r: #행도 같다면 열이 더 왼쪽인지 확인
                            if find_fish_c > new_c:
                                find_fish_r = new_r #더 왼쪽이라면 좌표 최신화
                                find_fish_c = new_c
                else:
                    q.append([new_r, new_c]) #1칸 이내 먹을 수 있는 물고기가 없다면 계속 반복 진행, 큐에 더해주기
                    visit[new_r][new_c] = visit[mom[0]][mom[1]] +1 #걸린 시간 표시
    
    if most_short != n**2: #물고기가 하나밖에 없었다면 위의 while문에서 return이 되지 않기 때문에 while문 끝나고 return작업 한번 더 실시
        #while문에서 return이랑 같은 작업!
        how_long += most_short #걸린 시간 추가해줌
        eat += 1 #먹은 물고기 수 추가
        fish_map[find_fish_r][find_fish_c] = 9 #이동한 상어의 위치 최신화
        fish_map[position[0]][position[1]] = 0 #이동 전 상어의 위치 0으로 변경
        if shark_size == eat: #먹은 물고기랑 상어 크기가 같으면 상어 크기 1 올려줌
            shark_size += 1
            eat = 0
        return [find_fish_r, find_fish_c] #물고기를 먹은 위치 반환
    else:
        return None

n = int(input())

fish_map = [list(map(int, input().split())) for _ in range(n)] #물고기 배열

shark_size = 2 #아기상어의 크기
s_shark = [0,0] #아기상어의 시작 위치

how_long = 0 #시간이 얼마나 걸렸는지
eat = 0 #먹은 물고기의 수

#아기상어의 시작 위치, 물고기 수 찾기
for r in range(n):
    for c in range(n):
        if fish_map[r][c] == 9:
            s_shark[0] = r
            s_shark[1] = c

while True:
    result = bfs(s_shark)

    if result == None: #먹을 수 있는 물고기가 없을 때
        print(how_long) #걸린 시간을 출력
        break
    else: #먹을 수 있는 물고기가 있다면
        s_shark = result #s_shark에 현재 상어좌표 대입

