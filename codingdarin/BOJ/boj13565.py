# BOJ 13565. 침투 (D2/S2)

M, N = map(int, input().split())
arr = [list(map(int, input())) for _ in range(M)]
is_passed = False
ans = 'NO'

di = [0,1,0,-1]
dj = [1,0,-1,0]


def dfs(i,j):
    stack = [(i,j)]
    while stack:
        i, j = stack.pop()
        if i == M-1:
            return True
        for xi, xj in zip(di,dj):
            ni, nj = i+xi, j+xj
            if 0 <= ni < M and 0 <= nj < N:
                if arr[ni][nj] == 0:
                    arr[i][j] = 1
                    stack.append((ni,nj))
    return False

    
    
for j in range(N):
    if arr[0][j] == 0:
        arr[0][j] = 1
        if dfs(0,j):
            ans = 'YES'
            break

print(ans)