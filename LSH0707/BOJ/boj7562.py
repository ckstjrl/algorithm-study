import sys
input = sys.stdin.readline
from collections import deque
T = int(input())
for _ in range(T):
    N = int(input())
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    visited = [[0] * N for _ in range(N)]
    ans = -1
    q = deque()
    q.append((a, b, 0))  # i좌표, j좌표, 이동횟수
    visited[a][b] = 1
    while q:  # bfs
        ci, cj, cnt = q.popleft()
        if ci == c and cj == d:
            ans = cnt
            break
        for di,dj in [[-1,2],[-2,1],[-2,-1],[-1,-2],[1,-2],[2,-1],[2,1],[1,2]]:
            ni = ci + di
            nj = cj + dj
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                q.append((ni, nj, cnt + 1))
    print(ans)