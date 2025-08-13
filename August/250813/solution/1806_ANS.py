import sys
input = sys.stdin.readline

N, S = map(int, input().split())
A = list(map(int, input().split()))

INF = 10**9
ans = INF

L = 0
cur = 0

# 더블 포인터
# n은 배열의 길이
# r = 오른쪽 인덱스
for R in range(N):
    # current = 현재 배열안에 있는 수들의 합
    cur += A[R]\
    
    #[5]

    # cur > 15
    while cur >= S:
        # 현재 배열의 길이와 초기화값 최대값을 비교해서 ans변수
        ans = min(ans, R - L + 1)
        cur -= A[L]
        L += 1

print(0 if ans == INF else ans)
