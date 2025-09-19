"""
BOJ1261-알고스팟
움직일 수 있는 방향은 좌우상하
지나가면서 0이면 지나가고 1이면 벽뚫기
그러니까 가는데 간선의 비용이 1인거임
"""
# 1번 BFS 활용 버전 - 136ms
import sys
input = sys.stdin.readline
def check(i,j):
    if 0<=i<N and 0<=j<M:
        return True
    else:
        return False


def bfs(si,sj):
    q = deque([])
    q.append((si,sj))
    visited[si][sj] = 0
    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]
    while q:
        i, j = q.popleft()
        for d in range(4):
            ni, nj = i+di[d], j+dj[d]
            # i,j -> 출발위치
            # ni, nj -> 도착 위치
            # if 도착위치 > 길찾기
            if check(ni,nj):
                temp = visited[i][j] + maps[ni][nj]
                if temp < visited[ni][nj]:
                    visited[ni][nj] = temp
                    q.append((ni,nj))
    return visited[N-1][M-1]

from collections import deque
M, N = map(int, input().split())
maps = [list(map(int, input().rstrip())) for _ in range(N)]
INF = float('inf')
visited = [[INF] * M for _ in range(N)]
ans = bfs(0,0)
print(ans)


# 2번 다익스트라 활용 버전 - 188ms
import heapq
import sys

input = sys.stdin.readline

def check(i,j):
    if 0<=i<N and 0<=j<M:
        return True
    else:
        return False

def dijkstra(si, sj):
    pq = [(0,(si,sj))]
    INF = float('inf')
    visited = [[INF] * M for _ in range(N)]
    visited[si][sj] = 0

    while pq:
        cnt, (i, j) = heapq.heappop(pq)
        if i == N-1 and j == M-1:
            return cnt       
        for d in range(4):
            ni, nj = i+di[d], j+dj[d]
            if check(ni,nj):
                temp = cnt + maps[ni][nj]
                # 벽 부수는 횟수가 최소인 경우로 갱신
                if visited[ni][nj] > temp:
                    visited[ni][nj] = temp
                    heapq.heappush(pq, (visited[ni][nj], (ni, nj)))


M, N = map(int, input().split())
maps = [list(map(int,input().strip())) for _ in range(N)]
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
ans = dijkstra(0, 0)
print(ans)
