"""
BFS -> 가지치기 진행하면서 탐색
visited = visited[prev] + maps[cur]
"""

from collections import deque

def check(i,j):
    if 0 <= i < N and 0 <= j < N:
        return True
    else:
        return False

def bfs():
    visited = [[100000] * N for _ in range(N)]
    visited[0][0] = 1
    q = deque()
    q.append([0,0])
    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]
    while q:
        i,j = q.popleft()
        for d in range(4):
            ni, nj = i+di[d], j+dj[d]
            if check(ni,nj):
                if visited[ni][nj] > visited[i][j] + maps[ni][nj]:
                    visited[ni][nj] = visited[i][j] + maps[ni][nj]
                    q.append([ni,nj])
    return visited


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    maps = [list(map(int,input())) for _ in range(N)]
    visited = bfs()
    print(f"#{test_case} {visited[N-1][N-1]-1}")