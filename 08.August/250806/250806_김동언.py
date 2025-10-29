com_num = int(input()) #컴퓨터 수
couple_num = int(input()) #연결되어있는 컴퓨터쌍의 수

virus = [1] # 감염된 컴퓨터들을 모은 리스트

couple_list = [] #연결되어있는 컴퓨터쌍 input을 하나의 리스트에 저장
for i in range(couple_num): 
        couple_list.append(list(map(int, input().split())))

for j in range(com_num): #컴퓨터의 수 만큼 반복
    for couple in couple_list: #서로 연결된 컴퓨터 중 하나라도 감염된 컴퓨터라면(virus리스트에 포함되어 있다면) 모두 virus에 추가
        if (couple[0] in virus) or (couple[1] in virus):
            virus.append(couple[0])
            virus.append(couple[1])

virus = list(set(virus)) #중복값 제거

virus_num = len(virus)

print(virus_num-1) #1번 컴퓨터는 제외한 수량