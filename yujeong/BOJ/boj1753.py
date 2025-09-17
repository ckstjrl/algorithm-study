# 1753. 최단경로

import sys, heapq
input = sys.stdin.readline

# 그래프를 다익스트라 알고리즘으로 탐색하며 노드별로 도달하기 위한 최단경로를 저장할 함수 search()
def search(s):
    q = [(0, s)]    # (누적 거리, 노드)
    while q:
        # q.sort(key=lambda x: x[1], reverse=True)
        # nxt, dist = q.pop()
        dist, nxt = heapq.heappop(q)
        if dist > visited[nxt]:     # 지금 누적거리보다 더 짧은 거리로 노드 도달 가능한경우 continue
            continue
        for n, d in edges[nxt]:
            if visited[n] > visited[nxt] + d:   # 기존 누적거리로 저장한 값보다 더 짧게 도달 가능한경우
                visited[n] = visited[nxt] + d   # 최단거리 갱신
                # q.append((n, visited[n]))
                heapq.heappush(q, (visited[n], n))  # 힙에 push


V, E = map(int, input().split())    # 정점 V개, 간선 E개
K = int(input())                    # 시작 정점

edges = [[] for _ in range(V+1)]        # 간선 정보를 저장할 인접 리스트 
for _ in range(E):
    u, v, w = map(int, input().split())
    edges[u].append((v, w))

visited = [1e9] * (V+1)     # 임의의 큰 값으로 visited 초기화
visited[K] = 0              # 시작 노드의 누적거리값은 0
search(K)                   # 탐색 시작 

for i in range(1, V+1):
    if visited[i] != 1e9:   # 경로가 존재하는 경우 (초기값이 아닌 값으로 갱신된 경우)
        print(visited[i])   # 그 값 출력
    else:                   # 아닌 경우
        print('INF')        # 'INF' 출력