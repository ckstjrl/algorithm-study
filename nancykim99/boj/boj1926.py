'''
BOJ1926 / D2): 그림

해결 방법 : DFS. 2차원 배열.
'''

N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]

def dfs(i, j):
    stack = []
    stack.append((i,j))
    paper[i][j] = 0
    pic_sum = 1
    while stack:
        ti, tj = stack.pop()
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = ti + di, tj + dj
            if 0<=ni<N and 0<=nj<M and paper[ni][nj] == 1:
                paper[ni][nj] = 0
                stack.append((ni, nj))
                pic_sum += 1
    return pic_sum

pics = []
pic_num = 0
for i in range(N):
    for j in range(M):
        if paper[i][j] == 1:
            picture = dfs(i, j)
            pic_num += 1
            pics.append(picture)

print(pic_num)

if pics:
    print(max(pics))
else:
    print(0)

