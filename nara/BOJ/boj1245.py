import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

q = deque()
visit = [[False] * M for _ in range(N)]

di = [-1, -1, -1, 0, 0, 1, 1, 1]
dj = [-1, 0, 1, -1, 1, -1, 0, 1]
flag = 0

def bfs(x, y):
    q.append([x, y])
    visit[x][y] = True
    flag = True
    while q:
        i, j = q.popleft()
        for c in range(8):
            ni, nj = i + di[c], j + dj[c]
            if 0 <= ni < N and 0 <= nj < M:
                if graph[ni][nj] > graph[x][y]:
                    flag = False
                if not visit[ni][nj] and graph[ni][nj] == graph[x][y]:
                    visit[ni][nj] = True
                    q.append([ni, nj])
    return flag

cnt = 0
for i in range(N):
    for j in range(M):
        if not visit[i][j]:
            if bfs(i, j):
                cnt += 1
print(cnt)