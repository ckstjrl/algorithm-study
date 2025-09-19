'''
(BOJ10984 / D1): 내 학점을 구해줘
'''

N = int(input())

for _ in range(N):
    semester = int(input())
    class_n = 0
    grade_pre = 0
    for _ in range(semester):
        x, y = map(float, input().split())
        class_n += int(x)
        grade_pre += int(x) * y


    grade = round(grade_pre / class_n, 1)
    print(class_n, grade)
