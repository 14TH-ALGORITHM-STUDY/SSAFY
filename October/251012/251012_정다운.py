def out_plug(N, K, order_set):
    cnt = 0
    end_limit = N
    hole = order_set[:end_limit]
    for i in range(K-N):
        if order_set[end_limit:][i] in hole:
            continue
        else:
            out_number = check_out_number(hole, order_set, end_limit, i)
            hole[out_number] = order_set[end_limit:][i]
            cnt += 1
    return cnt

def check_out_number(hole, order_set, end_limit, i):
    out_lst = [0] * N

    for idx in range(N):
        if hole[idx] in order_set[end_limit+i:]:
            idx = order_set[end_limit+i:].index(hole[idx])
            out_lst[idx] = idx
        else:
            out_lst[idx] = -1

    if -1 in out_lst:
        return out_lst.index(-1)
    else:
        return out_lst.index(max(out_lst))

N, K = map(int, input().split())
order = list(map(int, input().split()))

# input으로 받은 전기용품 사용 순서인 order를 연속된 숫자가 없도록 정리한 order_set 새롭게 정의
order_set = [order[0]]
for i in range(1, len(order)):
    if order[i] != order[i-1]:
        order_set.append(order[i])
# K도 order_set의 길이로 재정의
K = len(order_set)

# 만약 멀티탭 구멍의 개수가 K보다 같거나 크다면 굳이 뽑을 필요가 없으므로 정답은 0
if N >= K:
    ans = 0
else:
    ans = out_plug(N, K, order_set)
print(ans)