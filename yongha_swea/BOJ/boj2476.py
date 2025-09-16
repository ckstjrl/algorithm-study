#주사위를 3개 던진다 (1~6 눈 값)
# 같은 눈 3개: 10000 + 눈 * 1000
# 같은 눈 2개: 1000 + 눈 * 100
# 다른 눈: 가장 큰 눈 * 100

N = int(input())

party = [list(map(int, input().split())) for _ in range(N)]

score = 0

max_score = 0

for i in range(len(party)):
    #party[i][0]: 주사위 1, party[i][1]: 주사위2, party[i][2]: 주사위3
    die_1 = party[i][0]
    die_2 = party[i][1]
    die_3 = party[i][2]

    #매 사람마다 초기화
    score = 0
    
    #모두 같은 눈인 경우 점수 계산
    if die_1 == die_2 == die_3:
        score = 10000 + (die_1 * 1000)
    
    #두개가 같은 눈인 경우 점수 계산
    elif die_1 == die_2 or die_1 == die_3:
        score = 1000 + (die_1 * 100)
    elif die_2 == die_3:
        score = 1000 + (die_2 * 100)
    
    #모두 다른 값인 경우 점수 계산
    else:
        if die_1 > die_2 and die_1 > die_3:
            score = die_1 * 100
        elif die_2 > die_1 and die_2 > die_3:
            score = die_2 * 100
        else:
            score = die_3 * 100

    if score >= max_score:
        max_score = score

print(max_score)