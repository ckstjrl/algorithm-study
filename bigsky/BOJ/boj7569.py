# BOJ7569(D3): 토마토
from collections import deque
import sys
input = sys.stdin.readline

def check_unripe(arr):
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if arr[h][i][j] == 0:
                    return False
    return True

M, N, H = map(int, input().split())
arr = [[list(map(int, input().strip().split())) for _ in range(N)] for _ in range(H)]

ripe_tomatoes = deque()
for h in range(H):
    for i in range(N):
        for j in range(M):
            if arr[h][i][j] == 1:
                ripe_tomatoes.append((h, i, j, 0))

min_days = 0

while ripe_tomatoes:
    h, i, j, day = ripe_tomatoes.popleft()
    min_days = max(min_days, day)
    for dh, di, dj in [[1, 0, 0], [-1, 0, 0], [0, 0, 1], [0, 1, 0], [0, 0, -1], [0, -1, 0]]:
        nh, ni, nj = h + dh, i + di, j + dj
        if 0 <= nh < H and 0 <= ni < N and 0 <= nj < M and arr[nh][ni][nj] == 0:
            arr[nh][ni][nj] = 1
            ripe_tomatoes.append((nh, ni, nj, day+1))

if check_unripe(arr):
    print(min_days)
else:
    print(-1)