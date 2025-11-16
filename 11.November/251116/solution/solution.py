import sys
from collections import deque

input = sys.stdin.readline		# 속도 향상

n = 0
cap = [[0] * 52 for _ in range(52)]
flow = [[0] * 52 for _ in range(52)]		# 현재 물의 흐름
# visited 배열은 findway 함수 내에서 매번 새로 생성됩니다.
total_flow = 0


def findway(from_node, to_node):		# BFS
	visited = [-1] * 52		# 방문여부 & 도착 지점 (경로 추적 가능) # -1으로 초기화

	q = deque()
	q.append(from_node)
	visited[from_node] = from_node	# 시작점이므로

	while q:
		now = q.popleft()

		for i in range(52):
			if cap[now][i] - flow[now][i] > 0 and visited[i] == -1:
				q.append(i)
				visited[i] = now
				if i == to_node:	# 도착점이라면 종료
					break
			
		if visited[to_node] != -1:	# 도착점이라면 while도 종료
			break
	
	if visited[to_node] == -1:	# 'Z'에 도달하지 못했다면
		return 0

	# 'Z'에 도달했다면 : 유량 확인
	path = float('inf') # C++의 21e8 (int 최대값) 대신 무한대(inf) 사용
	v = to_node
	while v != from_node:
		w = visited[v]
		path = min(path, cap[w][v] - flow[w][v])
		v = visited[v]
	
	v = to_node
	while v != from_node:
		w = visited[v]
		
		flow[w][v] += path	# 정방향
		flow[v][w] -= path	# 역방향

		v = visited[v]

	return path

# --- main ---

n = int(input())

for _ in range(n):
	fr, to, fl = input().split()
	fl = int(fl)
	
	u, v = 0, 0
	if 'A' <= fr <= 'Z': u = ord(fr) - ord('A')		# A-Z -> 0-25
	else: u = ord(fr) - ord('a') + 26				# a-z -> 26-51

	if 'A' <= to <= 'Z': v = ord(to) - ord('A')		# A-Z -> 0-25
	else: v = ord(to) - ord('a') + 26				# a-z -> 26-51

	cap[u][v] += fl	# 여러개 파이프가 있을 수 있으므로
	cap[v][u] += fl

start_node = 0 # 'A'
end_node = ord('Z') - ord('A') # 25

while True:
	path = findway(start_node, end_node)
	
	if path == 0:
		break
	
	total_flow += path
	
print(total_flow)
