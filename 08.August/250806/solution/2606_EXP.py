'''
INPUT
7
6
1 2
2 3
1 5
5 2
5 6
4 7
'''

C = int(input()) # 컴퓨터의 수를 입력 받음 C = 7

L = int(input()) # 컴퓨터 쌍의 수 L = 6

g = [[] for i in range(C + 1)] # g 이중 리스트 컴퓨터 개수 + 1 생성
# [[0], [1], [2], [3], [4], [5], 6[], 7[]]

vstd = [False] * (C + 1) # [False, False, False... 컴퓨터의 수 + 1 만큼]
# [False, False, False, False, False, False, False, False]

for i in range(L): # 컴퓨터 쌍의 수(L=6)만큼 반복
    a, b = map(int, input().split()) # 컴퓨터 쌍의 정보 입력 받음
    g[a].append(b) # g의 a번째에 b를 추가
    g[b].append(a) # g의 b번째에 a를 추가

'''
i = 0)
index    0   1   2   3   4   5   6   7  
        [[], [], [], [], [], [], [], []]

index    0    1    2   3   4   5   6   7  
        [[], [2], [1], [], [], [], [], []]
----------------------------------------------
i = 1)
index    0    1    2   3   4   5   6   7  
        [[], [2], [1], [], [], [], [], []]
        
index    0    1      2     3   4   5   6   7  
        [[], [2], [1, 3], [2], [], [], [], []]
-------------------------------------------------
최종 결과
g = [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]
--------------------------------------------------
'''

def dfs(v): # 재귀 함수 선언
    vstd[v] = True # 만약 v가 1이라면?
    # vstd = [False, False, False, False, False, False, False, False]
    # vstd = [False, True, False, False, False, False, False, False]
    # 즉, 1번 컴퓨터를 방문했어요! 라는 의미, vstd = visited의 약자!
    
    for i in g[v]:
    # g = [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]
    # g[1] = [2, 5]
    # 즉, 1번 컴퓨터는 2번과 5번과 연결되어있다!
    
        if not vstd[i]:
            dfs(i)
'''
--------------------------------------------------------------
dfs(1) 경우
vstd = [False, True, False, False, False, False, False, False]
for i in [2, 5]
i = 2)
if not vstd[2] => 너 2번 컴퓨터 방문 안했어? => 응 안했어
    dfs(2) => 2번도 가서 확인해!
---------------------------------------------------------------
dfs(2) 경우
vstd = [False, True, True, False, False, False, False, False]
for i in [1, 3, 5]
i = 1)
vstd = [False, True, True, False, False, False, False, False]
if not vstd[1] => 너 1번 컴퓨터 방문안했어? => 했는데?

i = 3)
vstd = [False, True, True, False, False, False, False, False]
if not vstd[3] => 너 3번 컴퓨터 방문안했어? => 응 안했어
    dfs(3) => 3번도 가서 확인해!
----------------------------------------------------------------
dfs(3) 경우
vstd = [False, True, True, True, False, False, False, False]
for i in [2]

i = 2)
vstd = [False, True, True, True, False, False, False, False]
if not vstd[2] => 너 2번 컴퓨터 방문안했어? => 했는데?
------------------------------------------------------------------
i = 5)
vstd = [False, True, True, True, False, False, False, False]
if not vstd[5] => 너 5번 컴퓨터 방문안했어? => 응 안했는데?
    dfs(5) => 5번 가서 확인해!

검사할 컴퓨터가 없을때까지 무한 반복
최종적으론 1번으로부터 감염된 정보들이 vstd 배열에 저장된다!
'''

dfs(1) # 1번부터 감염 검사 시작해
print(sum(vstd) - 1) # 1번은 제외 최종 결과 도출!, True는 1로 False는 0으로 간주됨

















