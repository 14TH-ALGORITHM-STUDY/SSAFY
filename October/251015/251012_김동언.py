from collections import deque

# n: 멀티탭 구멍의 개수, k: 전기용품의 사용 횟수
n, k = map(int, input().split())

# 전기용품의 사용순서를 넣을 리스트(덱)
elec = deque()
elec_data = list(map(int, input().split()))

for i in elec_data:
    elec.append(i)

# 현재 사용 중인 전기용품이 들어있는 리스트
soket = []

# 플러그를 빼는 횟수(최종 출력할 값)
cnt = 0

# 전기용품이 모두 소모될 때까지 진행
while elec:
    # 덱을 이용해서 왼쪽부터 빼낸다.
    use = elec.popleft()
    # 이미 소켓에서 사용 중이라면 교체할 필요가 없으니 PASS
    if use in soket:
        continue
    # 소켓에 꽂혀있지 않지만 소켓에 빈자리가 있다면 바로 꽂기
    elif len(soket) < n:
        soket.append(use)
    # 소켓에 꽂혀있지 않고 소켓에 빈자리도 없다면 하나를 빼고 꽂는다
    # 효율성을 위해 뒤에 남은 전기용품 순서 중 가장 나중에 사용하거나, 아예 사용계획이 없는 친구를 뺀다.
    else:
        # 초기화
        long_range = -1
        remove_num = -1
        for using in soket:
            try:
                # 남은 순서를 탐색하여 현재 사용 중인 전기용품이 몇차례 뒤에 다시 사용한는지 확인
                # 사용 중인 전기용품 중 가장 나중에 다시 사용예정인 전기용품를 찾는다.
                if elec.index(using) > long_range:
                    long_range = elec.index(using)
                    remove_num = using
            # index(using) 실행했는데 남은 순서 리스트에 해당 전기용품이 없다면 오류 발생
            # 그 친구를 바로 뺀다.
            except:
                remove_num = using
                break
        # soket(사용중인 전기용품 리스트)에 전기용품을 제거하고 새로운 전기용품을 추가한다.
        soket.remove(remove_num)
        soket.append(use)
        
        # 플러그 교환 횟수 추가
        cnt += 1
        
print(cnt)