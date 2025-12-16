# BOJ 1753. 최단경로 / D3
'''
방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성하시오.
단, 모든 간선의 가중치는 10 이하의 자연수이다.

입력
첫째 줄에 정점의 개수 V와 간선의 개수 E가 주어진다. (1 ≤ V ≤ 20,000, 1 ≤ E ≤ 300,000)
모든 정점에는 1부터 V까지 번호가 매겨져 있다고 가정한다.
둘째 줄에는 시작 정점의 번호 K(1 ≤ K ≤ V)가 주어진다.
셋째 줄부터 E개의 줄에 걸쳐 각 간선을 나타내는 세 개의 정수 (u, v, w)가 순서대로 주어진다.
이는 u에서 v로 가는 가중치 w인 간선이 존재한다는 뜻이다.
u와 v는 서로 다르며 w는 10 이하의 자연수이다.
서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음에 유의한다.

출력
첫째 줄부터 V개의 줄에 걸쳐, i번째 줄에 i번 정점으로의 최단 경로의 경로값을 출력한다. 시작점 자신은 0으로 출력하고, 경로가 존재하지 않는 경우에는 INF를 출력하면 된다.
'''

import sys
import heapq
V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())

# 시작점 K까지의 거리는 0, 나머지는 무한대로 시작.
# pq는 (현재까지 알려진 최단거리, 정점) 튜플의 최소 힙.
INF = 1e9
arr = [[] for _ in range(V+1)]
dist = [INF] * (V+1)

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    arr[u].append((v,w))

dist[K] = 0
pq = [(0, K)]

# 힙에서 뽑힌 (ds, b)는 지금 알고 있는 b까지의 최단 거리 후보 중 최소.
# 같은 정점 b에 대해 더 짧은 거리가 나중에 갱신되어 새 튜플이 큐에 들어간 뒤,
# 이전의 긴 값 pop
# if ds != dist[b]: continue 이 한 줄 덕분에 visited 배열이 필요 없음
# 인접 정점 v에 대해 nxt = ds + w가 더 짧으면 거리 갱신하고, (nxt, v)를 큐에 푸시.
while pq:
    ds, b = heapq.heappop(pq)
    if ds != dist[b]:
        continue
    for v, w in arr[b]:
        nxt = ds + w
        if nxt < dist[v]:
            dist[v] = nxt
            heapq.heappush(pq, (nxt, v))

for a in range(1, V+1):
    if dist[a] == 1e9:
        print('INF')
    else:
        print(dist[a])

# 힙 사용안하고 다익스트라 구현 코드 (시간 초과 발생)
# visited = [0] * (V+1)
# def near_node():
#     min_val = INF
#     idx = 0
#     for i in range(1, V+1):
#         if dist[i] < min_val and visited[i] == 0:
#             min_val = dist[i]
#             idx = i
#     return idx
#
# def dijstra(s):
#     dist[s] = 0
#     visited[s] = 1
#     for i in arr[s]:
#         dist[i[0]] = i[1]
#     for _ in range(V-1):
#         n = near_node()
#         if n == 0:
#             break
#         visited[n] = 1
#         for j in arr[n]:
#             if dist[n] + j[1] < dist[j[0]]:
#                 dist[j[0]] = dist[n] + j[1]

# dijstra(K)
# for a in range(1, V+1):
#     if dist[a] == 1e9:
#         print('INF')
#     else:
#         print(dist[a])

'''
디엑스트 사용
그냥 구현하는경우에는 시간초과 발생
힙 사용하여 구현하는 방식으로 해야지 시간 단축 가능
그냥 구현하는 경우에는 완전탐색과 비슷해서 시간 복잡도 상대적으로 큼
'''