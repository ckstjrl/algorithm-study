"""
일차원 리스트에서 BFS
걷기 -> X-1 or X+1
순간이동 -> 2*X
"""
from collections import deque
import sys

def check(x):
    if 0<=x<200001:
        return True
    else:
        return False 

def bfs(N,K):
    visited = [0] * (200001)    # visited도 최대만큼 만들기
    q = deque()
    q.append(N)
    visited[N] = 1
    while q:
        cur = q.popleft()
        for i in range(3):  # 3가지 이동 방법 BFS
            if i == 0:
                nx = cur + 1
            elif i== 1:
                nx = cur -1
            else:
                nx = cur*2
            if check(nx):
                if visited[nx] == 0 and nx != K:    # 범위 내에서 K가 아니면
                    visited[nx] = visited[cur] + 1  # visited 처리
                    q.append(nx)    # 큐에 넣어주기
                elif visited[nx] == 0 and nx == K:  # K에 첫 방문
                    visited[nx] = visited[cur] + 1  # visited[K] 방문 처리
                    return visited

input = sys.stdin.readline
N, K = map(int, input().split())
arr = [0] * (200001) # 최대가 100,000 이므로 2*최대값까지 리스트 설정
if N ==K:   # N과 K가 동일하면 0 출력
    print(0)
else:
    visited = bfs(N,K)
    print(visited[K]-1) # visited[N] = 1로 시작하여 1초 빼주기