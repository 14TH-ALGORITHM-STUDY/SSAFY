T = int(input())    # Test case의 개수
N = int(input())    # 컴퓨터 쌍의 개수
chain_cases =[]     # 컴퓨터 쌍 리스트 초기화

for i in range(N):
    chain_case = list(map(int, input().split()))    # 컴퓨터 쌍
    chain_cases.append(chain_case)  # 받은 입력을 만들어둔 리스트에 추가

i = 0   # i 값 초기화
value_to_key = [1]      # 출력값에 먼저 1 넣어두기
for chain_case in chain_cases:
    if 1 in chain_case:     # 리스트 중 1이 아닌 값 추가
        if chain_case[0] != 1:
            value_to_key.append(chain_case[0])
        else:
            value_to_key.append(chain_case[1])

while i < len(value_to_key):    # value to key 리스트 전체를 확인
    value = value_to_key[i]
    for chain_case in chain_cases:
        if chain_case[0] == value:      # chain case의 key 값과 value 값이 같은데
            if chain_case[1] not in value_to_key:       #chain case의 value 값이 리스트에 없다면 추가
                value_to_key.append(chain_case[1])
        elif chain_case[1] == value:    # chain case의 value 값과 value 값이 같을때
           if chain_case[0] not in value_to_key:        #chain case의 key 값이 리스트에 없다면 추가
                value_to_key.append(chain_case[0])
    i += 1
print(len(value_to_key)-1)      # 시작할 때 넣어둔 1 값 고려