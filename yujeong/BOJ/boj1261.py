# 1261. 알고스팟

from heapq import heappop, heappush

# 벽 부수는 횟수가 최소인 경로를 탐색하는 함수 dijkstra()
def dijkstra(x, y):
    pq = [(0, (x, y))]
    visited = [[1e9] * M for _ in range(N)]
    visited[x][y] = 0

    while pq:
        cnt, (px, py) = heappop(pq)
        if px==N-1 and py==M-1: # (N, M)에 도착하면
            return cnt          # 그때까지 벽 부순 횟수 리턴
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = px+dx, py+dy
            if 0<=nx<N and 0<=ny<M:
                new_cnt = cnt + maze[nx][ny]
                # 벽 부수는 횟수가 최소인 경우로 갱신
                if visited[nx][ny] > new_cnt:
                    visited[nx][ny] = new_cnt
                    heappush(pq, (visited[nx][ny], (nx, ny)))


M, N = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]

ans = dijkstra(0, 0)
print(ans)