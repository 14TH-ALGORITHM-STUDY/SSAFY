from collections import deque

m, n = map(int, input().split())

mirro = [list(map(int, input())) for _ in range(n)]
visit = [[m*n]*m for _ in range(n)]
visit[0][0] = 0


q = deque()
q.append((0,0,0))

can_go = [(1,0),(0,1),(-1,0),(0,-1)]

while q:
    now = q.popleft()
    if now[2] != visit[now[0]][now[1]]:
        continue

    for r, c in can_go:
        new_r = now[0]+r
        new_c = now[1]+c
        if 0<=new_r<n and 0<=new_c<m:
            if mirro[new_r][new_c]==1:
                if visit[new_r][new_c] > now[2]+1:
                    visit[new_r][new_c] = now[2]+1
                    q.append((new_r, new_c, now[2]+1))
            else:
                if visit[new_r][new_c] > now[2]:
                    visit[new_r][new_c] = now[2]
                    # q.appendleft((new_r, new_c, now[2]))
                    q.append((new_r, new_c, now[2]))

print(visit[n-1][m-1])