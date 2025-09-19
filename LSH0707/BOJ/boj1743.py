import sys
input = sys.stdin.readline
from collections import deque
N, M, K = map(int, input().split())
arr = [[0] * M for _ in range(N)]
for _ in range(K):
    a, b = map(int, input().split())
    arr[a-1][b-1] = 1
def bfs(si, sj):
    q = deque()
    q.append((si, sj))
    arr[si][sj] = 0  # 방문 처리
    count = 1
    while q:
        i, j = q.popleft()
        for di, dj in [(-1,0),(1,0),(0,1),(0,-1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 1:
                arr[ni][nj] = 0
                q.append((ni, nj))
                count = count + 1
    return count
ans = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:  # 1인지점찾아서
            a = bfs(i, j)  # 함수실행후 리턴값으로 최댓값 기록
            if a > ans:
                ans = a
print(ans)