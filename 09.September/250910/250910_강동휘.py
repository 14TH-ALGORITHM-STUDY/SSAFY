N = int(input())
lst = [tuple(map(int, input().split())) for _ in range(N)]

starts = sorted(s for s, e in lst)
ends   = sorted(e for s, e in lst)

i = j = 0
cur = ans = 0

while i < N:
    if starts[i] < ends[j]:
        cur += 1          # 새 강의 시작 → 방 하나 더 필요
        ans = max(ans, cur)
        i += 1
    else:
        cur -= 1          # 어떤 강의가 끝남 → 방 하나 비움
        j += 1

print(ans)
