# BOJ1238(D3): 파티
from heapq import heappush, heappop
import sys
input = sys.stdin.readline

def dijkstra(start, graph):
    dist = [float('inf')] * (N + 1)
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, u = heappop(pq)
        if dist[u] < d:
            continue
        for v, w in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heappush(pq, (nd, v))
    return dist


N, M, X = map(int, input().split())  # N: 학생/마을 수, M: 도로 수, X: 파티 마을
g = [[] for _ in range(N + 1)]   # 정방향 간선
rg = [[] for _ in range(N + 1)]  # 역방향 간선
for _ in range(M):
    a, b, t = map(int, input().split())
    g[a].append((b, t))
    rg[b].append((a, t))

to_home = dijkstra(X, g)
to_party = dijkstra(X, rg)

ans = 0
for i in range(1, N + 1):
    total = to_home[i] + to_party[i]
    ans = max(ans, total)

print(ans)