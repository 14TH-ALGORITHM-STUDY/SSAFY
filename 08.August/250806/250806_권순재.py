computers_num = int(input()) # 컴퓨터의 수를 입력받습니다.
num_connected_pairs = int(input()) # 연결되어 있는 컴퓨터 쌍의 수를 입력받습니다.
connected_pairs = [] # 연결되어 있는 컴퓨터 쌍의 정보를 받은 리스트를 생성합니다.
infected_computers = set() # 감염된 컴퓨터 정보를 받을 set를 생성합니다.

for _ in range(num_connected_pairs): # 연결되어 있는 컴퓨터 쌍의 수만큼 반복합니다.
    A = list(map(int, input().split())) # 컴퓨터 쌍을 받고 list로 변환합니다.
    B = list(reversed(A)) # 컴퓨터 쌍의 정보를 뒤집습니다.
    connected_pairs.append(A) # 연결된 컴퓨터 쌍의 정보를 받고 저장합니다.
    connected_pairs.append(B) # 뒤집은 컴퓨터 쌍의 정보를 저장합니다.

def link(computer_1): # computer_1에 연결된 computer_2를 찾는 재귀함수를 선언합니다.
    for computer_2 in range(1, computers_num+1): # 1부터 컴퓨터의 수까지 computer_2가 순회합니다.    
        if computer_2 == computer_1: # 단, 자기 자신은 제외합니다 ex. (1,1) => 이런 연결은 없음
            continue
        
        if [computer_1, computer_2] in connected_pairs: # (computer_1, computer2)의 연결쌍이 입력받은 컴퓨터 쌍에 있는지 확인합니다.
            infected_computers.add(computer_2) # 존재한다면, computer_2를 infected_computers에 추가합니다.
            connected_pairs.remove([computer_1, computer_2]) # 지나왔던 길은 삭제합니다.
            connected_pairs.remove([computer_2, computer_1]) # 지나왔던 길은 삭제합니다.
            link(computer_2) # 이제 computer_2와 연결된 정보를 얻기 위해 재귀를 실행합니다.
    else: # for-else문으로 더 이상 자신과 연결된 컴퓨터 정보가 없을때 입니다.
        return # 재귀함수를 종료합니다. 

link(1) # 1번 컴퓨터로부터 감염이 시작되므로, 1번 컴퓨터에 대한 재귀함수를 실행합니다.
infected_computers.discard(1) # 1번 컴퓨터는 제외한 결과를 도출해야함으로, 제거합니다. remove 쓰면 오류남
print(len(infected_computers)) # 감염된 컴퓨터 수를 출력합니다.