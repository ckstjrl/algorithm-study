import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

M, N = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(M)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def dfs(x, y):
    visited[x][y] = True
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] == 0 and not visited[nx][ny]:
            dfs(nx, ny)


visited = [[False]*N for _ in range(M)]

for y in range(N):
    if graph[0][y] == 0 and not visited[0][y]:
        dfs(0, y)

if True in visited[M-1]:
    print('YES')
else:
    print('NO')