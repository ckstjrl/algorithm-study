import sys
input = sys.stdin.readline
from collections import deque
M, N = map(int, input().split())
arr = [list(input().strip()) for _ in range(M)]
visited = [[0]*N for _ in range(M)]
q = deque()
ans = 'NO'
for j in range(N):
    if arr[0][j] == '0':  # 처음으로 전류 공급되는 좌표 q에 append
        q.append((0, j)) 
        visited[0][j] = 1  # 방문 기록

while q:
    ci, cj = q.pop()
    for di,dj in [[1,0],[-1,0],[0,1],[0,-1]]:
        ni = ci + di 
        nj = cj + dj
        if 0 <= ni < M and 0 <= nj < N:
            if arr[ni][nj] == '0' and visited[ni][nj] == 0:  
                visited[ni][nj] = 1
                q.append((ni, nj))
                if ni == M-1: # 다음 인접좌표 가장 밑에 도달하면 break 
                    ans = 'YES'
                    break

print(ans)