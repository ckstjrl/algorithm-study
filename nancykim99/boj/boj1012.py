# BOJ1012. 유기농 배추

from collections import deque

def bfs(i, j):
    q = deque()
    q.append((i, j))
    arr[i][j] = 0
    while q:
        ti, tj = q.popleft()
        arr[ti][tj] = 0
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1,0]]:
            wi, wj = ti+di , tj+dj
            if 0<=wi<M and 0<=wj<N and arr[wi][wj] == 1:
                arr[wi][wj] = 0
                q.append((wi, wj))


T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    arr = [[0] * N for _ in range(M)]

    for _ in range(K):
        i, j = map(int, input().split())
        arr[i][j] = 1

    cnt = 0
    for i in range(M):
        for j in range(N):
            if arr[i][j] == 1:
                cnt += 1
                bfs(i, j)

    print(cnt)