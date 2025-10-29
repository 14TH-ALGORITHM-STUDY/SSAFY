# # 백준 제출 시 채점 64%까지 진행 후 시간초과 발생

# # r: 행의 수, c: 열의 수, q: 구해야하는 영역이 수
# r, c, q = map(int, input().split())

# #그림의 각 픽셀의 밝기 정보 (인덱스를 맞추기 위해 0으로만 이루어진 1행, 1열 추가)
# light_map = [[0] * (c+1)] #0으로만 이루어진 행 생성
# row_data = [[0] + list(map(int, input().split())) for _ in range(r)] #입력값 추가
# for data in row_data:
#     light_map.append(data)

# for _ in range(q):
#     sum = 0 #측정 픽셀의 밝기 합
#     cnt = 0 #측정 픽셀의 수
#     r1, c1, r2, c2 = map(int, input().split()) #측정영역의 왼쪽상단, 오른쪽하단 좌표값 입력
#     for row in range(r1, r2+1):
#         for col in range(c1, c2+1):
#             sum += light_map[row][col]
#             cnt += 1
#     avg = sum//cnt #측정 픽셀의 밝기 평균
#     print(avg)

#==========================================================================================


# 백준 제출 시 채점 80%쯤까지 진행 후 시간초과 발생

# r: 행의 수, c: 열의 수, q: 구해야하는 영역이 수
r, c, q = map(int, input().split())

#light_map : 그림의 각 픽셀의 밝기 정보 (인덱스를 맞추기 위해 0으로만 이루어진 1행, 1열 추가)
light_map = [[0] * (c+1)] #0으로만 이루어진 행 생성 (1행)
row_data = [[0] + list(map(int, input().split())) for _ in range(r)] #입력값 추가 (가장 앞에 [0] : 모든 값이 0인 1열)
for data in row_data:
    light_map.append(data)
 
# light_map을 각 행별로 누적합 방식으로 변경
for row in range(1, r+1):
    for col in range(1, c+1):
        light_map[row][col] += light_map[row][col-1]

for _ in range(q):
    sum_all = 0 #측정 픽셀이 포함된 행의 밝기 합
    sum_for_minus = 0 #측정 픽셀이 포함된 행 중 측정 영역이 아닌 부분의 합
    r1, c1, r2, c2 = map(int, input().split()) #측정영역의 왼쪽상단, 오른쪽하단 좌표값 입력
    for row in range(r1, r2+1):
        sum_all += light_map[row][c2]
        sum_for_minus += light_map[row][c1-1]

    avg = (sum_all - sum_for_minus)//((r2-r1+1)*(c2-c1+1))
    print(avg)