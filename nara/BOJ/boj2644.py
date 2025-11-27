import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
s1, s2 = map(int, input().split())
m = int(input())
relation = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    relation[a][b] = 1
    relation[b][a] = 1


def bfs(start, end):
    visit = [False] * (n+1)
    distance = [0] * (n+1)
    q = deque([start])
    while q:
        now = q.popleft()
        if now == end:
            return distance[now]
        for i in range(1, n+1):
            if not visit[i] and relation[now][i] == 1:
                visit[i] = True
                distance[i] = distance[now] + 1
                q.append(i)
    return -1


print(bfs(s1, s2))