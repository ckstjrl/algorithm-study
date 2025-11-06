'''
BOJ13565 / D2): 침투

해결 방법 : DFS. 2차원 배열.
'''

M, N = map(int, input().split())
cloth = [list(map(int, list(input().strip()))) for _ in range(M)]

def dfs(i, j):
    global arrived_end
    stack = []
    stack.append((i, j))
    while stack:
        ti, tj = stack.pop()
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = ti + di, tj + dj
            if 0<=ni<M and 0<=nj<N and cloth[ni][nj] == 0:
                stack.append((ni, nj))
                cloth[ni][nj] = 1
            if ni == M-1:
                arrived_end += 1

arrived_end = 0
i = 0
for j in range(N):
    if cloth[i][j] == 0:
        dfs(i, j)

if arrived_end > 0:
    print('YES')
else:
    print('NO')