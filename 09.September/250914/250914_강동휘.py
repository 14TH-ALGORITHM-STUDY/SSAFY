import sys
from collections import deque

sys.stdin = open("20303.halloween_bully.txt", "r")

# --- 문제 & 기본 조건 ---
# 친구의 사탕을 뺏는다
# 친구의 친구까지 사탕을 뺏는다
# K명 이상이 울기 시작하면 안된다.
# 최대로 뺏을 수 있는 사탕 수
# N은 정점의 수
# M은 간선의 수

# --- 문제 설계 ---
#


def bfs(s):

    if visited[s]:
        return

    q = deque([s])
    visited[s] = True
    cnt = 0
    total = 0

    while q:
        cur = q.popleft()
        cnt += 1
        total += candy[cur]

        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)

    groups.append((cnt, total))


N, M, K = map(int, input().split())
candy = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N + 1)
groups = []  # 아이수, 사탕 수

for i in range(1, N + 1):
    bfs(i)
# print(groups)

dp = [0] * (K + 1)

for child_cnt, total_candy in groups:
    for i in range(K, child_cnt - 1, -1):
        dp[i] = max(dp[i], dp[i - child_cnt] + total_candy)

print(max(dp) if K > 0 else 0)
