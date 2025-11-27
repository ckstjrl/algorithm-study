# SWEA5249: 최소 신장 트리

# Kruskal 알고리즘 : 
# 모든 간선을 가중치가 가장 작은 것부터 차례대로 선택하면서, 
# 사이클이 생성되지 않도록 간선을 하나식 추가하는 방식
def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    px, py = find(x), find(y)
    if px <= py:
        parent[py] = px
    else:
        parent[px] = py


t = int(input())
for tc in range(1, t+1):
    v, e = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(e)]
    parent = list(range(v + 1))

    edges.sort(key = lambda x: x[2])

    ans = 0
    for x, y, c in edges:
        if find(x) != find(y):
            union(x, y)
            ans += c

    print(f'#{tc} {ans}')


# ---------------------------------------------------------------
# Prim 알고리즘 :
# 임의의 시작 정점에서 시작하여, 현재 MST 집합에 연결되지 않은 정점 중
# 가장 낮은 가중치를 가진 간선을 선택하여 MST를 구축하는 방법
from heapq import heappush, heappop

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        x, y, c = map(int, input().split())
        graph[x].append((y, c))
        graph[y].append((x, c))
    
    INF = float('inf')
    min_dist = [INF] * (V + 1)
    visited = [False] * (V + 1)
    
    min_dist[0] = 0
    pq = [(0, 0)]

    total = 0

    while pq:
        c, x = heappop(pq)

        if visited[x]:
            continue
        visited[x] = True
        total += c

        for y, c in graph[x]:
            if not visited[y] and c < min_dist[y]:
                min_dist[y] = c
                heappush(pq, (c, y))
    
    print(f'#{tc} {total}')