import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)

def bfs(start):
    visit = [False] * (N+1)
    visit[start] = True
    q = deque([start])
    cnt = 0
    while q:
        c = q.popleft()
        for n in graph[c]:
            if not visit[n]:
                visit[n] = True
                cnt += 1
                q.append(n)
    return cnt

result = [0] * (N+1)
max_cnt = 0
for i in range(1, N+1):
    result[i] = bfs(i)
    if result[i] > max_cnt:
        max_cnt = result[i]

for i in range(1, N+1):
    if result[i] == max_cnt:
        print(i, end=' ')