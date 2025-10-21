'''
문제 조건 → 시뮬레이션 
1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전
2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동, 만약 이동할 수 없다면 이동 X
    1. 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 함
3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올림
4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정 종료, 그렇지 않으면 1번으로 돌아감
'''

'''
# deque
## rotate

a = deque([1, 2, 3, 4, 5])
print(a)
a.rotate(1) # 오른쪽으로 이동 == 제일 뒤에 있던 게 제일 앞으로 이동
print(a)

# 출력 결과
deque([1, 2, 3, 4, 5])
deque([5, 1, 2, 3, 4])

a.rotate(-1) # 왼쪽으로 이동 == 제일 앞에 있던 게 제일 뒤로 이동
print(a)

# 출력 결과
deque([2, 3, 4, 5, 1])

'''
from collections import deque

def robot_on_belt(N, K, A_array):
    answer = 0
    belt = deque([False] * N)

    while True:
        answer += 1

        # 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전
        A_array.rotate(1) 
        belt.rotate(1)
        belt[N-1] = False # 로봇이 내리는 위치에 도달하면 즉시 내림

        # 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동, 만약 이동할 수 없다면 이동 X
        for i in range(N-2, -1, -1):
            # 2-1. 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 함
            if belt[i] and not belt[i+1] and A_array[i+1] > 0:
                belt[i], belt[i+1] = False, True
                A_array[i+1] -= 1

        belt[N-1] = False # 이동 후 다시 로봇이 내리는 위치에 도달한 경우 check

        # 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올림
        if A_array[0] > 0:
            belt[0] = True
            A_array[0] -= 1

        # 4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정 종료, 그렇지 않으면 1번으로 돌아감
        if A_array.count(0) >= K:
            break

    return answer

N, K = map(int, input().split())
A_array = deque(list(map(int, input().split())))

ans = robot_on_belt(N, K, A_array)
print(ans)