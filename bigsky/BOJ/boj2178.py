# BOJ2178: 미로 탐색

from collections import deque
import sys

def bfs(N, M, maze):
    q = deque([(0, 0, 1)]) # (i, j, cnt)
    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1

    while q:
        ci, cj, c_cnt = q.popleft()

        if (ci, cj) == (N-1, M-1):
            return c_cnt
        
        for di, dj in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M and maze[ni][nj] == 1 and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                q.append((ni, nj, c_cnt + 1))

N, M = map(int, sys.stdin.readline().split())
maze = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

print(bfs(N, M, maze))