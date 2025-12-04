N = int(input())
ans = [0] * (N+1)
if N > 2:
    ans[1] = 1
    ans[2] = 2
    for i in range(3, N+1):  # (i-2길이 갯수 + 00) + (i-1길이 갯수 + 1)
        ans[i] = (ans[i-1] + ans[i-2]) % 15746
if N < 3:
    print(N)
else:
    print(ans[N])