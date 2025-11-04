# 1926. 그림
import sys
input = sys.stdin.readline
from collections import deque

# BFS로 연결된 영역을 탐색하며 가장 넓은 그림 크기를 갱신하는 함수 bfs()
def bfs(x, y):
    global cnt, max_area
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    temp = 0    # 이번 그림의 크기
    while q:
        px, py = q.pop()
        temp += 1   
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = px + dx, py + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and board[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True
    max_area = max(temp, max_area)


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
cnt = 0         # 그림 개수
max_area = 0    # 가장 넓은 그림 크기 
visited = [[False] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        # 그림이 있는 영역이고 아직 탐색하지 않았으면 bfs()
        if board[i][j] == 1 and not visited[i][j]:  
            bfs(i, j)
            cnt += 1  

print(cnt)
print(max_area)