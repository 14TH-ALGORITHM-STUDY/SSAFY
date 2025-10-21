import sys
from collections import deque

input = sys.stdin.readline


def rotate():
    global step

    while True:
        step += 1

        # 1. 벨트와 로봇 회전
        # belt.appendleft(belt.pop())
        belt.rotate(1)
        # robots.appendleft(robots.pop())
        robots.rotate(1)
        robots[-1] = False  # 로봇을 벨트에서 내림

        # 2. 로봇 이동
        # 가장 먼저 올라간 로봇부터 이동
        for i in range(N - 2, -1, -1):  # (N - 2)번째 로봇부터
            # 이동할 수 없다면 -> 이미 로봇이 존재하거나 벨트 내구도가 없다면
            if not (robots[i] and not robots[i + 1] and belt[i + 1]):
                continue  # 가만히 있는다.
            robots[i] = False
            robots[i + 1] = True
            belt[i + 1] -= 1
        robots[-1] = False

        # 3. 로봇 올리기
        # 내구도가 0이 아니라면
        if belt[0] > 0 and not robots[0]:
            robots[0] = True
            belt[0] -= 1

        # 4. 종료 조건
        cnt = 0
        for n in belt:
            if n == 0:
                cnt += 1
        if cnt >= K:
            break


N, K = map(int, input().split())
belt = deque(map(int, input().split()))
robots = deque([False] * N)

step = 0
rotate()

print(step)
