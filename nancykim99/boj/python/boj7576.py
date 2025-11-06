# BOJ7576. 토마토
import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# q에 모든 시작점 (익은 토마토가 있는 칸) 추가하기
q = deque()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            q.append((i, j))

# 그냥 bfs가 아닌 모든 1에서 시작해야하는 bfs이기 때문에 함수 형태가 아닌, 반복문으로 진행
while q:
    ti, tj = q.popleft()
    for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        wi, wj = ti+di, tj+dj
        if 0<=wi<N and 0<=wj<M and arr[wi][wj] == 0:
            arr[wi][wj] = arr[ti][tj] + 1
            q.append((wi, wj))

ans = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            print(-1)
            exit()
        else:
            if ans < arr[i][j]:
                ans = arr[i][j]

print(ans-1) # 시작 토마토가 1이기 때문에, 1 빼기