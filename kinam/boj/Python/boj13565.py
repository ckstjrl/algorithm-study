'''boj13565 - 침투

인제대학교 생화학연구실에 재직중인 석교수는 전류가 침투(percolate) 할 수 있는 섬유 물질을 개발하고 있다. 
이 섬유 물질은 2차원 M × N 격자로 표현될 수 있다. 
편의상 2차원 격자의 위쪽을 바깥쪽(outer side), 아래쪽을 안쪽(inner side)라고 생각하기로 한다. 
또한 각 격자는 검은색 아니면 흰색인데, 검은색은 전류를 차단하는 물질임을 뜻하고 흰색은 전류가 통할 수 있는 물질임을 뜻한다. 
전류는 섬유 물질의 가장 바깥쪽 흰색 격자들에 공급되고, 이후에는 상하좌우로 인접한 흰색 격자들로 전달될 수 있다.

김 교수가 개발한 섬유 물질을 나타내는 정보가 2차원 격자 형태로 주어질 때, 
바깥쪽에서 흘려 준 전류가 안쪽까지 침투될 수 있는지 아닌지를 판단하는 프로그램을 작성하시오.'''

import sys
sys.setrecursionlimit(100000)

def dfs(si ,sj):
    global ans
    visited[si][sj] = 1

    if ans == 'YES':
        return

    if si == M-1:
        ans = 'YES'
        return
    
    for d in range(4):
        ni, nj = si + di[d], sj + dj[d]
        if 0 <= ni < M and 0 <= nj < N and not visited[ni][nj]:
            if arr[ni][nj] == 0:
                dfs(ni, nj)



M, N = map(int, input().split())
arr = [list(map(int, input())) for _ in range(M)]

visited = [[0] * N for _ in range(M)]
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

ans = 'NO'
    
for i in range(N):
    dfs(0, i)
    if ans == 'YES':
        break

print(ans)
