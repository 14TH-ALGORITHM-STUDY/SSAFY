# N 벨트
# 2N벨트가 감싸고있음
#로봇을 올리거나 이동 시, 내구도 1 감소
# 회전방향으로 한칸 이동
# 다음칸에 로봇이 없고, 내구도가 1 이상이여야 옮길 수 있음
# 0의 개수가 K 이상이면 끝



from collections import deque

def solve(N, K, Ai):
    belt = deque(Ai)
    robot = deque([False] * N) # N번째에서 로봇 내림
    cnt = 0

    while True:
        cnt += 1

        v_belt = belt.pop()
        belt.appendleft(v_belt)
        v_robot = robot.pop()
        robot.appendleft(v_robot)
        robot[-1] = False

        for i in range(N-2, -1, -1): # N번째 컨베이어 인덱스 N-1임. 내리는칸.
            #현재칸에 로봇이 있고, 다음칸에 로봇 없고, 내구도가 1 이상
            if robot[i] and not robot[i +1] and belt[i+1]>0:
                robot[i] = False #다음칸으로 로봇이가서 현재칸 빔
                robot[i+1] = True #로봇이 와서 차있음
                belt[i+1] -= 1 #내구도 감소
        robot[-1] = False #N번째 칸에서 로봇이 내림

        # 로봇 올리기
        if belt[0] >0:
            robot[0] = True
            belt[0] -= 1
        
        if belt.count(0) >= K:
            return cnt
    

N, K = map(int, input().split()) # N 컨베어 절반, K 내구도
Ai = list(map(int, input().split())) # 컨베이어 내구도
result = solve(N, K, Ai)
print(result)



