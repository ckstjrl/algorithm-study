import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
graph = [list(map(str, input().strip())) for _ in range(M)]

visit = [[False] * N for _ in range(M)]

def bfs(i, j, color):
    q = deque()
    q.append([i, j])
    visit[i][j] = True
    cnt = 1
    while q:
        i, j = q.popleft()
        for di, dj in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < M and 0 <= nj < N and not visit[ni][nj] and graph[ni][nj] == color:
                visit[ni][nj] = True
                q.append([ni, nj])
                cnt += 1
    return cnt

blue = 0
white = 0
for i in range(M):
    for j in range(N):
        if graph[i][j] == 'B' and not visit[i][j]:
            blue += bfs(i, j, 'B') ** 2
        if graph[i][j] == 'W' and not visit[i][j]:
            white += bfs(i, j, 'W') ** 2
print(white, blue)