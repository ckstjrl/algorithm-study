# BOJ14500(D3): 테트로미노

def dfs(x, y, cnt, total):
    global ans

    if cnt == 4:
        ans = max(ans, total)
        return

    for dx, dy in [[0, 1], [1, 0], [0, -1],[-1, 0]]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            visited[nx][ny] = 1
            dfs(nx, ny, cnt + 1, total + arr[nx][ny])
            visited[nx][ny] = 0

def check_T(x, y):
    global ans

    shapes = [[(0, 0), (0, 1), (0, 2), (-1, 1)],
               [(0, 0), (0, 1), (0, 2), (1, 1)],
               [(0, 0), (1, 0), (2, 0), (1, 1)],
               [(0, 0), (1, 0), (2, 0), (1, -1)]]

    for shape in shapes:
        total = 0
        flag = 1
        for i, j in shape:
            nx, ny = x + i, y + j
            if 0 <= nx < N and 0 <= ny < M:
                total += arr[nx][ny]
            else:
                flag = 0
                break
        if flag:
            ans = max(ans, total)

# Main
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(i, j, 1, arr[i][j])
        visited[i][j] = 0

        check_T(i, j)

print(ans)