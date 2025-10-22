# BOJ 2822. 점수 계산 (D1 / S5)

scores = []
for i in range(1, 9):
    scores.append((int(input()), i))

scores.sort(reverse=True)

# 합 출력
print(sum(score[0] for score in scores[0:5]))  

# 번호 출력 (오름차순 정렬 필요)
nums = sorted([scores[i][1] for i in range(5)])
for num in nums:
    print(num, end=' ')