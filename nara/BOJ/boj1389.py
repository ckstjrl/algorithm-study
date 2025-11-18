import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
graph = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

def bfs(start, end):
    visit = [False] * (N+1)
    distance = [0] * (N+1)
    q = deque([start])
    while q:
        now = q.popleft()
        if now == end:
            return distance[now]
        for i in range(1, N+1):
            if not visit[i] and graph[now][i] == 1:
                visit[i] = True
                distance[i] = distance[now] + 1
                q.append(i)
    return -1

def kevinbacon(node):
    num = 0
    for i in range(1, N+1):
        if i != node:
            num += bfs(node, i)
    return num

relations = [0]
for i in range(1, N+1):
    relations.append(kevinbacon(i))
print(relations.index(min(relations[1:])))
