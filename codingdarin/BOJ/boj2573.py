# BOJ 2573. 빙산 (G4 / D3)

from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 델타 배열
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

# 녹이기
def melt():
    melting = [[0] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0:
                sea_count = 0
                for k in range(4):
                    ni, nj = i + di[k], j + dj[k]
                    if graph[ni][nj] == 0:
                        sea_count += 1
                melting[i][j] = sea_count
    
    for i in range(n):
        for j in range(m):
            graph[i][j] = max(0, graph[i][j] - melting[i][j])

# 빙산 세기 
def count_ice():
    visited = [[False] * m for _ in range(n)]
    count = 0
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0 and not visited[i][j]:
                count += 1
                queue = deque([(i, j)])
                visited[i][j] = True
                
                while queue:
                    ci, cj = queue.popleft()
                    for k in range(4):
                        ni, nj = ci + di[k], cj + dj[k]
                        if 0 <= ni < n and 0 <= nj < m:
                            if graph[ni][nj] > 0 and not visited[ni][nj]:
                                visited[ni][nj] = True
                                queue.append((ni, nj))
    return count

year = 0
while True:
    ice_count = count_ice()
    
    if ice_count >= 2:
        print(year)
        break
    if ice_count == 0:
        print(0)
        break
    
    melt()
    year += 1