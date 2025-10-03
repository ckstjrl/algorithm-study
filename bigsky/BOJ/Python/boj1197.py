# BOJ1197 : 최소 스패닝 트리

# Kruskal 알고리즘
import sys
sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip()

v, e = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(e)]
parent = list(range(v + 1))
ans = 0

edges.sort(key = lambda x: x[2])

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x, y = find(x), find(y)

    if x <= y:
        parent[y] = x
    else:
        parent[x] = y

for i in range(e):
    x, y, c = edges[i]
    if find(x) != find(y):
        union(x, y)
        ans += c

print(ans)
# ------------------------------------
# Prim 알고리즘
from heapq import heappush, heappop

V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    x, y, c = map(int, input().split())
    graph[x].append((c, y))
    graph[y].append((c, x))

INF = float('inf')
min_dist = [INF] * (V + 1)
visited = [False] * (V + 1)

pq = [(0, 1)]
min_dist[1] = 0

total = 0

while pq:
    c, x = heappop(pq)
    if visited[x]:
        continue
    visited[x] = True
    total += c

    for c, y in graph[x]:
        if not visited[y] and min_dist[y] > c:
            min_dist[y] = c
            heappush(pq, (c, y))

print(total)