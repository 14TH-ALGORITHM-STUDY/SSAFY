#n=물품의 수, k=버틸 수 있는 무게
n, k = map(int, input().split())
max_value = 0 #마지막에 출력할 가치합의 최댓값

items = {} #key:무게 value:가치 딕셔너리
weight_list = [] #무게만 모아놓은 리스트
for i in range(n):
    weight, value = map(int, input().split())
    items[weight] = value
    weight_list = list(items.keys())

for case in range(1<<n): # 1<<n : 물품의 수 n을 고려했을 때 만들수 있는 조합의 수 = 2^^n
    mid_list = [] # 무게가 n이하인지 확인하기위해 임시로 저장할 리스트
    for i in range(n): # 각 자리수별 확인하기 위해 n번 반복
        if case & (1<<i):
            mid_list.append(weight_list[i]) #가능한 조합을 만들어서 mid_list에 저장
    if sum(mid_list) <= k: # 만든 mid_list의 무게가 k이하인지 확인
        cur_value = 0
        for item in mid_list: # 무게 k 이하인 조합의 가치를 계산하고 max_value에 최댓값 저장
            cur_value += items[item]
            if max_value < cur_value:
                max_value = cur_value

print(max_value)