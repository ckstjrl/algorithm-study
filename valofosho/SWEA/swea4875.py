def check(i,j,N):
    if 0<=i<N and 0<=j<N:
        return True
    else:
        return False

def  dfs(i, j):
    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]
    visited[i][j] = 1
    for d in range(4):
        ni, nj = i+di[d], j+dj[d]
        if check(ni,nj,N):
            if maps[ni][nj] == 0 and visited[ni][nj] == 0:
                dfs(ni,nj)
            elif maps[ni][nj] == 0 and visited[ni][nj] == 1:
                continue
            elif maps[ni][nj] == 3:
                global ans
                ans = 1
                return
            



T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    maps = [list(map(int, input())) for _ in range(N)]
    S = 2
    G = 3
    visited = [[0]*N for _ in range(N)]
    flag = False
    for i in range(N):
        for j in range(N):
            if maps[i][j] == 2:
                flag = True
                break
        if flag:
            break
    ans = 0
    dfs(i, j)
    print(f"#{test_case} {ans}")