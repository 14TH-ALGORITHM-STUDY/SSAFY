from collections import deque


# bfs로 친구 무리 단위별로 탐색
def bfs(stt):
    q = deque([stt])
    visited[stt] = True
    count = 1  # 무리의 인원 수
    sum_value = arr[stt]  # 그 무리의 사탕 합 수

    while q:
        cu_stt = q.popleft()
        for w in G[cu_stt]:
            if not visited[w]:
                visited[w] = True
                q.append(w)
                count += 1
                sum_value += arr[w]
    return (count, sum_value)


N, M, K = map(int, input().split())  # 길바닥 아이들 수, 아이 친구 묶음, 공명시작
arr = [0] + list(map(int, input().split()))  # 각 아이들의 사탕 개수
G = [[] for _ in range(N + 1)]  # 그래프 생성
for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
    # print(G)
visited = [False] * (N + 1)
arr_list = []

for i in range(1, N + 1):
    if not visited[i]:
        arr_list.append(bfs(i))
print(arr_list)

###########내가 풀려고 했던 풀이 (오답임) #######################
# result = 0
# for i in range(len(arr_list)):
#     peole = 0
#     value = 0
#     for j in range(len(arr_list)):
#         peole += arr_list[j][0]
#         value += arr_list[j][1]
#         if peole <= K:
#             result = max(result, value)
# print(result)
################################################################


####################전문가 정답##################################
dp = [0] * K  # dp[x] = 인원 x명 모았을 때 얻을 수 있는 최대 사탕 수
for people, candy in arr_list:  # 무리 하나씩 넣어보면서
    for i in range(K - 1, people - 1, -1):  # 역순으로 갱신
        dp[i] = max(dp[i], dp[i - people] + candy)

print(max(dp))  # 최댓값 출력
