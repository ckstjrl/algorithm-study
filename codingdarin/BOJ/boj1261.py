import heapq
import sys

input = lambda: sys.stdin.readline().rstrip()

M, N = map(int, input().split())
maze = [input() for _ in range(N)]

# 다익스트라로 최단경로 찾기
dist = [[float('inf')] * M for _ in range(N)]  # 거리 배열
dist[0][0] = 0
pq = [(0, 0, 0)]  # (비용, x, y)

# 델타 배열
dx = [0,1,0,-1]
dy = [1,0,-1,0]

while pq:
    cost, x, y = heapq.heappop(pq)
    
    # 목표 도달시 종료
    if x == N-1 and y == M-1:
        print(cost)
        break
    
    # 이미 더 짧은 경로가 있으면 스킵
    if dist[x][y] < cost:
        continue
    
    # 4방향 탐색
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        
        if 0 <= nx < N and 0 <= ny < M:
            new_cost = cost + int(maze[nx][ny])  # 벽이면 +1, 빈방이면 +0
            
            if new_cost < dist[nx][ny]:
                dist[nx][ny] = new_cost
                heapq.heappush(pq, (new_cost, nx, ny))