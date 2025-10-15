def choose_target():
    target = None
    farthest_nxt = -1

    for p in plugged:
        if ptr[p] < len(schedules[p]):
            nxt_use = schedules[p][ptr[p]]
        else:
            nxt_use = float("inf")

        if nxt_use > farthest_nxt:
            farthest_nxt = nxt_use
            target = p

    return target


def optimize():
    global unplug_cnt

    for i, dev in enumerate(order):
        ptr[dev] += 1

        # 1. 이미 꽂혀 있다면 패스
        if dev in plugged:
            continue

        # 2. 빈 자리가 있으면 꽂기
        if len(plugged) < N:
            plugged.add(dev)
            continue

        # 3. 가득 찼으면 타겟 선정 후 새로운 기기로 교체
        target = choose_target()
        plugged.remove(target)
        plugged.add(dev)
        unplug_cnt += 1


N, K = map(int, input().split())
order = list(map(int, input().split()))

schedules = [[] for _ in range(K + 1)]
for idx, device in enumerate(order):
    schedules[device].append(idx)

ptr = [0] * (K + 1)

plugged = set()
unplug_cnt = 0

optimize()

print(unplug_cnt)
