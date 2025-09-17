# boj1753(D3): 최단경로
import sys
import heapq

input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
route = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    route[u].append((v, w))

distance = [float('inf')] * (V + 1)
distance[K] = 0
pq = [(0, K)]

while pq:
    dist, node = heapq.heappop(pq)

    if distance[node] < dist:
        continue

    for n, w in route[node]:
        n_dist = dist + w
        if distance[n] > n_dist:
            distance[n] = n_dist
            heapq.heappush(pq, (n_dist, n))

for i in range(1, V + 1):
    if distance[i] == float('inf'):
        print("INF")
    else:
        print(distance[i])


# 시간초과...
# V, E = map(int, input().split())
# K = int(input())
# route = [[] for _ in range(V + 1)]
# for _ in range(E):
#     u, v, w = map(int, input().split())
#     route[u].append((v, w))
# visited = [200000] * (V + 1)
# visited[K] = 0
# q = deque([(K, 0)])
# while q:
#     start, dist = q.popleft()
#     for v, w in route[start]:
#         n_dist = dist + w
#         if visited[v] > n_dist:
#             visited[v] = n_dist
#             q.append((v, n_dist))
#
# for i in range(1, V + 1):
#     if visited[i] == 200000:
#         print("INF")
#     else:
#         print(visited[i])