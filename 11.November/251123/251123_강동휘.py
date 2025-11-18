T = int(input())
for _ in range(T):
    N = int(input())

    dp = [[0] * 4 for _ in range(n + 1)]

    if N >= 1:
        for k in range(1, N + 1):
            dp[k][1] = 1
            dp[k][2] = k // 2 + 1
            
            if k <= 3:
                dp[k][3] = k
            else:
                dp[k][3] = dp[k][2] + dp[k - 3][3]

    print(dp[N][3])