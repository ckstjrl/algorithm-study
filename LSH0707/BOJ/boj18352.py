import sys
input = sys.stdin.readline
from collections import deque
N, M, K, X = map(int, input().split())
arr = [[] for _ in range(1+N)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
dis = [-1] * (1+N)  # 거리 배열
dis[X] = 0  # 시작점 초기화
q = deque()
q.append(X)
while q:  # BFS
    p = q.popleft()
    for i in arr[p]:
        if dis[i] == -1:  # 방문기록없으면
            dis[i] = dis[p] + 1  # 현재거리 + 1 기록
            q.append(i)  # 큐에 추가
cnt = 0
for i in range(len(dis)):
    if dis[i] == K:
        print(i)
        cnt = cnt + 1
if cnt == 0:  # K인 도시없으면 -1출력
    print(-1)