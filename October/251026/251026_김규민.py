# 비가온다. 얼마나 고이는지?
# 세로길이 H, 가로길이 W
# 바닥은 항상 막혀있음 
# 벽이 있는곳은 1 없는 곳은 0 인 배열 새로 만들기
# 1. 처음 1을만나고부터 0 카운팅 시작
# 2. 다음 1을 만나면 0카운팅 한 것 담기
# 3. 다시 1을 만나면 카운팅 새로 시작
# 4. 다음 1을 만나면 0카운팅 한 것 담기
## 1, 2, 3, 4 반복


H, W = map(int, input().split())
arr = list(map(int, input().split()))

# 벽 1, 없는 곳 0인 배열 만들 곳
new_arr = [[0] * W for _ in range(H)]

# 벽 채우기
for col in range(W):
    for row in range(arr[col]):
        new_arr[row][col] = 1 
# print(new_arr)

result = 0 #누적할 최종 결과

# 행별로 돌면서 0 개수 카운팅하기
for r in range(H):
    cnt = 0 # 0 누적할 그릇
    started = False  # 벽 만남 여부

    for c in range(W):
        if new_arr[r][c] == 1: # 벽 만남 // 다시 벽 만난 경우
            started = True     # 벽 만남 체크
            if started:        # 벽을 만난 후로
                result += cnt  # 0 개수 카운팅했던 것 담기
            
            cnt = 0            # 초기화
        else:                  # 0인 경우
            if started:        # 벽을 만난 상태에서
                cnt += 1       # 0의 개수 카운팅

print(result)





