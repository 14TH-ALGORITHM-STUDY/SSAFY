T = int(input())

# dp[i] = 1로 초기화
dp = [1] * 10001

# 2를 사용하는 경우 추가
for i in range(2, 10001):
    dp[i] += dp[i-2]

# 3을 사용하는 경우 추가
for i in range(3, 10001):
    dp[i] += dp[i-3]

for _ in range(T):
    n = int(input())
    print(dp[n])