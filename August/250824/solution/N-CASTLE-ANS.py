N = int(input())
DAT = [0] * 10
cnt = 0

def func(row):
    global cnt
    # 기저 조건 -> N개의 행에 모두 배치 완료
    if row == N:
        cnt += 1
        return
    
    # 현재 행에서 모든 열 탐색
    for col in range(N):
        # 가지치기 -> 이미 이 열에 castle을 두었다면 continue
        if DAT[col] == 1:
            continue
        DAT[col] = 1   # 현재 행에서 col열에 castle을 둔다
        func(row + 1)  # 다음 행으로 이동
        DAT[col] = 0   # 백트래킹 (놓았던 거 해제)

func(0)
print(cnt)