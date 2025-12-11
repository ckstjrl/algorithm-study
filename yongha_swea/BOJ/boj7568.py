# BOJ7568 덩치

size =[]

ranking = []

people = int(input())

# 무게와 키 양쪽이 모두 더 큰 경우에만 상위 랭크, 하나라도 작으면 동률, 둘 다 작으면 더 낮은 랭크
for i in range(people):
    w, h = map(int, input().split())
    size.append((w, h))

for i in range(people):
    # 랭크는 0이 아니라 1부터 시작하기 때문에 1로 시작
    rank = 1

    # 다른 사람과 비교하여 무게와 키 양쪽이 다 작은 경우에 랭크 하나 추가 
    for j in range(people):
        if size[i][0] < size[j][0] and size[i][1] < size[j][1]:
            rank += 1

    #등수를 받는 랭킹 리스트에 랭크 리스트 추가
    ranking.append(rank)

print(*ranking)
    
