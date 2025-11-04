# BOJ2583(D2): 영역 구하기
from collections import deque

M, N, K = map(int, input().split())

arr = [[0] * N for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            arr[y][x] = 1

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(y, x):
    visited[y][x] = True
    area = 1
    q = deque([(y, x)])
    while q:
        y, x = q.popleft()  # y축, x축, 넓이
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < M and 0 <= nx < N and arr[ny][nx] == 0 and not visited[ny][nx]:
                q.append((ny, nx))
                area += 1
                visited[ny][nx] = True
    return area

visited = [[False] * N for _ in range(M)]
areas = []
for y in range(M):
    for x in range(N):
        if arr[y][x] == 1 or visited[y][x] == True:
            continue
        areas.append(bfs(y, x))
areas.sort()

print(len(areas))
print(*areas)