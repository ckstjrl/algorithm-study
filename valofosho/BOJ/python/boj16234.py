"""
BOJ16234 - 인구 이동
문제 정의
1. NxN 크기의 땅에 N**2 개의 국가가 존재한다
2. 인접한 국가 사이에는 국경이 존재한다.
3. 두 나라의 인구 차이가 L이상 R 이하라면, 두 나라가 국경선을 연다.
4. 국경선을 연 나라는 인구이동을 시작해 (연합의 인구수) / (연합을 이루고 있는 국가수) (소수점은 버림)가 된다.
5. 각 나라의 인구수가 주어졌을 때 며칠동안 인구 이동이 발생하는지 구하라


로직 정의
1. 각 지점마다 돌아야 하는데 2개 이상의 집합이 나오는 경우 역시 존재한다.
    -> 한 턴에 여러 개의 집합이 나올 수 있고, 이를 한 번에 처리해줘야 한다.
    -> 조금 무식한 방법으로 전체 순회(visited + 시작점 제공)
"""

import sys
from collections import deque
input = sys.stdin.readline

def bfs(i,j):
    q = deque([(i,j)])
    corp = maps[i][j]
    bros = [(i,j)]
    cnt = 1
    visited[i][j] = 1
    while q:
        i,j = q.popleft()
        cur = maps[i][j]
        for d in range(4):
            ni, nj = i+di[d], j+dj[d]
            # 범위 나감
            if not(0<=ni<N and 0<=nj<N):
                continue
            if visited[ni][nj]:
                continue
            # 차이가 범위 내라면
            nx = maps[ni][nj]
            # 차이는 절대값으로
            diff = abs(cur-nx)
            if not(L<= diff <= R):
                continue
            q.append((ni,nj))
            visited[ni][nj] = 1
            corp += nx
            bros.append((ni,nj))
            cnt += 1
    else:
        # 연합 내 국가 수, 변경할 평균 값, 위치좌표들
        return cnt, corp//cnt, bros

N, L, R = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
while_cnt = 0
flag = True

while flag:
    # 매일 visited 배열을 초기화 해줘야 한다.
    visited = [[0]*N for _ in range(N)]
    flag = False
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                # 순회
                cnt, new, bros = bfs(i,j)
                if cnt == 1:
                    continue
                else:
                    # 연결된 연합의 값들 일괄 변경
                    for bi, bj in bros:
                        visited[bi][bj] = 1
                        maps[bi][bj] = new     
                    # cnt가 2개 이상이기에 한 번 더 진행
                    flag = True
            else:
                continue
    # 변화가 일어나야 하나의 일수로 측정
    if flag:
        while_cnt += 1
print(while_cnt)