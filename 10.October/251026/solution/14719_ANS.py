h, w = map(int, input().split())

height = list(map(int, input().split()))

left_max = [0] * w
right_max = [0] * w

left_max[0] = height[0]
right_max[w-1] = height[w-1]

for idx_left in range(1, w):
    left_max[idx_left] = max(left_max[idx_left-1], height[idx_left])

for idx_right in range(w-2,-1,-1):
    right_max[idx_right] = max(right_max[idx_right+1], height[idx_right])

total_water = 0

for idx in range(w):
    depth = min(left_max[idx], right_max[idx]) - height[idx]
    total_water += depth

print(total_water)