# BOJ4963: 섬의 개수
import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]

while True:
    w, h = map(int, input().split())
    
    if w == 0 and h == 0:
        break

    arr = [input().split() for _ in range(h)]
    visited = list([False for _ in range(w)] for _ in range(h))
    total = 0

    for i in range(h):
        for j in range(w):
            if arr[i][j] == '0' or visited[i][j]:
                continue

            q = deque([(i, j)])
            visited[i][j] = True
            while q:
                x, y = q.popleft()
                for d in range(8):
                    nx, ny = x + dx[d], y + dy[d]
                    if nx < 0 or ny < 0 or nx >= h or ny >= w or arr[nx][ny] == '0' or visited[nx][ny]:
                        continue
                    q.append((nx, ny))
                    visited[nx][ny] = True
            total += 1
    
    print(total)
