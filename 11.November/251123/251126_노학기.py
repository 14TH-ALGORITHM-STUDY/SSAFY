lim = 10000

#########
# case1 #
#########
# 1. 모든 수를 1로만 만드는 경우는 1가지 (초기화)
dp = [1] * (lim + 1)

# 2. 2를 사용하여 만드는 경우를 누적
for i in range(2, lim + 1):
    dp[i] += dp[i - 2]

# 3. 3을 사용하여 만드는 경우를 누적
for i in range(3, lim + 1):
    dp[i] += dp[i - 3]

#########
# case2 #
#########
# dp = [0] * (lim + 1)
# dp[0] = 1
# for num in [1, 2, 3]:
#     for i in range(num, lim+1):
#         dp[i] += dp[i - num]

T = int(input())

for _ in range(T):
    n = int(input())
    print(dp[n])

# 순서가 중요하지 않을 때 (조합, 이 문제)
# 동전 종류가 바깥쪽 루프
for coin in [1, 2, 3]:
    for i in range(coin, n + 1):
        dp[i] += dp[i - coin]

# 순서가 중요할 때 (순열, 백준 9095번)
# 만드는 숫자 i가 바깥쪽 루프
for i in range(1, n + 1):
    for coin in [1, 2, 3]:
        if i >= coin:
            dp[i] += dp[i - coin]








