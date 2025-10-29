'''
10 6 6
9 15 4 4 1 5 19 14 20 5
1 3
2 5
4 9
6 2
7 8
6 10

- 친구 관계는 양방향
    - 1 3 으로 주어졌으면 3 1도 성립 -> 친구 관계를 그룹화   
'''

N, M, K = map(int, input().split())
candy = list(map(int, input().split()))

friends = {i: [] for i in range(N)} # N명의 아이들에 대해 빈 리스트 초기화
for _ in range(M):
    a, b = map(int, input().split())
    # index로 활용하기 위해 1씩 빼서 넣어 줌
    a -= 1
    b -= 1
    friends[a].append(b)
    friends[b].append(a)
# {0: [2], 1: [4, 5], 2: [0], 3: [8], 4: [1], 5: [1, 9], 6: [7], 7: [6], 8: [3], 9: [5]}


# 그룹화
visited = [False] * N
groups = [] # [(그룹 인원, 그룹 총 사탕)]

for i in range(N):
    if not visited[i]:
        group_size = 0
        group_candy = 0
        
        q = [i]
        visited[i] = True
        
        while q:
            current_child = q.pop(0)
            group_size += 1
            group_candy += candy[current_child]
            
            for friend in friends[current_child]:
                if not visited[friend]:
                    visited[friend] = True
                    q.append(friend)
        
        groups.append((group_size, group_candy))
# [(2, 13), (4, 26), (2, 24), (2, 33)]

dp = [0] * K

for size, value in groups:
    for j in range(K-1, size -1, -1):
        dp[j] = max(dp[j], dp[j-size]+value)

'''
*** kanpsack 알고리즘 ***
url : https://howudong.tistory.com/106#google_vignette

dp[j] : j 명의 아이들을 선택했을 때, 얻을 수 있는 최대 사탕의 수
K-1 부터 시작하는 이유 : 우리의 목표 인원수가 K-1 명이기 때문 
size-1 에서 끝나는 이유 : 아이들 그룹의 총 인원수(size)가 만들고자 하는 목표 인원수(j) 보다 클 수 없기 때문
여러 그룹 size들이 더해져서 목표 인원수 j를 채워야 되는데 size가 j를 넘어버리면
시작과 동시에 아이들 울음소리가 하늘을 찌를 것..
역순으로 순회하는 이유 : 그래야 그룹 당 한 번씩만 뺏을 수 있어서
j가 정방향으로 순회하게 되면, dp[2], dp[3]이 먼저 계산되는데 이후에 dp[4],dp[5]에서 dp[2], dp[3]을 참조해서 사용할 때
현재 그룹으로 update된 값을 참조하게 되며 이는 한 그룹을 2번 사용하게 되는 꼴 (하기 DP 과정 설명 참조)

dp[j] = max(dp[j], dp[j-size]+value) : 직전 사이즈 까지 최적화된 dp값에 현재 value값을 더한 값과 현재 저장된 dp[j] 값을 비교
'''
# dp = [0, 0, 33, 33, 57, 57]
print(dp[K-1])

'''
[DP 과정]

group 1) size = 2, value = 13
range(5, 1, -1) : 5, 4, 3, 2

(1) j = 5 -> dp[5] = max(dp[5], dp[3] + 13) = max(0, 0+13) = 13
(2) j = 4 -> dp[4] = max(dp[4], dp[2] + 13) = max(0, 0+13) = 13
(3) j = 3 -> dp[3] = max(dp[3], dp[1] + 13) = max(0, 0+13) = 13
(4) j = 2 -> dp[2] = max(dp[2], dp[0] + 13) = max(0, 0+13) = 13

dp = [0, 0, 13, 13, 13, 13]

---

group 2) size = 4, value = 26
range(5, 3, -1) : 5, 4

(1) j = 5 -> dp[5] = max(dp[5], dp[1] + 26) = max(13, 0+26) = 26 # 5명을 채울 때, 기존의 최적 13개와 4명 그룹(26)에 dp[1](0)을 더한 경우 중 더 나은 것 선택
(2) j = 4 -> dp[4] = max(dp[4], dp[0] + 26) = max(13, 0+26) = 26

dp = [0, 0, 13, 13, 26, 26]

---

group 3) size = 2, value = 24
range(5, 1, -1) : 5, 4, 3, 2

(1) j = 5 -> dp[5] = max(dp[5], dp[3] + 24) = max(26, 13+24) = 37 # 5명을 채울 때, 현재 max인 4명 그룹으로만 채우는 경우(26)와 '현재 3명 max 조합(그룹 1로만 채우는 경우, 13) + 현재 그룹(24)'으로 채우는 경우 중 더 나은 것 선택
(2) j = 4 -> dp[4] = max(dp[4], dp[2] + 24) = max(26, 13+24) = 37
(3) j = 3 -> dp[3] = max(dp[3], dp[1] + 24) = max(13, 0+24) = 24
(4) j = 2 -> dp[2] = max(dp[2], dp[0] + 24) = max(13, 0+24) = 24

dp = [0, 0, 24, 24, 37, 37]

---

group 4) size = 2, value = 33
range(5, 1, -1) : 5, 4, 3, 2

(1) j = 5 -> dp[5] = max(dp[5], dp[3] + 33) = max(37, 24+33) = 57 # 5명을 채울 때, 현재 max인 '그룹 1 + 그룹 3'(37)과 현재 3명 max 조합인 '그룹 3'(24)에 현재 그룹(33)을 더한 경우 중 더 나은 것 선택
(2) j = 4 -> dp[4] = max(dp[4], dp[2] + 33) = max(37, 24+33) = 57
(3) j = 3 -> dp[3] = max(dp[3], dp[1] + 33) = max(24, 0+33) = 33
(4) j = 2 -> dp[2] = max(dp[2], dp[0] + 33) = max(24, 0+33) = 33

dp = [0, 0, 33, 33, 57, 57]
'''