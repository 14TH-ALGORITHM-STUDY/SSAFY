import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 제한 늘리기

# 입력 받기
N, K = map(int, input().split())  # N: 물건 개수, K: 배낭 최대 무게
items = [(0, 0)]  # (weight, value), 인덱스 1부터 사용
for _ in range(N):
    w, v = map(int, input().split())
    items.append((w, v))

# 메모이제이션 테이블 (-1: 아직 계산 안 함)
dp = [[-1] * (K + 1) for _ in range(N + 1)]

def knapsack(i, w):
    """
    i: 현재 고려 중인 물건 번호
    w: 남은 배낭 용량
    반환: i번째 물건부터 고려했을 때 얻을 수 있는 최대 가치
    """
    # **기저 사례**: 물건이 없거나, 용량이 0이면 가치 0
    if i == 0 or w == 0:
        return 0

    # 이미 계산한 적 있으면 그대로 반환
    if dp[i][w] != -1:
        return dp[i][w]

    weight, value = items[i]

    if weight > w:
        # 현재 물건이 배낭에 안 들어가는 경우 → 그냥 안 담음
        dp[i][w] = knapsack(i - 1, w)
    else:
        # 두 경우 중 더 가치가 큰 걸 선택
        dp[i][w] = max(
            knapsack(i - 1, w),               # 현재 물건 안 담음
            knapsack(i - 1, w - weight) + value  # 현재 물건 담음
        )

    return dp[i][w]

# 최종 결과 출력
print(knapsack(N, K))
