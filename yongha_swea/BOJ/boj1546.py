#boj1546 평균

#N: 시험 본 과목 수
N = int(input())

score = list(map(int, input().split()))

M = max(score)

ans = 0

#각 과목 점수
for i in score:
    ans += ((i/M) * 100)

#평균을 위해 과목수로 나누기
ans = ans / len(score)

print(f'{float(ans)}')