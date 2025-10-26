import sys

input = sys.stdin.readline

H, W = map(int, input().split())
heights = list(map(int, input().split()))

if W < 3:
    print(0)
    sys.exit()

L = [0] * W
R = [0] * W

# 왼쪽 최대
L[0] = heights[0]
for i in range(1, W):
    L[i] = max(L[i-1], heights[i])

# 오른쪽 최대
R[W-1] = heights[W-1]
for i in range(W-2, -1, -1):
    R[i] = max(R[i+1], heights[i])

# 고이는 물 합연산
ans = 0
for i in range(W):
    ans += max(0, min(L[i], R[i]) - heights[i])

print(ans)
