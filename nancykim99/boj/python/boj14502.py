'''
BOJ14502 : 연구소 (G4)

해결 방법 :
1. 모든 비어있는 공간에서 3개 조합을 다 찾기
2. 조합들을 돌면서, bfs로 바이러스 퍼진 상태 만들고, 안전한 공간 개수 구하기
3. 안전한 개수 중 max를 찾기
'''

from itertools import combinations
from collections import deque

def bfs(safe_lab, virus):
    q = deque()
    for v in virus:
        i, j = v[0], v[1]
        q.append(v)
    while q:
        ti, tj = q.pop()
        for di, dj in ([0,1], [1,0], [0,-1], [-1,0]):
            ni, nj = ti + di, tj + dj
            if 0 <= ni < n and 0 <= nj < m and safe_lab[ni][nj] == 0:
                q.append((ni,nj))
                safe_lab[ni][nj] = 2
    return find_safe(safe_lab)

def find_safe(safe_lab):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if safe_lab[i][j] == 0:
                cnt += 1
    return cnt

n, m = map(int, input().split())
lab = [list(map(int,input().split())) for _ in range(n)]

blanks = []
virus = []

ans = 0
for i in range(n):
    for j in range(m):
        if lab[i][j] == 0:
            blanks.append((i, j))
        if lab[i][j] == 2:
            virus.append((i, j))

temp_walls = list(combinations(blanks, 3))
for walls in temp_walls:
    safe_lab = [row[:] for row in lab]
    for i, j in walls:
        safe_lab[i][j] = 1
    temp = bfs(safe_lab, virus)
    ans = max(ans, temp)

print(ans)