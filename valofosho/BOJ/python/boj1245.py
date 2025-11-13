"""
BOJ1245 - 농장 관리

문제 정의
1. N x M 격자로 이루어진 농장
2. 산봉우리마다 경비원을 배치하려는데 산봉우리가 총 몇개인지 세야한다.
3. 같은 높이를 가지는 하나의 격자 혹은 인접한 격자들의 집합
4. 산봉우리와 인접한 격자는 모두 산봉우리의 높이보다 작아야한다.
5. 인접하다의 정의는 X좌표 Y좌표 차가 모두 1이하인 경우 -> 대각도 된다는 뜻ㄱ이네요
6. 격자 내에 총 몇개의 산봉우리가 있는지 구하라


로직 정의
1. 아무래도 돌아야 겠지..?
2. 지점마다 시작점을 주고, visited 배열 활용해서 인접한 배열들 -> 찾다가 같거나 작으면 ok
-> 같으면 q에 넣고, 작으면 continue, 크면 flag 만약 flag 안걸리면 걔가 봉우리
다시 빈 값들부터 시작

"""
from collections import deque
import sys
input = sys.stdin.readline


def bfs(i,j):
    q = deque([])
    q.append((i,j))
    visited[i][j] = 1
    flag = False
    while q:
        i, j = q.popleft()
        cur = maps[i][j]
        for d in range(8):
            ni, nj = i+di[d], j+dj[d]
            # 범위 체크
            if not(0<=ni<N and 0<=nj<M):
                continue
            # 다른 봉우리보다 낮으면 flag
            if cur < maps[ni][nj]:
                flag = True
            # 같은 높이에 방문안한 인접점 추가
            if cur == maps[ni][nj] and not visited[ni][nj]:
                visited[ni][nj] = 1
                q.append((ni,nj))
    # 하나라도 높은게 있으면 0 아니면 1
    return 1 if not flag else 0


        
N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
di = [1,1, 1, 0, 0, -1,-1,-1]
dj = [0,1,-1, 1, -1, 0, 1, -1]
ans = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            temp  = bfs(i,j)
            if temp:
                ans += 1
            else:
                continue
print(ans)