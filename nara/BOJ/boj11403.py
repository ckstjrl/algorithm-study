import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]


def dfs(start):
    visit = [0] * N
    stack = [start]
    while stack:
        node = stack.pop()
        for next_node in range(N):
            if graph[node][next_node] == 1 and visit[next_node] == 0:
                visit[next_node] = 1
                stack.append(next_node)
    return visit


for i in range(N):
    print(*dfs(i))