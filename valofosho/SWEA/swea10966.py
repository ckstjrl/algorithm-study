"""
물이면 W, 땅이면 L

"""
from collections import deque
def check(i, j, N, M):
    if 0<=i<N and 0<=j<M:
        return True
    else:
        return False

def find_lakes():
    lakes = []
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 'W':
                lakes.append([i,j])
    return lakes

def bfs(lakes):
    visited = [[0] * M for _ in range(N)]
    q = deque(lakes)
    
    di = [-1, 1, 0, 0]
    dj = [0, 0, 1, -1]
    while q:
        i, j = q.popleft()
        for d in range(4):
            ni, nj = i+di[d], j+dj[d]
            if check(ni, nj, N, M):
                # 땅이면
                if maps[ni][nj] == 'L' and visited[ni][nj] == 0 :
                    visited[ni][nj] = visited[i][j] + 1
                    q.append([ni,nj])
                
    return visited

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    maps = [input() for _ in range(N)]
    lakes = find_lakes()
    visited = bfs(lakes)
    cnt = 0
    for row in  visited:
        cnt += sum(row)
    print(f"#{test_case} {cnt}")
