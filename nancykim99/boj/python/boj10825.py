'''
BOJ10825 / D2): 국영수

해결 방법 : 그냥 구현
'''

N = int(input())

grade = []
for tc in range(N):
    name, korean, english, mathematics = input().split()
    grade.append((name, int(korean), int(english), int(mathematics)))

# - : 내림차순
grade.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in range(N):
    print(grade[i][0])