# -*- coding: utf-8 -*-
"""
 * 문제: 백준 14502 연구소
 *
 * ## 문제 설명
 * N x M 크기의 연구소 맵이 주어집니다. 맵에는 빈 칸(0), 벽(1), 바이러스(2)가 있습니다.
 * 이 맵의 빈 칸 중에서 3개를 골라 새로운 벽을 세울 수 있습니다.
 * 그 후, 바이러스는 상하좌우 인접한 빈 칸으로 퍼져나갑니다.
 * 벽을 3개 세운 뒤, 바이러스가 퍼지지 않은 안전 영역(0)의 크기가 최대가 되는 경우를 찾아 그 크기를 출력하는 문제입니다.
 *
 * ## 풀이 접근
 * 이 문제는 가능한 모든 경우를 탐색해야 하는 '브루트 포스(Brute Force)' 문제입니다.
 * 벽을 세울 수 있는 모든 조합을 시도하고, 각 조합마다 결과를 확인하여 최댓값을 찾아야 합니다.
 *
 * 1.  **탐색 대상 목록화**:
 * - 먼저, 벽을 세울 수 있는 모든 빈 칸(0)의 좌표를 리스트에 전부 저장합니다.
 * - 이렇게 하면 전체 맵(N*M)을 매번 탐색할 필요 없이, 벽을 세울 수 있는 후보들만 모아놓고 효율적으로 조합을 찾을 수 있습니다.
 *
 * 2.  **벽 세우기 (조합, DFS/백트래킹)**:
 * - 위에서 만든 '빈 칸 목록'에서 3개의 칸을 선택하는 모든 조합을 찾아야 합니다.
 * - 재귀 함수(DFS 방식)를 사용하여 구현합니다. `pickwall` 함수가 이 역할을 합니다.
 * - 중복된 조합을 피하기 위해, 다음 벽은 항상 현재 선택한 벽보다 리스트의 더 뒷 순번에서만 선택하도록 합니다.
 *
 * 3.  **바이러스 퍼뜨리기 (시뮬레이션, BFS)**:
 * - 벽 3개가 세워진 각각의 맵 상태에 대해 바이러스가 어떻게 퍼지는지 시뮬레이션합니다.
 * - 너비 우선 탐색(BFS) 알고리즘으로 구현하는 것이 가장 적합합니다. `simulation` 함수가 이 역할을 합니다.
 *
 * 4.  **안전 영역 계산 및 최댓값 갱신**:
 * - 바이러스 시뮬레이션이 끝난 후, 맵에 남아있는 빈 칸(0)의 개수를 셉니다.
 * - 이 개수가 이전에 구한 최댓값보다 크면, 최댓값을 갱신합니다.
"""

import sys
from collections import deque
import copy # 시뮬레이션을 위한 맵 복사에 사용

# 전역 변수 선언
# n, m: 맵의 세로, 가로 크기
n, m = 0, 0

# map: 원본 맵을 저장하는 2차원 리스트
# (Python의 내장 함수 map과의 충돌을 피하기 위해 graph라는 이름을 사용하는 것이 일반적이지만,
# C++ 코드와의 통일성을 위해 여기서는 map_data로 명명)
map_data = []

# empty_spaces: 벽을 세울 수 있는 빈 칸(0)의 좌표 목록
empty_spaces = []

# max_safearea: 모든 조합 중 가장 컸던 안전 영역의 크기 (최종 정답)
max_safearea = 0

# 4방향 탐색을 위한 y, x 좌표 변화량 (상, 하, 좌, 우)
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 바이러스 확산 시뮬레이션 및 안전 영역 계산 함수 (BFS 사용)
def simulation():
    global max_safearea # 전역 변수 max_safearea를 수정하기 위해 선언

    # 1. 시뮬레이션을 위해 원본 맵(map_data)을 깊은 복사(deepcopy)하여 임시 맵을 만듦
    simulmap = copy.deepcopy(map_data)
    q = deque() # BFS를 위한 덱(deque) 생성

    # 2. 시뮬레이션 맵(simulmap)에서 모든 바이러스의 초기 위치를 큐에 넣는다.
    for i in range(n):
        for j in range(m):
            if simulmap[i][j] == 2:
                q.append((i, j))

    # 3. BFS를 통해 바이러스 확산 진행
    while q:
        y, x = q.popleft()

        # 현재 위치에서 상하좌우 4방향을 탐색
        for i in range(4):
            next_y, next_x = y + dy[i], x + dx[i]

            # 맵 범위를 벗어나지 않고, 다음 위치가 빈 칸(0)인 경우
            if 0 <= next_y < n and 0 <= next_x < m and simulmap[next_y][next_x] == 0:
                # 바이러스로 감염시키고, 큐에 추가하여 다음 탐색 대상으로 삼는다.
                simulmap[next_y][next_x] = 2
                q.append((next_y, next_x))

    # 4. 안전 영역(0의 개수) 계산
    safearea = 0
    for i in range(n):
        for j in range(m):
            if simulmap[i][j] == 0:
                safearea += 1
    
    # 5. 최대 안전 영역 크기 갱신
    max_safearea = max(max_safearea, safearea)

# 벽 3개를 세우는 모든 조합을 찾는 재귀 함수 (DFS/백트래킹 사용)
# lev: 현재까지 세운 벽의 개수
# start_idx: 탐색을 시작할 'empty_spaces' 리스트의 인덱스
def pickwall(lev, start_idx):
    # Base Case: 벽 3개를 모두 세웠을 경우
    if lev == 3:
        # 현재 맵 상태에서 바이러스 시뮬레이션을 실행
        simulation()
        # 현재 조합에 대한 탐색을 마치고 돌아간다.
        return

    # Recursive Step: 다음 벽을 세울 위치를 찾는다.
    # 'empty_spaces' 리스트를 순회하며 벽을 세울 위치를 고른다.
    # start_idx + 1 부터 시작하는 이유: 중복된 조합을 피하기 위함
    for i in range(start_idx + 1, len(empty_spaces)):
        # 리스트에서 i번째 후보지의 좌표를 가져온다.
        y, x = empty_spaces[i]

        # --- 백트래킹 과정 ---
        # 1. 선택: 해당 위치에 벽을 세운다.
        map_data[y][x] = 1
        # 2. 탐색: 다음 벽을 세우기 위해 재귀 호출 (세운 벽 개수+1, 현재 리스트 인덱스 전달)
        pickwall(lev + 1, i)
        # 3. 복구: 재귀 호출이 끝나면, 세웠던 벽을 다시 빈 칸으로 되돌려 놓는다.
        map_data[y][x] = 0

# 메인 실행 부분
if __name__ == "__main__":
    # 입출력 속도 향상
    input = sys.stdin.readline

    # 맵의 크기(n, m) 입력
    n, m = map(int, input().split())

    # 초기 맵 상태 입력 및 빈 칸 목록 생성
    for i in range(n):
        row = list(map(int, input().split()))
        map_data.append(row)
        for j in range(m):
            # 만약 입력받은 칸이 빈 칸(0)이라면, 벽을 세울 수 있는 후보 목록에 추가
            if map_data[i][j] == 0:
                empty_spaces.append((i, j))
    
    # 벽을 0개 세운 상태, -1번 인덱스부터 탐색 시작 (실제로는 0번부터 시작됨)
    pickwall(0, -1)

    # 최종적으로 계산된 최대 안전 영역 크기 출력
    print(max_safearea)