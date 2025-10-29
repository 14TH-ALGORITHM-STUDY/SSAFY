# ----------------------------------------------------
# 백준 20303 할로윈의 양아치
# 핵심 아이디어:
#   1) 친구 관계를 그래프로 만들고
#   2) BFS/DFS로 연결된 "무리"들을 찾는다
#   3) 각 무리를 (인원수, 사탕합)으로 아이템화
#   4) 인원을 K명 미만만 데려갈 수 있으므로 cap=K-1
#   5) 0/1 배낭(DP)으로 최대 사탕 개수를 구한다
# ----------------------------------------------------

import sys
input = sys.stdin.readline   # 빠른 입력 (필수는 아님)

# [1] 입력 받기
N, M, K = map(int, input().split())       # N=아이 수, M=친구 관계 수, K=제한 인원수
candies = [0] + list(map(int, input().split()))  
# candies[1]~candies[N] = 각 아이가 가진 사탕 수
# 앞에 0을 넣은 이유: 아이 번호를 1부터 쓰려고 (인덱스 맞추기용)


# [2] 친구 그래프 만들기 (무방향) 
graph = [[] for _ in range(N + 1)]        # 인접 리스트 방식
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)                    # a의 친구에 b 추가
    graph[b].append(a)                    # b의 친구에 a 추가

# [3] BFS로 "무리(연결요소)" 찾기 
visited = [False] * (N + 1)               # 방문 체크
groups = []                               # (인원수, 사탕합) 저장

for i in range(1, N + 1):                 # 1번 아이부터 N번 아이까지 확인
    if not visited[i]:                    # 아직 방문 안 했으면 새로운 무리 시작
        queue = [i]                       # BFS 큐 초기화
        visited[i] = True
        count, total = 0, 0               # 현재 무리의 인원수, 사탕합

        while queue:                      # 큐가 빌 때까지 반복
            x = queue[0]                  # 큐 맨 앞 원소 꺼내기
            queue = queue[1:]             # (pop(0) 대신 슬라이싱 사용)
            count += 1                    # 무리 인원수 증가
            total += candies[x]           # 무리 사탕합 더하기

            # x의 친구들 확인
            for nxt in graph[x]:
                if not visited[nxt]:      # 아직 방문 안 한 친구라면
                    visited[nxt] = True   # 방문 처리
                    queue.append(nxt)     # 큐에 추가

        groups.append((count, total))     # 무리 완성 → (인원수, 사탕합) 저장


# [4] 0/1 배낭 DP 준비 
cap = K - 1                               # K명 '미만' 조건 → 최대 cap명 가능
dp = [0] * (cap + 1)                      # dp[c] = c명 이내로 데려갈 때 최대 사탕 수


# [5] 각 무리를 아이템처럼 넣어보기 
for w, v in groups:                       # w=무리 인원수, v=무리 사탕합
    if w > cap:                           # 무리가 cap보다 크면 못 담음
        continue
    # 0/1 배낭: 뒤에서 앞으로 역순으로 갱신 (중복 선택 방지)
    for c in range(cap, w - 1, -1):
        # 현재 dp[c]와, 이 무리를 추가했을 때(dp[c-w]+v) 중 큰 값 선택
        dp[c] = max(dp[c], dp[c - w] + v)


# [6] 정답 출력 
print(max(dp))                            # 가능한 인원수(0~cap) 중 최댓값



