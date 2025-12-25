import sys
input = sys.stdin.readline

N, K = map(int, input().split())

dp = [[0] * (K+1) for _ in range(N+1)]
dp[0][0] = 1

for i in range(N+1):
    for j in range(1, K+1):
        dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % 10**9

print(dp[N][K])