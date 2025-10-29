import heapq

n = int(input())
time_list = [list(map(int, input().split())) for _ in range(n)]
time_list.sort()
rooms = []
heapq.heappush(rooms, time_list[0][1])

for i in range(1, n):
    if time_list[i][0] >= rooms[0]:
        heapq.heappop(rooms)
    heapq.heappush(rooms, time_list[i][1])

print(len(rooms))