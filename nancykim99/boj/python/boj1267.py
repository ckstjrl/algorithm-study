'''
(BOJ1267 / D1): 휴대폰 요금
'''

N = int(input())
call = list(map(int, input().split()))

Y = 0
M = 0
for i in range(N):
    Y += ((call[i] // 30) + 1) * 10
    M += ((call[i] // 60) + 1) * 15

if Y > M:
    print(f'M {M}')
elif Y < M:
    print(f'Y {Y}')
else:
    print(f'Y M {Y}')
