# BOJ 2755. 이번 학기 평점은 몇점? (D1 / B1)
from decimal import Decimal

n = int(input())

# 등급-점수 딕셔너리: 부동소수점 오차를 피하기 위해 0.3에는 데시멀 적용
pair = {'A': 4,
        'B': 3,
        'C': 2,
        'D': 1,
        '+' : Decimal('0.3'),
        '0' : 0,
        '-' : Decimal('-0.3')}

total = 0
hours = 0
for _ in range(n):
    subject, hour, grade = input().split()
    hour = Decimal(hour)    # 데시멀 연산을 위해 변환

    if grade == 'F':
        score = 0
    else:
        score = pair[grade[0]] + pair[grade[1]]

    total += hour * score
    hours += hour

ans = total / hours
print(f"{ans:.2f}")

