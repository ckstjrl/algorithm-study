"""
유기농 배추
T: 테스트 케이스
N: 가로 길이 M: 세로 길이 K: 배추 위치 개수
MxN 배열
"""
from collections import deque
def check(i,j):
    if 0 <= i < M and 0 <= j <N:
        return True
    else:
        return False

def bfs(i,j):
    q = deque()
    q.append([i,j])
    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]
    flag = False
    while q:
        i,j = q.popleft()
        # 방문한 적이 없으면 flag
        if visited[i][j] == 0:
            flag = True
        for d in range(4):
            ni, nj = i+di[d], j+dj[d]
            if check(ni,nj) and visited[ni][nj] == 0:
                # 배추가 있으면
                if maps[ni][nj] == 1:
                    q.append([ni,nj])
                    visited[ni][nj] = 1
                    flag = True
                else:
                    visited[ni][nj] = 1
    return flag


T = int(input())
for test_case in range(1, T+1):
    M, N, K = map(int, input().split())
    maps = [[0] * N for _ in range(M)]
    for _ in range(K):
        a, b = map(int, input().split())
        maps[a][b] = 1
    
    cnt = 0
    visited = [[0] * N for _ in range(M)]
    for i in range(M):
        for j in range(N):
            # 배추 위치부터 bfs
            if maps[i][j] == 1:
                if bfs(i,j):
                    cnt += 1
    print(cnt)