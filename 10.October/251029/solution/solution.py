# 백준 1253 좋다 solution
# 문제 도입부
N = int(input())
a = list(map(int, input().split()))

# 기본 아이디어
a.sort()
cnt = 0
for i in range(N):

    # 투 포인터와 타겟 정의
    l = 0
    r = N - 1
    target = a[i]

    # 반복 횟수가 정해져 있지 않고
    # 재귀 깊이가 충분히 크다
    # while 사용
    # 종료 조건: l가 r이 교차하기 전까지 반복 탐색
    is_good = False
    while l < r:
        # 불가능 조건
        if l == i:
            l += 1
            continue
        if r == i:
            r -= 1
            continue

        # 판별식
        s = a[l] + a[r]
        if s == target:
            is_good = True
            break
        elif s < target:
            l += 1
        else:
            r -= 1

    if is_good:
        cnt += 1

print(cnt)
