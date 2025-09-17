# BOJ1261(D3): 알고스팟
# 해결방법: 우선순위큐를 이용한 다익스트라
# 메모리: 112108KB, 시간: 140ms
# 가장 빠른 거 따라했지만 크게 차이는 없었다...
# 비용이 0 또는 1로 고정되어있어서 다익스트라보다 BFS가 더 적합했을 듯!
from heapq import heappush, heappop
import sys

input = sys.stdin.readline

def dijkstra():
    pq = [(0, 0, 0)]
    dist[0][0] = 0

    while pq:
        cost, i, j = heappop(pq)

        if dist[i][j] < cost:
            continue
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = i + di, j + dj
            if ni < 0 or ni >= N or nj < 0 or nj >= M:
                continue
            n_cost = cost + board[ni][nj]
            if n_cost < dist[ni][nj]:
                dist[ni][nj] = n_cost
                heappush(pq, (n_cost, ni, nj))

M, N = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(N)]
dist = [[float('inf')] * M for _ in range(N)]

dijkstra()
print(dist[N-1][M-1])

#----------------------------------------------------

# 개선된 정답!이지만 더 효율적인 알고리즘이 있었다!
# 해결방법 : deque을 이용한 개선된 BFS
# 메모리: 114360KB, 시간: 120ms
# from collections import deque

# def bfs():
#     q = deque([(0, 0)])
#     visit_cost[0][0] = 0

#     while q:
#         x, y = q.popleft()
#         c_cost = visit_cost[x][y]

#         if x == N - 1 and y == M - 1:
#             return c_cost

#         for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
#             nx, ny = x + dx, y + dy
#             if nx < 0 or ny < 0 or nx >= N or ny >= M:
#                 continue
#             n_cost = c_cost + arr[nx][ny]
#             if visit_cost[nx][ny] == -1 or visit_cost[nx][ny] > n_cost:
#                 visit_cost[nx][ny] = n_cost
#                 if arr[nx][ny] == 0:  # 비용이 0이면 앞쪽
#                     q.appendleft((nx, ny))
#                 else:  # 비용이 1이면 뒤쪽에 추가
#                     q.append((nx, ny))

#     return visit_cost[N-1][M-1]


# M, N = map(int, input().split())  # M: 가로크기, N: 세로크기
# arr = list(list(map(int, input())) for _ in range(N))
# visit_cost = [[-1] * M for _ in range(N)]

# ans = bfs()

# print(ans)

#----------------------------------------------------

# 정답!이지만 남들과 달리 메모리와 시간이 많이 걸렸음(다시풀기)
# 해결방법 : 큐를 이용한 BFS
# 메모리: 121288KB, 시간: 204ms
# from collections import deque

# def bfs():
#     q = deque([(0, 0, 0)])  # x좌표, y좌표, cost
#     visit_cost[0][0] = 0
#     while q:
#         x, y, cost = q.popleft()
#         for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
#             nx, ny = x + dx, y + dy
#             if nx < 0 or ny < 0 or nx >= N or ny >= M:
#                 continue
#             if arr[nx][ny] == 1:
#                 n_cost = cost + 1
#             else:
#                 n_cost = cost
#             if visit_cost[nx][ny] == -1 or visit_cost[nx][ny] > n_cost:
#                 visit_cost[nx][ny] = n_cost
#                 q.append((nx, ny, n_cost))



# M, N = map(int, input().split())  # M: 가로크기, N: 세로크기
# arr = list(list(map(int, input())) for _ in range(N))
# visit_cost = [[-1] * M for _ in range(N)]

# bfs()

# print(visit_cost[N-1][M-1])