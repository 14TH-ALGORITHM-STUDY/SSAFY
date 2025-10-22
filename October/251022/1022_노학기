from collections import deque

n, k = map(int, input().split())
belt = deque(map(int, input().split()))
robot = deque([0] * n)
result = 0
zero_count = belt.count(0)

while True:
    result += 1

    # 1. 벨트 회전한다.
    belt.rotate(1)
    robot.rotate(1)
    robot[-1] = 0  # 내리는 위치에 도달한 경우, 즉시 내림

    # 2. 로봇 이동하기.
    for i in range(n - 2, -1, -1):
        if belt[i + 1] >= 1 and robot[i + 1] == 0 and robot[i] == 1:
            robot[i + 1] = 1
            robot[i] = 0
            belt[i + 1] -= 1
            if belt[i + 1] == 0:  # 0이 되었는지 확인
                zero_count += 1

    robot[-1] = 0  # 내리는 위치에 도달한 경우, 즉시 내림

    # 3. 올리는 위치에 로봇 올리기
    if belt[0] >= 1 and robot[0] == 0:
        robot[0] = 1
        belt[0] -= 1
        if belt[0] == 0:  # 0이 되었는지 확인
            zero_count += 1

    # 4. 내구도 0인 칸 수가 k이상이면 종료
    if zero_count >= k:
        break

print(result)
