# 1697. 숨바꼭질 

from collections import deque

def bfs(N, K):
    q = deque()
    q.append(N)
    while q:
        x = q.popleft()
        if x == K:          # K에 도달
            print(road[x])  # 이때까지 걸린 시간 출력
            break
        for dx in [x-1, x+1, x*2]:  # x에서 다음으로 움직일 수 있는 경우의 수
            if 0<=dx<=100000 and not road[dx]:   # 방문한 적 없는 거리(지점)이면 이동             
                road[dx] = road[x] + 1  # 시간(초) +1
                q.append(dx)

N, K = map(int, input().split())
road = [0] * (100001)       # N, K 범위는 0 이상 100000 이하
bfs(N, K)
