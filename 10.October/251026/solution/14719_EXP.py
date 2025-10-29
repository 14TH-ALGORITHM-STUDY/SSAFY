# h: 2차원 세계의 세로길이, w: 2차원 세계의 가로길이
h, w = map(int, input().split())
# ex) 10, 10

# 블록의 높이
height = list(map(int, input().split()))
# print(height)
# ex) [3, 5, 2, 4, 7, 9, 2, 10, 9, 5]

# 본인의 높이와 좌측/우측 블록들의 높이 중 가장 높은 블록의 높이 값
# left_max[i] : 0번부터 i번 인덱스까지의 최대 높이
# right_max[i] : i번부터 w-1번 인덱스까지의 최대 높이
# 아래 코드에서 하나씩 채워넣을 예정
left_max = [0] * w
right_max = [0] * w

# 0번째 인덱스와, w-1번째 인덱스는 각각 좌측과, 우측에 블록이 없으니 본인 높이로 초기화
left_max[0] = height[0]
right_max[w-1] = height[w-1]

# 본인의 포함한 좌/우측의 블록 중 가장 높은 값을 찾는다.
# 좌/우측의 모든 값을 하나하나 비교할 필요없다.
# 좌측의 경우 left_max[idx-1]이 좌측 블록 중 최대값이 보장되기 떄문에 left_max[idx-1]이랑 height[idx]만 비교하면 된다.
# 우측도 마찬가지 right_max[idx+1]와 height[idx]만 비교하면됨 최댓값을 구할 수 있다.
for idx_left in range(1, w):
    left_max[idx_left] = max(left_max[idx_left-1], height[idx_left])

for idx_right in range(w-2,-1,-1):
    right_max[idx_right] = max(right_max[idx_right+1], height[idx_right])
# ex)
#10                                        0        
#9                                 0       0   0    
#8                                 0       0   0    
#7                             0   0       0   0    
#6                             0   0       0   0    
#5                 0           0   0       0   0   0
#4                 0       0   0   0       0   0   0
#3             0   0       0   0   0       0   0   0
#2             0   0   0   0   0   0   0   0   0   0
#1             0   0   0   0   0   0   0   0   0   0
# height    = [3,  5,  2,  4,  7,  9,  2,  10, 9,  5]
#-----------------------------------------------------
# left_max  = [3,  5,  5,  5,  7,  9,  9,  10, 10, 10]
# right_max = [10, 10, 10, 10, 10, 10, 10, 10, 9,  5]
#-----------------------------------------------------
# depth     = [0,  0,  3,  1,  0,  0,  7,  0,  0,  0]
# depth = min(left_max, right_max) - height

# 빗물의 총량을 저장할 변수 (최종 출력값)
total_water = 0

# 빗물이 쌓이는 높이 : 좌측 블록들의 최대 높이와 우측 블록들의 최대 높이 중 낮은 높이까지 빗물이 쌓인다.
# 본인이 더 높다면 쌓일 수 없다.
# [0, 0, 3, 1, 0, 0, 7, 0, 0, 0]
for idx in range(w):
    depth = min(left_max[idx], right_max[idx]) - height[idx]
    total_water += depth

print(total_water)