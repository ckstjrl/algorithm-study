#boj2822 점수 계산

#8개의 점수를 input으로 받기
T = 8

score = 0

score_lst = []
score_order = []

for tc in range(1, T+1):
    score = int(input())
    score_lst.append(score)
    score_order.append(tc)

#큰 순서부터 정렬한 복사한 리스트
score_top_down = sorted(score_lst, reverse=True)

total_score = 0
mid_order = []
final_order = ''

# 가장 큰 점수부터 5개를 합산
for i in range(5):
    total_score += score_top_down[i]

# 가장 큰 점수 5개의 인덱스를 활용하여서 새로운 리스트에 추가 후 다시금 작은수부터 재정렬
for i in range(5):
    mid_order.append(score_lst.index(score_top_down[i]) + 1)
mid_order.sort()

#넣어 준 점수를 하나씩 뽑아서 띄워쓰기를 추가하여 형식 맞추기
while mid_order:
    final_order = final_order + str(mid_order.pop(0)) + ' '


print(total_score)
print(final_order)

