import sys
input = sys.stdin.readline

T = int(input())


def dfs(node, cnt):
    visited[node] = 1
    for i in graph[node]:
        if not visited[i]:
            cnt = dfs(i, cnt+1)
    return cnt


for _ in range(T):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [0] * (N+1)
    print(dfs(1, 0))