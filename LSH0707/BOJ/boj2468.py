import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
min_r = float('inf')
max_r = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] > max_r:
            max_r = arr[i][j]
        if arr[i][j] < min_r:
            min_r = arr[i][j]

def safe(n):  # 비가 n만큼 왔을 때 생기는 안전구역의 수
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] - n <= 0:  # 물에 잠긴 좌표는 1로 표시
                visited[i][j] = 1
    cnt = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                # 전체 순회하면서 물에 안잠긴 구역에 대해 DFS(1로 표시) -> 안전구역cnt+1
                stack = []
                stack.append((i, j))
                visited[i][j] = 1
                while stack:
                    pi, pj = stack.pop()
                    for di,dj in [[-1,0],[1,0],[0,-1],[0,1]]:
                        ni = pi + di
                        nj = pj + dj
                        if 0 <= ni < N and 0 <= nj < N:
                            if visited[ni][nj] == 0:
                                stack.append((ni, nj))
                                visited[ni][nj] = 1
                cnt = cnt + 1
    return cnt

max_safe = 1
for x in range(min_r, max_r):  # 비의양 -> (최소높이 ~ 최대높이-1)
    a = safe(x)
    if a > max_safe:
        max_safe = a
print(max_safe)