'''
BOJ2665 : 미로만들기 (G4)

해결 방법 : 
bfs에 visited 그래프와 distance 그래프를 따로 둬서 최소 경로 찾기 <- 이럴꺼면 다익스트라로 풀어도 됐을껄...

메모 : 
자꾸 까먹는 `appendleft()` : 시간복잡도 O(1)
'''
from collections import deque

n = int(input())
room = [list(input()) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
distance = [[0]*n for _ in range(n)]

def bfs(i, j):
    q = deque()
    q.append((i, j))
    while q:
        ti, tj = q.popleft()
        if ti == (n-1) and tj == (n-1):
            return distance[ti][tj]
        for si, sj in ([0,1], [1,0], [0,-1], [-1, 0]):
            ni, nj = ti + si, tj + sj
            if 0 <= ni < n and 0 <= nj < n:
                if not visited[ni][nj]:
                    visited[ni][nj] = 1
                    if room[ni][nj] == '1':
                        q.appendleft((ni, nj))
                        distance[ni][nj] = distance[ti][tj]
                    else:
                        q.append((ni, nj))
                        distance[ni][nj] = distance[ti][tj] + 1

print(bfs(0,0))