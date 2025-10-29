import sys

input = sys.stdin.readline

N = int(input())
a = list(map(int, input().split()))

a.sort()
cnt = 0
for i in range(N):

    l = 0
    r = N - 1
    target = a[i]

    is_good = False
    while l < r:
        if l == i:
            l += 1
            continue
        if r == i:
            r -= 1
            continue

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
