import heapq

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for next_node, next_cost in adj[now]:
            cost = dist + next_cost
            if distance[next_node] > cost:
                # 거리 갱신 시 부모도 갱신
                parent[next_node] = now
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))

INF = int(1e9)
n, m = map(int, input().split())
distance = [INF] * (n + 1)
parent = [0] * (n + 1)
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))
    adj[b].append((a, c))

dijkstra(1)

print(n - 1)

for i in range(2, n + 1):
    print(i, parent[i])