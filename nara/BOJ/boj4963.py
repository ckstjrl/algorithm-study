import sys
from collections import deque
input = sys.stdin.readline

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(h)]
    visit = [[False] * w for _ in range(h)]
    cnt = 0

    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    def bfs(x, y):
        q = deque()
        q.append((x, y))
        visit[x][y] = True

        while q:
            cx, cy = q.popleft()
            for d in range(8):
                nx, ny = cx + dx[d], cy + dy[d]
                if 0 <= nx < h and 0 <= ny < w:
                    if not visit[nx][ny] and graph[nx][ny] == 1:
                        visit[nx][ny] = True
                        q.append((nx, ny))

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and not visit[i][j]:
                bfs(i, j)
                cnt += 1

    print(cnt)