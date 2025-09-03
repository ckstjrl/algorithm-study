"""
고저차가 발생하면 그 만큼 +
시작과 도착은 각각 좌상귀, 우하귀 끝점
높이는 한 번만이 아닌 계속 변동

bfs로 진행
"""

from collections import deque

def check(i,j,N):
    if 0<=i<N and 0<=j<N:
        return True
    else:
        return False

def bfs(N):
    visited = [[100000] * N for _ in range(N)]
    visited[0][0] = 0   # 시작점 방문 표시
    q = deque()
    q.append([0,0])
    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]
    while q:
        i,j = q.popleft()
        for d in range(4):
            ni, nj = i+di[d], j+dj[d]
            if check(ni,nj, N):
                    if maps[ni][nj] > maps[i][j]:
                        nx_temp = visited[i][j] + maps[ni][nj] - maps[i][j] + 1
                    else:
                        nx_temp = visited[i][j] + 1
                    if nx_temp <= visited[ni][nj]:
                        visited[ni][nj] = nx_temp
                        q.append([ni,nj])
    return visited

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    maps = [list(map(int, input().split())) for _ in range(N)]
    si,sj,gi,gj = 0,0,N,N
    visited = bfs(N)
    print(f"#{test_case} {visited[N-1][N-1]}")