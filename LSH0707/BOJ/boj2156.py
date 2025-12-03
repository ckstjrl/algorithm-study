import sys
input = sys.stdin.readline
N = int(input())
arr = [int(input()) for _ in range(N)]
dp = [0] * N
if N > 0:
    dp[0] = arr[0]
if N > 1:
    dp[1] = arr[0] + arr[1]
if N > 2:
    dp[2] = max(dp[1], arr[0]+arr[2], arr[1]+arr[2])
if N > 3:
    for i in range(3, N):  # (i-1, i 둘다 마심), (i-1안마심 i마심), (i 안마심)
        dp[i] = max(dp[i-3]+arr[i-1]+arr[i], dp[i-2] + arr[i], dp[i-1])
print(dp[-1])