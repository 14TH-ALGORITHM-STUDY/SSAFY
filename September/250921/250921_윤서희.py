# 주어진 도시를 두 개의 분리된 마을로 나누는 데 필요한 최소 비용을 구하는 문제
# N:집의 개수, M: 길의 개수
# 각 길은 유지비가 있으며, 모든 집은 결국 두 마을 중 하나에 속해야 함
#  - 각 마을 안에 있는 집들은 서로 연결되어 있어야 함.
#  - 두 마을 사이의 길은 없어야 함.


import sys
sys.setrecursionlimit(10**6)

def find_root(parent_list, house):
    #어떤 집이 속한 마을의 대표(대장) 집을 찾는다
    if parent_list[house] != house:
        parent_list[house] = find_root(parent_list, parent_list[house])
    return parent_list[house]

def unite_villages(parent_list, house1, house2):
    #두 집이 속한 마을을 하나로 합친다
    root1 = find_root(parent_list, house1)
    root2 = find_root(parent_list, house2)
    if root1 < root2:
        parent_list[root2] = root1
    else:
        parent_list[root1] = root2

def main():
    # 집의 개수(N)와 길의 개수(M)를 입력받는다
    num_houses, num_roads = map(int, sys.stdin.readline().split())

    # 길 정보를 '유지비', '집1', '집2' 순서로 리스트에 저장한다
    roads = []
    for _ in range(num_roads):
        house1, house2, cost = map(int, sys.stdin.readline().split())
        roads.append((cost, house1, house2))

    roads.sort()  # 유지비가 저렴한 길부터 사용하기 위해 정렬한다

    parent_list = [i for i in range(num_houses + 1)] # 각 집을 각자 하나의 마을로 초기화한다

    total_cost = 0  # 모든 집을 연결하는 데 드는 총 유지비
    max_road_cost = 0 # 가장 비싼 길의 유지비

    # 유지비가 저렴한 길부터 하나씩 연결해본다
    for cost, house1, house2 in roads:
        # 두 집이 아직 다른 마을에 속해 있다면, 길을 연결한다
        if find_root(parent_list, house1) != find_root(parent_list, house2):
            unite_villages(parent_list, house1, house2)
            total_cost += cost
            # 연결한 길 중 가장 비싼 길의 유지비를 기록한다
            max_road_cost = cost 

    #총 유지비에서 가장 비싼 길의 유지비를 빼서 출력한다
    print(total_cost - max_road_cost)

if __name__ == "__main__":
    main()

    #다음에 다시 한 번 풀어보도록 하겠습니다