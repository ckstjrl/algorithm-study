import sys
input = sys.stdin.readline
from collections import deque
M, N, K = map(int, input().split())
arr = [[0] * N for _ in range(M)]

def rec(a, b, c, d):  # 직사각형 내부에 포함되는 영역 -> 1
    for i in range(b, d):
        for j in range(a, c):
            arr[i][j] = 1

for _ in range(K):
    a, b, c, d = map(int, input().split())
    rec(a, b, c, d)

def area(si, sj):  # 직사각형으로 분리된 영역 넓이 return
    q = deque()
    q.append((si, sj))
    arr[si][sj] = 1
    a = 1
    while q:
        pi, pj = q.popleft()
        for di,dj in [[-1,0],[1,0],[0,1],[0,-1]]:
            ni = pi + di
            nj = pj + dj
            if 0 <= ni < M and 0 <= nj < N:
                if arr[ni][nj] == 0:
                    a = a + 1
                    arr[ni][nj] = 1
                    q.append((ni, nj))
    return a

ans = []
for i in range(M):  # 영역 전체 순회 -> 직사각형에 포함되지 않은 영역에 대해 넓이 구하고 저장
    for j in range(N):
        if arr[i][j] == 0:
            ans.append(area(i, j))
ans.sort()
print(len(ans))
print(*ans)