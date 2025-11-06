"""
문제 정의
1. N명의 학생, M 개의 도로(단방향), T 시간 소요
2. 각각 걸어가서 다시 본인 마을로 돌아와야한다
3. 단방향이라 오고 가는 길이 달라요.
4. 가장 많은 시간을 소요한 학생은 누구!

로직 정의
1. 그동안의 문제들과는 달리 단방향이고 왔다 갔다 왕복을 구해야 하기 때문에 이 부분 처리가 가장 주요
2. 기본적으로 다익스트라를 활용해서 X 마을까지 가는 각각의 최단 경로를 찾고
3. 다시 한 번 역으로 X에서 출발해서 각 마을까지 도달하는 최단 경로를 합해준다.
4. 최종적으로 가장 큰 마을의 인덱스를 출력

"""

import sys
import heapq

input = sys.stdin.readline

# 다익스트라 함수
def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0,start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for next_node, next_cost in adj[now]:
            cost = dist + next_cost
            if distance[next_node] > cost:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))

INF = float('inf')
N, M, X  = map(int, input().split())
adj = [[] for _ in range(N+1)]
# 거리 정보를 담기 위한 하나의 리스트 선언
dist_sum = [0] * (N+1)
for _ in range(M):
    a, b, w = map(int, input().split())
    # 단방향 연결
    adj[a].append((b,w))

distance = [INF] * (N+1)
for i in range(1,N+1):
    # 매 지점마다 새로 돌아야 하기 때문에 초기화
    distance = [INF] * (N+1)
    dijkstra(i)
    # 각 시작점에서 X까지의 최소 비용 담기
    dist_sum[i] += distance[X]
distance = [INF] * (N+1)
# X에서 시작하는 다익스트라 진행
dijkstra(X)
for i in range(1,N+1):
    dist_sum[i] += distance[i]
print(max(dist_sum))