# 19532. 수학은 비대면강의입니다
'''
ax + by = c
dx + ey = f

[입력]
정수
a, b, c, d, e, f가 공백으로 구분되어 차례대로 주어진다.

[출력]
x, y

방정식으로 풀어서 x, y를 계산
'''
a, b, c, d, e, f = map(int, input().split())
x = (b*f - c*e) // (b*d - a*e)
y = (a*f - c*d) // (a*e - b*d)
print(x, y)