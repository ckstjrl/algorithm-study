# BOJ1520(D3): 내리막 길
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]

# -1: 미방문, 0~양수: 도착지까지 가는 가짓수
dp = [[-1] * N for _ in range(M)]

def dfs(x, y):
    if x == M - 1 and y == N - 1:
        return 1
    
    if dp[x][y] != -1:
        return dp[x][y]
    
    dp[x][y] = 0
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < M and 0 <= ny < N:
            if arr[nx][ny] < arr[x][y]:
                dp[x][y] += dfs(nx, ny)
    
    return dp[x][y]

print(dfs(0, 0))