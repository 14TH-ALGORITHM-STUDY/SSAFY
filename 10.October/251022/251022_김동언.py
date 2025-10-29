# 이번에도 이거 안해주니까 시간초과나네
import sys
input = sys.stdin.readline

# n: 컨베이어벨트 길이, k: 내구성이 0인 칸의 개수가 k가 되면 중단
n, k = map(int, input().split())

# 내구성 리스트
level = list(map(int, input().split()))

# 내구성이 0인 칸의 수 카운트
level_0 = 0

# 시작점 이후 각 인덱스에 로봇이 있는지 유무
robot = [False] * n

# 시작점 인덱스
start_idx = 0

# 단계 최신화 할 변수
cnt = 0

# 내구성이 0인 칸이 k개 이상이 되면 멈춘다.
while level_0<k:
    # 단계 + 1
    cnt += 1

    #컨베이어 벨트를 회전시킨다 -> 로봇을 올리는 시작점의 인덱스가 한칸 후퇴한다.
    start_idx = (start_idx - 1 + (n*2)) % (n*2)
    
    # 로봇 위치 변경해야함 - GPT 도움
    # 컨베이어 벨트가 회전하면서 발생하는 로봇의 위치 변화!
    for robot_idx in range(n-1,0,-1):
        robot[robot_idx] = robot[robot_idx-1]
    robot[0] = False
    robot[n-1] = False

    # 로봇이 스스로 움직이며 발생하는 로봇의 위치 변화
    for idx in range(n-1,0,-1):
        # 마지막 조건 : robot[idx-1]에 로봇이 있어야 다음 칸으로 옮길 수 있으니 확인해야함 - GPT 도움
        # 이동할 칸의 내구성이 0인가? 이동할 칸에 로봇이 이미 있는가? 이동시킬 로봇이 있는가? 조건을 모두 만족하면 로봇을 이동
        if level[(start_idx + idx)%(2*n)] != 0 and robot[idx] == False and robot[idx-1] == True:
            robot[idx] = robot[idx-1]
            # 이동했으니 이전 칸에 로봇이 없는 것으로 상태 변경
            robot[idx-1] = False
            # 이동한 칸의 내구성 -1
            level[(start_idx + idx)%(2*n)] -= 1
            # 내구성이 0이 되었다면 level_0을 +1해서 최신화
            if level[(start_idx + idx)%(2*n)] == 0:
                level_0 += 1

    # 시작점의 내구성이 0이 아니라면 시작점에 로봇을 올린다.
    if level[start_idx] != 0:
        # 올렸으니 내구성 -1
        level[start_idx] -= 1
        # 해당 인덱스에 로봇을 올렸다고 표시
        robot[0] = True
        # 내구성이 0이 되었다면 level_0을 +1해서 최신화
        if level[start_idx] == 0:
            level_0 += 1

print(cnt)