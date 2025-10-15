# SWEA1249: 보급로
from heapq import heappop, heappush

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input())) for _ in range(N)]
    INF = float('inf')
    dist = [[INF] * N for _ in range(N)]
    
    dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    pq = [(0, 0, 0)]
    dist[0][0] = data[0][0]

    while pq:
        c, x, y = heappop(pq)
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if dist[nx][ny] > c + data[x][y]:
                    dist[nx][ny] = c + data[x][y]
                    heappush(pq, (dist[nx][ny], nx, ny))

    print(f'#{tc} {dist[N-1][N-1]}')