'''
입력 예시:
4 3 5
25 93 64
10 29 85
80 63 71
99 58 86
2 2 2 3
3 2 3 3
1 2 2 2
1 2 4 3
2 3 2 3

출력 예시:
57
67
61
68
85
'''


# r: 행의 수, c: 열의 수, q: 구해야하는 영역이 수
r, c, q = map(int, input().split())
'''
시간 제한: 1초

입력값 범위:
1 <= r, c <= 1,000
1 <= q <= 10,000

조건 분석:
q의 개수만큼 직사각형 영역의 평균을 구해야함
q가 최대 10,000까지 입력 가능
매번 직사각형 영역의 값을 하나 하나 더하는 작업 시
r * c * q = 10^3 * 10^3 * 10^4
초당 약 1억 연산 가정, 10^10은 100초
매번 직사각형의 합을 구하면 무조건 시간초과
직사각형 합 구하는 다른 방법을 찾아야함
2차원 누적합으로 문제풀이
'''

#light_map : 그림의 각 픽셀의 밝기 정보 (인덱스를 맞추기 위해 0으로만 이루어진 1행, 1열 추가)
light_map = [[0] * (c+1)] #우선 0으로만 이루어진 행 생성 (1행)
row_data = [[0] + list(map(int, input().split())) for _ in range(r)] #행 추가 (가장 앞에 [0] : 모든 값이 0인 1열을 만들기 위해서)
for data in row_data:
    light_map.append(data)
'''
행과 열 인덱스는 0부터 시작인데, 문제에서는 행과 열이 1부터 시작
그래서 편의를 위해 0으로 이루어진 1행, 1열을 추가

 0 0 0 0
 0 2 5 1
 0 1 3 5
 0 3 4 2
'''
 
# light_map을 누적합 방식으로 변경
for row in range(1, r+1):
    for col in range(1, c+1):
        light_map[row][col] = light_map[row-1][col] + light_map[row][col-1] - light_map[row-1][col-1] + light_map[row][col]
'''
매번 직사각형 영역의 값을 하나씩 계산하면 시간초과
그래서 누적합을 계산하여 light_map을 변경

0 0 0  0
0 2 7  8
0 3 11 17
0 6 18 26

(1,1)은 (0,0) (0,1) (1,0) (1,1)의 합 : 0 + 0 + 0 + 2 = 2
(3,1)은 (0,0) (0,1) (1,0) (1,1) (2,0) (2,1)의 합 : 0 + 0 + 0 + 2 + 0 + 1 = 3

light_map[row-1][col] : 구하고자 하는 자리의 위쪽 모든 행, 구하고자 하는 자리의 열을 포함한 왼쪽 모든 열의 값의 합
                        0 0 0 0 X
                        0 0 0 0 X
                        0 0 0 0 X
                        X X X # X
                        X X X X X
light_map[row][col-1] : 구하고자 하는 자리의 왼쪽 모든 열, 구하고자 하는 자리의 행을 포함한 위쪽 모든 열의 값의 합
                        0 0 0 X X
                        0 0 0 X X
                        0 0 0 X X
                        0 0 0 # X
                        X X X X X
light_map[row-1][col-1] : 구하고자 하는 자리의 행과 열을 제외한 왼쪽과 위쪽의 모든 값의 합 (light_map[row-1][col]과 light_map[row][col-1]의 중복된 영역, 그래서 다시 한번 더해줘야함)
                        0 0 0 X X
                        0 0 0 X X
                        0 0 0 X X
                        X X X # X
                        X X X X X
light_map[row][col] : 자기 자신은 미포함되었기 때문에 본인 더하기
'''

for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split()) #측정영역의 왼쪽상단, 오른쪽하단 좌표값 입력
    sum_all = light_map[r2][c2] #측정 영역의 가장 오른쪽 아래 픽셀의 값
    sum_for_minus1 = light_map[r2][c1-1] #제거할 부분 1
    sum_for_minus2 = light_map[r1-1][c2] #제거할 부분 2
    sum_for_plus = light_map[r1-1][c1-1] #중복으로 제거되어 추가할 부분

    avg = (sum_all - sum_for_minus1 - sum_for_minus2 + sum_for_plus)//((r2-r1+1)*(c2-c1+1))
    print(avg)

'''
누적합을 이용하여 4번의 연산으로 직사각형의 평균을 계산

구하고자 하는 영역:
            X X X X X
            X X X X X
            X X 0 0 X r1
            X X 0 0 X r2
            X X X X X
               c1 c2
sum_all = light_map[r2][c2] : (r2, c2)의 행과 열을 포함한 왼쪽과 위쪽 모든 값의 합
            0 0 0 0 X
            0 0 0 0 X
            0 0 0 0 X     r1
            0 0 0 0(#) X  r2
            X X X X X
               c1 c2
sum_for_minus1 = light_map[r2][c1-1] : r2를 포함하는 그 위의 모든 행과 c1의 왼쪽 모든 열이 겹치는 값의 합
            0 0 X X X
            0 0 X X X
            0 0 # # X r1
            0 0 # # X r2
            X X X X X
               c1 c2
sum_for_minus2 = light_map[r1-1][c2] : r1의 위쪽 모든 행과 c2를 포함하는 그 왼쪽 행이 겹치는 값의 합
            0 0 0 0 X
            0 0 0 0 X
            X X # # X r1
            X X # # X r2
            X X X X X
               c1 c2
sum_for_plus = light_map[r1-1][c1-1 : r1의 위쪽 모든 행과 c1의 왼쪽 모든 열이 겹치는 값의 합 (sum_for_minus1과 sum_for_minus2의 겹치는 영역 중복으로 제거되어 다시 한번 추가해야함 )
            0 0 X X X
            0 0 X X X
            X X # # X r1
            X X # # X r2
            X X X X X
               c1 c2
'''