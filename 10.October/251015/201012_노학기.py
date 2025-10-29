N, K = map(int, input().split())
schedule = list(map(int, input().split()))

# print(N, K)
# print(schedule)

unplug_count = 0
multitap = set()
for i in range(K):
    product = schedule[i]

    if product in multitap: # 멀티탭에 제품이 있으면 넘어감
        continue

    if len(multitap ) < N: # 멀티탭에 빈 곳 있으면
        multitap.add(product) # 제품 사용
        continue

    unplug_count += 1 # 멀티탭이 다 찼으므로 뽑아야함

    unplug_candi = -1 # 멀티탭에서 뺼 제품 후보
    idx = -1 # 스케줄에서 가장 나중에 있는 자리
    left_schedule = schedule[i+1:] # 앞으로 남은 스케줄
    for plugged in multitap:
        cur_pos = 0
        if plugged in left_schedule: # 남은 계획에 제품이 있으면
            cur_pos = left_schedule.index(plugged) # 제품이 언제 쓰이는지
        else:
            cur_pos = K + 1 # 남은 계획에 없다면 우선적으로 뽑아야함으로 최대값으로 설정하여 무조건 뽑게함

        # 지금까지 찾은 가장 나중에 쓰이는 후보보다 더 뒤에 쓰인다면 후보 교체
        if cur_pos > idx:
            idx = cur_pos
            unplug_candi = plugged

    # 제품 후보를 제거 및 현재 제품 추가
    multitap.remove(unplug_candi)
    multitap.add(product)

print(unplug_count)
