n = int(input()) #체스판의 크기 (n x n)

def find_mini_set(start_row, max_col): #조건에 만족하는 부분집합을 찾기위한 함수
    global how_many #전역에 있는 how_many를 수정하기 위해 global 선언
    if start_row == (max_row): #탐색하는 행 인덱스가 최대값을 넘어가면 중단 (조건을 만족하는 하나의 부분집합이 완성되었다는 뜻)
        how_many += 1 #찾고있는 부분집합 수량 + 1
        # print(mini_set) #완성된 부분집합 출력 / 잘 작동하는지 확인용, 실제로는 필요없음
        return
    for i in range(max_col): #열마다 반복하며 작업 수행
        if visit_col[i] != 1: #해당 열이 방문했던 열인지 검사, 방문하지 않았다면 작업 수행
            visit_col[i] = 1 #방문 표시
            # mini_set[start_row][i] = 1 #부분집합을 위한 빈배열의 현재 행과 열에 1표시
            find_mini_set(start_row+1, max_col) #다음 열로 이동하여 재탐색
            # mini_set[start_row][i] = 0 #다음열으로 넘어가기 전에 원상복구 시켜줌
            visit_col[i] = 0 #다음열으로 넘어가기 전에 원상복구 시켜줌

max_row = n #체스판 행의 개수
max_col = n #체스판 열의 개수
start_row = 0 #탐색할 행의 인덱스
# mini_set = [[0] * max_col for _ in range(max_row)] #부분집합을 만들기 위한 빈배열 / 잘 작동하는지 확인용, 실제로는 필요없음
visit_col = [0] * max_col # 열에 방문한적 있는지 체크하기 위한 리스트
how_many = 0  #조건에 해당하는 부분집합의 수량을 표시 - 출력할 값

find_mini_set(start_row, max_col)

print(how_many)