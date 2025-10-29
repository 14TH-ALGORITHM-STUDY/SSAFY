# 컴퓨터 수
n = int(input())
# 연결된 쌍의 수
m = int(input())

# 그래프(인접 리스트) 초기화
graph = [[] for _ in range(n+1)]
#[[], [], [], [], [], [], [], []]


# 연결 정보 입력
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# print(graph) #[[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]
#graph = [[],
        #  [2, 5],        # 1번 컴퓨터 → 2, 5와 연결
        #  [1, 3, 5],     # 2번 컴퓨터 → 1, 3, 5와 연결
        #  [2],           # 3번 컴퓨터 → 2와 연결
        #  [7],           # 4번 컴퓨터 → 7과 연결
        #  [1, 2, 6],     # 5번 컴퓨터 → 1, 2, 6과 연결
        #  [5],           # 6번 컴퓨터 → 5와 연결
        #  [4]]           # 7번 컴퓨터 → 4와 연결

# 방문 체크 배열
visited = [False] * (n+1)
#"컴퓨터가 방문됐는지 여부"를 저장하는 리스트임. 일단 컴퓨터가 7개니까 아래처럼 나옴.
# visited = [False, False, False, False, False, False, False, False]
# 인덱스:     0      1      2      3      4      5      6      7
#visited[0]은 쓰지 않고 버림.
# 대신 visited[1]부터 visited[7]까지 컴퓨터 번호와 리스트 인덱스를 1:1로 맞춰서 사용.


# DFS 함수
def dfs(v):
    visited[v] = True
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(neighbor)
dfs(1)

# 처음에 dfs(1)
# → 1번 방문했다고 표시함
# → 연결된 친구들: 2번, 5번

# 2번은 아직 안 가봤어
# → if not visited[2]: → True니까 dfs(2)로 들어감
# → 2번 방문함 → 2번의 친구는 1번, 3번
# → 1번은 이미 갔으니까 안 감
# → 3번은 안 갔으니까 → dfs(3) 들어감

# 이런 식으로 연결된 컴퓨터들 따라가면서 전염시킴.

# 1번 컴퓨터에서 시작

# 1번 컴퓨터 제외하고 방문한 컴퓨터 수 출력
print(visited.count(True) - 1)

# visited = [False, True, True, True, False, True, True, False]
# 인덱스:     0      1      2      3      4      5      6      7
