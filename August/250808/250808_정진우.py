N, M = map(int, input().split())  # 물건 개수, 최대 무게
items = [list(map(int, input().split())) for _ in range(N)]  # [무게, 가치]

# 각 아이템에 priority 부여
for i in range(N):
    weight, value = items[i]
    items[i].append(value / weight)  # [weight, value, priority]

# priority 기준으로 내림차순 정렬
items.sort(key=lambda x: x[2], reverse=True)

max_value = 0

def dfs(idx, total_weight, total_value):
    global max_value

    if total_weight > M:
        return  # 무게 초과 → 가지치기
    max_value = max(max_value, total_value)

    if idx == N:
        return  # 모든 아이템 탐색 완료

    # 현재 idx 아이템을 선택하는 경우
    dfs(idx + 1, total_weight + items[idx][0], total_value + items[idx][1])

    # 현재 idx 아이템을 선택하지 않는 경우
    dfs(idx + 1, total_weight, total_value)

dfs(0, 0, 0)
print(max_value)
