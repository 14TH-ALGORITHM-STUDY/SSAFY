# 문제 요약
# 일부만 연결된 부분 연결 그래프가 주어진다.
# 각 노드의 컴퓨터의 연결 정보는 쌍(pair) 형태의 리스트
# 1번 컴퓨터와 직간접적으로 연결된 모든 컴퓨터 수 구하기

# 컴퓨터 수, 쌍의 수
cpu_cnt = int(input())
pair_cnt = int(input())

# 그냥 2차원 배열
arr = [list(map(int, input().split())) for _ in range(pair_cnt)]

# 카운트한 노드(1은 문제상 제외, 0은 아래 식의 조건때문에)
visited = [0, 1]

# 결과값으로 나올 카운트
cnt = 0

# 무한 루프
while True:
    # 더이상 변화가 없으면 종료
    changed = False
    # 이미 방문한 목록에 있고 중복이 아니라면 배열에 추가
    for pair in arr:
        if pair[0] in visited and pair[1] not in visited:
            visited.append(pair[1])
            cnt += 1
            changed = True
        elif pair[1] in visited and pair[0] not in visited:
            visited.append(pair[0])
            cnt += 1
            changed = True
    # 변화없으면 루프 탈출        
    if not changed:
        break

print(cnt)
