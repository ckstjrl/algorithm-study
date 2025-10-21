# BOJ 1926. 그림 (D2)

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for x in range(n)]

di = [0,1,0,-1]
dj = [1,0,-1,0]
max_w=0
cnt=0

def dfs(i,j):
    global cnt
    cnt += 1
    w = 0
    stack = [(i,j)]
    while stack:
        i, j = stack.pop()
        w +=1
        for xi, xj in zip(di,dj):
            ni,nj = i + xi, j + xj
            if 0<= ni < n and 0 <= nj < m:
                if arr[ni][nj] == 1:
                    stack.append((ni,nj))
                    arr[ni][nj] = 0
    return w

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            arr[i][j] = 0
            max_w= max(max_w, dfs(i,j))
print(cnt, max_w, sep='\n')