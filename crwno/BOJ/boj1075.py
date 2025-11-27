N = int(input())
F = int(input())

p = N % F
q = N % 100

res = q + (F - p)

while res >= F:
    res -= F

ans = str(res)

if len(ans) == 1:
    print('0' + ans)
elif len(ans) == 3:
    print(ans[1] + ans[2])
else:
    print(ans)