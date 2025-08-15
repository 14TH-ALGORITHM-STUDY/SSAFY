# r: 행의 수, c: 열의 수, q: 구해야하는 영역이 수
r, c, q = map(int, input().split())

#light_map : 그림의 각 픽셀의 밝기 정보 (인덱스를 맞추기 위해 0으로만 이루어진 1행, 1열 추가)
light_map = [[0] * (c+1)] #0으로만 이루어진 행 생성 (1행)
row_data = [[0] + list(map(int, input().split())) for _ in range(r)] #입력값 추가 (가장 앞에 [0] : 모든 값이 0인 1열)
for data in row_data:
    light_map.append(data)
 
# light_map을 각 행,열의 누적합 방식으로 변경
for row in range(1, r+1):
    for col in range(1, c+1):
        light_map[row][col] = light_map[row-1][col] + light_map[row][col-1] - light_map[row-1][col-1] + light_map[row][col]

for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split()) #측정영역의 왼쪽상단, 오른쪽하단 좌표값 입력
    sum_all = light_map[r2][c2] #측정 영역의 가장 오른쪽 아래 픽셀의 값
    sum_for_minus1 = light_map[r2][c1-1] #제거할 부분 1
    sum_for_minus2 = light_map[r1-1][c2] #제거할 부분 2
    sum_for_plus = light_map[r1-1][c1-1] #중복으로 제거되어 추가할 부분

    avg = (sum_all - sum_for_minus1 - sum_for_minus2 + sum_for_plus)//((r2-r1+1)*(c2-c1+1))
    print(avg)