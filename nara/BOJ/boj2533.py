import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(node):
    visit[node] = True
    for i in graph[node]:
        if not visit[i]:
            dfs(i)
            dp[node][0] += dp[i][1]
            dp[node][1] += min(dp[i][0], dp[i][1])


N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visit = [False] * (N+1)
dp = [[0, 1] for _ in range(N+1)]
dfs(1)

print(min(dp[1][0], dp[1][1]))