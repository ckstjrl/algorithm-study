import sys
from collections import deque
input = sys.stdin.readline

M, N, K = map(int, input().split())
graph = [[0] * N for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            graph[j][i] = 1

def bfs(x, y):
    global result
    q = deque()
    q.append([x, y])
    graph[x][y] = 1
    size = 1
    while q:
        x, y = q.popleft()
        for i in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            nx, ny = x + i[0], y + i[1]
            if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] == 0:
                graph[nx][ny] = 1
                q.append([nx, ny])
                size += 1
    result.append(size)

result = []
for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            bfs(i, j)

result.sort()
print(len(result))
for i in result:
    print(i, end=' ')