# BOJ15486(D3): 퇴사 2
import sys
input = sys.stdin.readline
N = int(input())
work = [tuple(map(int, input().split())) for _ in range(N)]
dp = [0] * (N + 1)
profit = 0
for i in range(N):
    profit = max(profit, dp[i])

    if i + work[i][0] > N:
        continue

    dp[i + work[i][0]] = max(profit + work[i][1], dp[i + work[i][0]])
print(max(dp))