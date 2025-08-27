# 14940. 쉬운 최단거리 
import sys
input = sys.stdin.readline

from collections import deque

def bfs(n, m):
    q = deque()
    visited = [[-1] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):          # visited 배열에서 출발지(목표지점)과 원래 갈 수 없는 곳 표시
            if arr[i][j] == '2':
                q.append((i, j))
                visited[i][j] = 0
            elif arr[i][j] == '0':
                visited[i][j] = 0    
    
    while q:
        px, py = q.popleft()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = px+dx, py+dy
            if 0<=nx<n and 0<=ny<m and arr[nx][ny] == '0':      # 갈 수 없는 곳에 막힘
                continue                                        # 다른 방향으로

            elif 0<=nx<n and 0<=ny<m and arr[nx][ny] == '1':    # 갈 수 있는 곳
                if visited[nx][ny] == -1:                       # 방문한 적 없는 곳이면
                    visited[nx][ny] = visited[px][py] + 1       # 거리 업데이트
                    q.append((nx, ny))
    
    for v in visited:
        print(*v)

n, m = map(int, input().split())
arr = [list(input().split()) for _ in range(n)]
bfs(n, m)
