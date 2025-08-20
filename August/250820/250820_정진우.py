import sys
N, r, c = map(int, sys.stdin.readline().split())

cnt = 0
while N > 0:
    half = 2**(N-1)
    if r < half and c < half:          # 2사분면
        pass
    elif r < half and c >= half:       # 1사분면
        cnt += half * half
        c -= half
    elif r >= half and c < half:       # 3사분면
        cnt += 2 * half * half
        r -= half
    else:                              # 4사분면
        cnt += 3 * half * half
        r -= half
        c -= half
    N -= 1

print(cnt)
