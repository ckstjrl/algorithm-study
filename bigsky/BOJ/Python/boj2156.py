# BOJ2156: 포도주 시식
import sys
input = sys.stdin.readline

n = int(input())
wines = [0] * 10000
for i in range(n):
    wines[i] = int(input())

dp = [0] * 10000

dp[0] = wines[0]
if n > 1:
    dp[1] = wines[0] + wines[1]
if n > 2:
    dp[2] = max(wines[2] + wines[0], wines[2] + wines[1], dp[1])

for i in range(3, n):
    dp[i] = max(dp[i-1], dp[i-3] + wines[i-1] + wines[i], dp[i-2] + wines[i])

print(dp[n-1])


# 완전탐색 시간초과
# n = int(input())
# wines = []
# for i in range(n):
#     wines.append(int(input()))
# tasted = [False] * n
#
# result = 0
#
# def dfs(idx, total):
#     global result
#     if idx == n:
#         result = max(result, total)
#         return
#
#     dfs(idx+1, total)
#
#     if not (idx >= 2 and tasted[idx-2] and tasted[idx-1]):
#         tasted[idx] = True
#         dfs(idx+1, total + wines[idx])
#         tasted[idx] = False
#
# dfs(0, 0)
# print(result)