import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(M)]
cnt = [[float('inf')] * N for _ in range(M)]
cnt[0][0] = 0
q = deque()
q.append([0, 0])
while q:
    state_i, state_j = q.popleft()
    for di, dj in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
        ni, nj = state_i + di, state_j + dj
        if 0 <= ni < M and 0 <= nj < N:
            tmp = cnt[state_i][state_j] + arr[ni][nj] # arr[ni][nj]가 벽이 있으면 1, 없으면 0
            if cnt[ni][nj] > tmp:
                cnt[ni][nj] = tmp
                q.append([ni, nj])

print(cnt[M-1][N-1])