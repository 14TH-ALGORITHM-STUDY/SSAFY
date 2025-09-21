# 정점 N개, 간선 M개, 가중치 C
# 마을을 2개로 분리, 각 분리된 마을 안에 집들이 서로 연결되도록 분할
# 각 분리된 마을 안에 임의의 두 집 사이엔 경로가 존재해야함
# 마을에 1개이상의 집 있어야함

def find_set(x): # 대표자 찾기
    if x == parents[x]:
        return x
    
    parents[x] = find_set(parents[x]) #편향트리가 되는 경우 
    return parents[x]                 #1개씩 다 타고 올라가기 때문에 바로 대표원소로 바꾸기
                                      #경로 압축


def union(x, y):
    r_x = find_set(x)
    r_y = find_set(y)

    if r_x == r_y: #이미 같은 집합이면
        return
    if ranks[r_x] < ranks[r_y]: #x의 레벨이 더 낮으면
        parents[r_x] = r_y # x를 y에 붙이고
    elif ranks[r_x] > ranks[r_y]: # 그 반대의 경우
        parents[r_y] = r_x # y를 x에 붙임
    else: #레벨이 똑같은 경우
        parents[r_y] = r_x #한쪽으로 병합하기 (parents[r_x] = r_y 상관없음) 
        ranks[r_x] += 1 # 레벨 1 올리기

N, M = map(int, input().split())
town =[]

for i in range(M):
    A, B, C = map(int, input().split())
    town.append((A, B, C))

town.sort(key=lambda x: x[2]) #가중치 기준으로 정렬

cnt = 0 #선택한 간선 수
result = 0 #가중치 합

parents = [i for i in range(N+1)]
ranks = [0] * (N+1)
max_c = 0 # 가장 큰 가중치
for x, y, z in town:
    if find_set(x) != find_set(y):
        union(x, y)
        cnt += 1
        result += z
        max_c = max(max_c, z)
        if cnt == N-1:
            break
print(result- max_c)
# 가장큰 가중치를 빼기 전엔 하나의 트리구조임
# 마을을 2개로 나누고, 유지비를 최소로 하려면
# 가장 큰 간선 1개를 없애면 트리가 2개로 나눠지고
# 가장 최소 유지비가 됨
