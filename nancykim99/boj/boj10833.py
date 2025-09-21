'''
(BOJ10833 / D1): 사과
'''

N = int(input())

rem_sum = 0
for _ in range(N):
    student, apple = map(int, input().split())
    rem_sum += (apple % student)

print(rem_sum)