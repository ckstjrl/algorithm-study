# BOJ7569. 토마토
import sys
from collections import deque

M, N, H = map(int, sys.stdin.readline().split())
arr = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]

# q에 모든 시작점 (익은 토마토가 있는 칸) 추가하기
q = deque()
for k in range(H):
    for i in range(N):
        for j in range(M):
            if arr[k][i][j] == 1:
                q.append((k, i, j))

# 그냥 bfs가 아닌 모든 1에서 시작해야하는 bfs이기 때문에 함수 형태가 아닌, 반복문으로 진행
while q:
    tk, ti, tj  = q.popleft()
    for dk, di, dj in [[0, 0, 1], [0, 0, -1], [0, 1, 0], [1, 0, 0], [0, -1, 0], [-1, 0, 0]]:
        wk, wi, wj = tk+dk, ti+di, tj+dj
        if 0<=wk<H and 0<=wi<N and 0<=wj<M and arr[wk][wi][wj] == 0:
            arr[wk][wi][wj] = arr[tk][ti][tj] + 1
            q.append((wk, wi, wj))

ans = 0
for k in range(H):
    for i in range(N):
        for j in range(M):
            if arr[k][i][j] == 0:
                print(-1)
                exit()
            else:
                if ans < arr[k][i][j]:
                    ans = arr[k][i][j]

print(ans-1) # 시작 토마토가 1이기 때문에, 1 빼기