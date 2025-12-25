N = int(input())

ans = [['*'] * N for _ in range(N)]


def f(x):
    for i in range(N):
        for j in range(N):
            if i//x % 3 == 1 and j//x % 3 == 1:
                ans[i][j] = ' '


k = 0
n = N
while n > 1:
    f(3**k)
    n = n // 3
    k += 1


for i in range(N):
    print(''.join(ans[i]))