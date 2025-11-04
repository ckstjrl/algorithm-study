# BOJ2533(D3): 사회망 서비스(SNS)
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
g = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

dp = [[0, 0] for _ in range(N + 1)]

visited = [False] * (N + 1)

def dfs(node):
    visited[node] = True
    dp[node][1] = 1

    for n_node in g[node]:
        if not visited[n_node]:
            dfs(n_node)
            dp[node][0] += dp[n_node][1]
            dp[node][1] += min(dp[n_node][0], dp[n_node][1])

dfs(1)
print(min(dp[1][0], dp[1][1]))




# 이분그래프 문제인가 했지만 이분그래프 문제가 아니었다...
# from collections import deque
# import sys
# input = sys.stdin.readline
#
# N = int(input())
# g = [[] for _ in range(N + 1)]
# for _ in range(N - 1):
#     a, b = map(int, input().split())
#     g[a].append(b)
#     g[b].append(a)
#
# group = [0] * (N + 1) # 얼리어답터o/x: 1, 얼리어답터x/o: 2
#
# group[1] = 1
# q = deque([1])
# while q:
#     node = q.popleft()
#     for n_node in g[node]:
#         if group[n_node] != 0:
#             continue
#         if group[node] == 1:
#             group[n_node] = 2
#         else:
#             group[n_node] = 1
#         q.append(n_node)
# print(group)
# print(min(group.count(1), group.count(2)))