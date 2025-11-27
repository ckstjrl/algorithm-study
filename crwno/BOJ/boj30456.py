N, L = map(int, input().split())
ans = []
for i in range(L - 1):
    ans.append(1)
ans.append(N)

for i in ans:
    print(i, end='')