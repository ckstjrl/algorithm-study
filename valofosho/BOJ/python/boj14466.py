"""
BOJ14466 - 소가 길을 건너간 이유 6

문제 정의
1. 소가 길을 건너간 이유는 길이 많아서
2. 길이 너무 많아서 길을 건너지 않고는 돌아다니기 힘듬
3. 인접한 목초지 사이는 일반적으로 자유롭게 이동
4. 그 중 일부는 길을 건너야 한다
5. 소들은 각각 다른 목초지에 위치하고, 어떤 두 소는 길을 건너지 않으면 만나지 못할 수 있다.
6. 해당하는 소들의 쌍은 몇 쌍인가

- N: 목장 크기 K: 소 마리 수 R: 길의 개수

Ki에서 ki+1로 가는 경로 중 길을 지나지 않고 가면 pass
길을 건너면 +1

2차원 배열

로직 정의
1. 하나의 소에서 다른 소로 가는 걸 찾는데 가는 중에 길 피하고 범위 내로만 이동
2. 만약 큐가 비었는데도 안되면 쌍에 추가하기
---

상세 로직
우선 하나의 소에서 다른 소로 가는 길이 있는지를 확인하는 코드는 BFS를 활용 
"""

import sys
from collections import deque
input = sys.stdin.readline

def check(i,j, N):
    if 0<=i<N and 0<=j<N:
        return True
    else:
        return False
    
def bfs(start, goal):
    i, j = start
    visited[i][j] = True
    q = deque([start])
    arrived = False
    gi, gj = goal
    while q:
        i,j = q.popleft()
        # 무사 도착이면 break
        if (i,j) == (gi,gj):
            arrived = True
            break        
        for d in range(4):
            ni, nj = i+di[d], j+dj[d]
            # 범위를 벗어나지 않고, 방문한 적이 없어야 함 일단
            if check(ni, nj, N) and not visited[ni][nj]:
               # 길이면 건너면 안됨
                if (i,j,ni,nj) in roads:
                    continue
                else:
                    visited[ni][nj] = True
                    q.append((ni,nj))

    return True if arrived else False

N, K, R = map(int, input().split())
# roads = [[0]*N for _ in range(N)] # 도로 위치 기록용
cows = []
roads = set()
for _ in range(R):
    r1, c1, r2, c2 = map(int, input().split())
    # BFS에서 방향은 양방향 모두 가능함
    roads.add((r1-1,c1-1,r2-1,c2-1))
    roads.add((r2-1,c2-1,r1-1,c1-1))

for _ in range(K):
    r, c= map(int, input().split())
    cows.append((r-1,c-1))

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

# 소는 한 쪽에서 다른 한쪽으로의 경우의 수만 활용
total = 0
for i in range(K-1):
    for j in range(i+1,K):
        start = cows[i]
        goal = cows[j]
        visited = [[False]*N for _ in range(N)] # BFS 기록용
        if not bfs(start, goal):
            total += 1
print(total)