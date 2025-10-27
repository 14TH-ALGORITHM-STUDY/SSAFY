# N개의 수 중 어떤 수가 다른 수 두 개 합으로 나타낼 수 있는 개수
# 수의 위치가 다르면 값이 같아도 다름

# 1. 정렬
# 2. 투 포인터 방식 ( 이 문제를 풀면서 깨달았음 어렵농)
# 3. l과 r이 i인 경우를 생각해서 조건에 넣어줘야했음. (크랙이네)
#  솔직히 GPT봤음. 안봤으면 절대 못풀었을 듯. 투포인터라는 것을 몰랐음


N = int(input())
a = list(map(int, input().split()))
arr = sorted(a)
cnt = 0

for i in range(N):
    target = arr[i]
    l, r = 0, N-1
    
    while l < r:
        s = arr[l] + arr[r]

        if s == target: # 수가 좋다!(GOOD)고
            if l != i and r != i: # 본인미포함이면
                cnt += 1 #개수 카운트하기
                break

            if l == i:      #이조건을
                l += 1      #안넣었다고
            elif r == i:    #시간초과
                r -= 1      #나옴. 타겟과 같은경우 l, r이 멈춤 무한루프된다 함


        elif s < target: #목표값보다 작은 경우
            l += 1       #정렬된 리스트여서 l의 인덱스를 올리면 값이 커짐
        elif s > target: #목표값보다 큰 경우
            r -= 1       #정렬된 리스트여서 r의 인덱스를 줄이면 값이 작아짐


print(cnt)