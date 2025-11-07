'''
BOJ14466 : 소가 길을 건너간 이유 6 (G3)

해결 방법 : 
routes의 소 좌표에 길로 가야하는 곳을 인접리스트로 체크하기.
bfs로 소가 지나갈 수 있는 모든 곳을 체크하기. 그대신, 길로 가야하는 곳은 제외하기.
* bfs로 가야 갈 수 있는지 없는지 전부 체크가 가능.
각 소를 돌면서 bfs를 돌고, 조합이기 때문에, bfs 소보다 다음 인덱스에 있는 소들 중에 안 간 곳이 있는지 체크.
있으면 cnt

메모 : 
좌표 안에 인접리스트를 만들기 위해, 3차원(?)에 가까운 리스트를 만듬
'''
# routes = [[[] for _ in range(n)] for _ in range(n)]
# for i in range(r):
#     xa, ya, xb, yb = map(int, input().split())
#     routes[xa-1][ya-1].append((xb-1, yb-1))
#     routes[xb-1][yb-1].append((xa-1, ya-1))
# '''
# 조합을 굳이 구하지 않고, 다음 소가 있는지 확인하기. 슬라이싱으로 확인하는걸 새로 배웠다.
# '''
# for sx, sy in cows[i + 1:]: 
#         if not visited[sx][sy]: 
#             cnt += 1
'''
'''
from collections import deque

def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = 1
    while queue:
        si, sj = queue.popleft()
        for ni, nj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ti, tj = si + ni, sj + nj
            if 0<=ti<n and 0<=tj<n:
                if not visited[ti][tj]:
                    if (ti, tj) in routes[si][sj]:
                        continue
                    queue.append((ti, tj))
                    visited[ti][tj] = 1 
    return visited

n, k, r = map(int, input().split())

routes = [[[] for _ in range(n)] for _ in range(n)] # 인접리스트처럼 만들기
for i in range(r):
    xa, ya, xb, yb = map(int, input().split())
    routes[xa-1][ya-1].append((xb-1, yb-1))
    routes[xb-1][yb-1].append((xa-1, ya-1))

cows = []
for i in range(k):
    x, y = map(int, input().split())
    cows.append((x-1, y-1))

cnt = 0
for i, cow in enumerate(cows):
    visited = [[0] * n for _ in range(n)]
    bfs(cow[0],cow[1]) # 각 소의 x, y
    for sx, sy in cows[i + 1:]: # 다음 소 중에 (짝이기 때문에, 조합임 -> 다음에 있는 소만 확인)
        if not visited[sx][sy]: # 다음 소가 있는 칸을 가지 않았다면 세기
            cnt += 1

print(cnt)