N = int(input())

par_per_room = list(map(int, input().split()))

#B: 총감독관 감시 가능 수, C: 부감독관 감시 수
B, C = list(map(int, input().split()))

#총 감독관이 커버 가능한 인원수
cover = 0

#감독관 수
seer = 0

for participants in par_per_room:
    #우선 주감독관 숫자 만큼 빼주기
    participants -= B
    seer += 1

    if participants > 0:
        seer = seer + (participants // C)
        if participants % C > 0:
            seer += 1

print(seer)