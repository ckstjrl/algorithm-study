N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

visited = [[-1] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            x, y = i, j
        elif arr[i][j] == 0:
            visited[i][j] = 0


front = rear = -1


rear += 1
q = [0] * ((M*N*2)+1)
q[rear] = x
rear += 1
q[rear] = y
visited[x][y] = 0
while front != rear:
    front += 1
    i = q[front]
    front += 1
    j = q[front]

    for dx, dy in [[1,0], [-1, 0], [0, 1], [0, -1]]:
        nx = i + dx
        ny = j + dy
        if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1 and visited[nx][ny] < 0:
            visited[nx][ny] = visited[i][j] + 1
            rear += 1
            q[rear] = nx
            rear += 1
            q[rear] = ny
            
for i in range(N):
    print(*visited[i])