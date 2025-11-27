import sys
from collections import deque
input = sys.stdin.readline

dir = [[0, 0, -1], [0, 0, 1], [0, -1, 0], [0, 1, 0], [-1, 0, 0], [1, 0, 0]]


def bfs():
    while q:
        h, i, j = q.popleft()
        for dh, di, dj in dir:
            nh, ni, nj = h + dh, i + di, j + dj
            if 0 <= nh < H and 0 <= ni < N and 0 <= nj < M:
                if tomato[nh][ni][nj] == 0:
                    tomato[nh][ni][nj] = tomato[h][i][j] + 1
                    q.append([nh, ni, nj])


M, N, H = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

dir = [[0, 0, -1], [0, 0, 1], [0, -1, 0], [0, 1, 0], [-1, 0, 0], [1, 0, 0]]

q = deque()
for h in range(H):
    for i in range(N):
        for j in range(M):
            if tomato[h][i][j] == 1:
                q.append([h, i, j])

bfs()

day = 0
for h in range(H):
    for i in range(N):
        for j in range(M):
            if tomato[h][i][j] == 0:
                print(-1)
                sys.exit(0)
            day = max(day, tomato[h][i][j])
print(day - 1)