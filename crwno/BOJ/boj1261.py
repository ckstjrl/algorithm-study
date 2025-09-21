from heapq import heappop, heappush


def dijkstra(x, y, cnt):

    pq = [(cnt, x - 1, y - 1)]
    cnt_arr = [[10000] * N for _ in range(M)]
    cnt_arr[x - 1][y - 1] = 0

    while pq:
        cnt, sx, sy = heappop(pq)
        if cnt_arr[sx][sy] < cnt:
            continue
        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
            nx, ny = sx + dx, sy + dy
            if 0 <= nx < M and 0 <= ny < N:

                new_cnt = cnt + walls[nx][ny]

                if cnt_arr[nx][ny] <= new_cnt:
                    continue
                cnt_arr[nx][ny] = new_cnt
                heappush(pq, (new_cnt, nx, ny))

    return cnt_arr[M - 1][N - 1]


N, M = map(int, input().split())
walls = [list(map(int, input())) for _ in range(M)]

print(dijkstra(1, 1, 0))