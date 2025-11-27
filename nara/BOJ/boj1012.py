import sys
sys.setrecursionlimit(10**6)
T = int(sys.stdin.readline())
def dfs (x, y):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if arr[ny][nx] == 1:
                arr[ny][nx] = 0
                dfs(nx, ny)
for tc in range(1, T + 1):
    M, N, K = map(int, sys.stdin.readline().split())
    arr = [[0] * M for _ in range(N)]
    for _ in range(K):
        i, j = map(int, sys.stdin.readline().split())
        arr[j][i] = 1
    cnt = 0
    for i in range(M):
        for j in range(N):
            if arr[j][i] == 1:
                cnt += 1
                dfs(i, j)
    print(cnt)