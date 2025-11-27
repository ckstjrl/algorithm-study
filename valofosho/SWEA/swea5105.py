"""
0은 이동 가능
1 은 벽
2 는 출발
3은 도착
"""
from collections import deque

def find_start():
    for i in range(N):
        for j in range(N):
            if maps[i][j] == 2:
                return i, j

def check(i,j,N):
    if 0<=i<N and 0<=j<N:
        return True
    else:
        return False

def bfs(i,j):
    visited = [[0]* N for _ in range(N)]
    visited[i][j] = 1
    q = deque()
    q.append([i,j])
    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]
    flag = False
    while q:
        i,j = q.popleft()
        for d in range(4):
            ni, nj = i+di[d], j+dj[d]
            if check(ni,nj,N) and visited[ni][nj] == 0:
                if maps[ni][nj] == 0:
                    visited[ni][nj] = visited[i][j] + 1
                    q.append([ni,nj])
                elif maps[ni][nj] == 3:
                    visited[ni][nj] = visited[i][j] + 1
                    flag = True
                    return visited[ni][nj] -2 

    if not flag:
        print(visited)
        return 0


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    maps = [list(map(int, input())) for _ in range(N)]
    i, j = find_start()
    ans = bfs(i,j)
    print(f"#{test_case} {ans}")