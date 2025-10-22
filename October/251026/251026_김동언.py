# 시간초과 발생... 포기

# 재귀 깊이 한도 수정
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find_pool(left, right):
    global cnt
    if len(height[left+1:right]) == 0:
        return
    inner_max = max(height[left+1:right])
    inner_max_idx = height.index(inner_max)
    out_min = min(height[left], height[right])
    if inner_max <= out_min:
        for idx in range(left+1, right):
            cnt_plus = out_min - height[idx]
            cnt += cnt_plus
    else:
        find_pool(left, inner_max_idx)
        find_pool(inner_max_idx, right)


h, w = map(int, input().split())

height = list(map(int, input().split()))

cnt = 0

find_pool(0, w-1)

print(cnt)