participants = [list(map(int, input().split())) for _ in range(5)]

max_score = 0

score = 0

winner = 0

for i in range(5):
    #매 참여자 점수 초기화
    score = 0
    for j in range(len(participants[i])):
        #점수 합산
        score += participants[i][j]
    #최대 점수 여부 확인
    if max_score <= score:
        max_score = score
        winner = i

#참여자 번호는 1번부터 시작이기 때문에 index에 1더하기
print(winner+1, max_score)