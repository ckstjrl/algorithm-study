import sys
input = sys.stdin.readline

N = int(input())
arr = [[0, 0]] # dummy
for _ in range(N):
    arr.append(list(map(int, input().split())))

dp = [0] * (N + 1)

for i in range(1, N + 1):
    t, p = arr[i]
    dp[i] = max(dp[i], dp[i - 1])
    if i + t - 1 <= N: # i + t - 1: 마지막 날
        dp[i + t - 1] = max(dp[i + t - 1], dp[i - 1] + p)

print(dp[N])