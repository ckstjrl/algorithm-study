N = int(input())
num = list(map(int, input().split()))
ans = []
for i in range(N):
    ans.append(i + 1)
    cnt = num[i]
    while cnt > 0:
        ans[i - 1], ans[i] = ans[i], ans[i - 1]
        cnt -= 1
        i = i - 1
print(' '.join(map(str, ans)))
