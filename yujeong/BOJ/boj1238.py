# 1238. 파티

import sys
input = sys.stdin.readline
from heapq import heappop, heappush
INF = float('inf')

# graph의 간선 정보들을 기준으로 pos에서부터 다익스트라 탐색하기 
def dijkstra(pos, graph):
    pq = [(0, pos)]
    dist = [INF] * (N+1)    # 탐색 결과 각 마을에 도달하는 데 걸리는 시간 기록
    dist[pos] = 0

    while pq:
        cost, node = heappop(pq)
        if cost > graph[node]:      # 기존 시간보다 크면 continue
            continue
        for nxt, w in roads[node]:  # 간선 정보 -- (목적지 마을, 시간)
            new_cost = w + cost     # 새 시간
            if new_cost < dist[nxt]:    # 새 시간이 기존 시간보다 작은 경우에만
                dist[nxt] = new_cost    # 정보 갱신
                heappush(pq, (new_cost, nxt))

    return dist     # 탐색 마친 dist 배열 리턴 


N, M, X = map(int, input().split())
roads = [[] for _ in range(N+1)]        # 원래 방향대로 가는 루트 정보 저장
back_roads = [[] for _ in range(N+1)]   # 반대 방향으로 저장 (a<->b 바꿔서)

# 도로 정보 담기 
for _ in range(M):              
    a, b, t = map(int, input().split())     # 도로 시작, 끝, 시간
    roads[a].append((b, t))         # 시작 -> 끝 방향으로 정보 저장
    back_roads[b].append((a, t))    # 끝 -> 시작 방향으로 정보 저장

# X->N, N->X 방향으로 다익스트라 탐색
xton = dijkstra(X, roads)
ntox = dijkstra(X, back_roads)

ans = 0
for i in range(1, N+1):
    # nth_time = dijkstra(i)[X]
    # ans = max(ans, xton[i] + nth_time)
    ans = max(ans, xton[i] + ntox[i])   # 왕복 시간 중 가장 오래 걸리는 시간 찾기

print(ans)
