# 2178. 미로 탐색 

def bfs():
    q = []
    q.append((0, 0))   # (1, 1)에서 시작 (근데 배열 인덱스는 (0, 0))

    while q:
        px, py = q.pop(0)
        if (px, py) == (N-1, M-1):  # 목적지 (N, M)에 도착
            return
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:   # 상하좌우로 움직임
            nx, ny = px+dx, py+dy
            if 0<=nx<N and 0<=ny<M and maze[nx][ny] == '1' and not visited[nx][ny]:
                visited[nx][ny] = visited[px][py] + 1   # 움직인 칸수 업데이트
                q.append((nx, ny))


N, M = map(int, input().split())

maze = [list(input()) for _ in range(N)]
visited = [[0]*M for _ in range(N)]         # 움직인 칸 수 저장할 배열 
visited[0][0] = 1                           # 시작 위치는 이미 지난 칸이므로 1로

bfs()
print(visited[N-1][M-1])                    # (N, M)의 값 출력