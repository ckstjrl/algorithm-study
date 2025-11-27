# 1012. 유기농 배추
import sys
from collections import deque
input = sys.stdin.readline

def dfs(x, y):
    q = deque([])
    q.append((x, y))
    while q:
        px, py = q.pop()
        farm[px][py] = 0    # 이미 탐색한 영역은 0으로 만듦 (같은 영역이 여러번 카운트되지 않도록)
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:   # 상하좌우 인접한 곳 탐색
            nx, ny = px+dx, py+dy
            if 0<=nx<N and 0<=ny<M:
                if farm[nx][ny] == 1:       # 배추가 심어진 땅이 인접한 곳에 있으면 스택에 추가
                    q.append((nx, ny))
                

T = int(input())
for tc in range(T):
    M, N, K = map(int, input().split())     # 가로 M, 세로 N, 배추 위치 K개
    farm = [[0] * M for _ in range(N)]      # 전체 땅
    for _ in range(K):
        x, y = map(int, input().split())
        farm[y][x] = 1                      # 배추가 심어진 땅을 1로 

    cnt = 0     # 배추가 모인 영역을 카운트
    for i in range(N):
        for j in range(M):
            if farm[i][j] == 1: # 배추가 심어진 영역이면
                dfs(i, j)       
                cnt += 1        # 영역 개수 +1
    
    print(cnt)