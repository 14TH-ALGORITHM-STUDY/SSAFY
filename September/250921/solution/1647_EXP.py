'''
-문제 요약
N개의 집과 M개의 도로 정보(양 끝 집, 비용)가 주어진다. 
각 마을에는 집이 하나 이상 있어야 된다고 했으므로 
모든 집들을 연결하는 최소 비용의 도로 네트워크(최소 스패닝 트리, MST)를 만들되, 
마을을 두 개로 분할하기 위해 가장 비용이 큰 도로 1개를 제거했을 때의 최소 유지비를 구하는 문제.

-문제 조건 분석
시간 제한 : 2초 (일반적으로 Python으로는 약 1억 번의 연산이 가능하다.)
입력 크기 : 
    - 집(정점) 수 : N (2 <= N <= 100,000)
    - 도로(간선) 수 : M (1 <= M <= 1,000,000)

간선 수 최대 백만 개 -> O(M log M) 정도의 알고리즘 필요
O(N^2) 불가능 (10^10 수준 -> 시간 초과)

-풀이방법
사용 알고리즘 : 크루스칼 MST (Union-Find)
아이디어:
    1. 모든 도로를 유지비 기준으로 정렬
    2. Union-Find로 MST를 구성하면서 간선 추가
    3. MST가 완성되면, 포함된 간선들 중 가장 큰 비용의 간선 제거
    4. 전체 MST 비용 - (가장 큰 간선 비용) = 정답 
'''

import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline  # 입력시간 때문에 시간초과가 발생하므로 `input()` 대신 `readline()`을 사용

def find_parents(x):
    if x == parents[x]: # 노드 x의 부모 노드가 자기 자신이라면
        return x        # 자기 자신을 반환

    # 노드 x의 부모노드의 자기자신이 아니면 
    # 노드 x의 부모노드 = 최상위 부모노드 탐색 재귀
    parents[x] = find_parents(parents[x])
    return parents[x]   # 현재 노드 x의 최상위 부모 노드 return 

def union(x, y):
    rx = find_parents(x)    # 노드 x의 최상위 노드 탐색
    ry = find_parents(y)    # 노드 y의 최상위 노드 탐색

    if rx == ry:            # 노드 x와 노드 y의 최상위 노드가 같다면 함수 종료
        return

    # 노드 x와 노드 y의 최상위 노드가 다르다면 
    if rx < ry:             # 노드 y의 최상위 노드가 노드 x의 최상위 노드보다 크다면
        parents[ry] = rx    # 노드 y의 최상위 노드를 노드 x의 최상위 노드로 갱신 
    else:                   # 노드 x의 최상위 노드가 노드 y의 최상위 노드보다 크다면
        parents[rx] = ry    # 노드 x의 최상위 노드를 노드 y의 최상위 노드로 갱신 

'''
input 예시

7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4
'''
N, M = map(int, input().split())
edges = []
for _ in range(M):
    n1, n2, w = map(int, input().split())
    edges.append((n1, n2, w))

# input으로 받은 (집1, 집2, 유지비)를 유지비 기준으로 정렬
edges.sort(key=lambda x : x[2])
'''
[(3, 2, 1), 
(6, 4, 1), 
(1, 3, 2), 
(2, 5, 2), 
(1, 6, 2), 
(1, 2, 3), 
(6, 5, 3), 
(4, 5, 3), 
(3, 4, 4), 
(6, 7, 4), 
(5, 1, 5), 
(7, 3, 6)]
'''

# 각 노드의 최상위 노드값을 노드 자기자신으로 초기 설정
parents = [i for i in range(N+1)]
cnt = 0         # union-find 횟수 0으로 초기 설정
min_w_sum = 0   # 길 유지비의 합의 최솟값
large_w = 0     # 현재까지의 가장 큰 유지비

for u, v, w in edges:
    if find_parents(u) != find_parents(v):  # u와 v의 최상위 노드의 값이 다르다면
        union(u, v)                         # u와 v를 union
        cnt += 1                            # union 횟수 + 1
        min_w_sum += w                      # 길 유지비 합에 + w
        large_w = w                         # 현재 유지비를 현재까지 가장 큰 유지비로 갱신

    if cnt == N:
        break

print(min_w_sum - large_w)  
# 길 유지비 최소합에 현재 가장 큰 유지비(간선)를 제거하여
# N-1개 집으로 구성된 마을과 1개의 집으로 구성된 마을로 분할 
