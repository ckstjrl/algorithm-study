N = int(input())

cnt = 1
ans = 1
while cnt < N:
    cnt += 6 * ans 
    ans += 1

print(ans)
