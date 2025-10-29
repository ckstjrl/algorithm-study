'''boj1854 - K번째 최단경로 찾기
봄캠프를 마친 김진영 조교는 여러 도시를 돌며 여행을 다닐 계획이다. 그런데 김 조교는, '느림의 미학'을 중요시하는 사람이라 항상 최단경로로만 이동하는 것은 별로 좋아하지 않는다. 하지만 너무 시간이 오래 걸리는 경로도 그리 매력적인 것만은 아니어서, 적당한 타협안인 '
$k$번째 최단경로'를 구하길 원한다. 그를 돕기 위한 프로그램을 작성해 보자.
'''

# 최단경로 -> 다익스트라
# K번쨰? .... 다익스트라 변형해보기
# 다익스트라 K번 돌리기? -> 뭔가 말이 안되는듯
# dist배열에 다 때려넣고 정렬하고 K번째 꺼내기?...구현은 쉬운데 복잡도 클듯
# dist[i]에 heap으로 넣어두고 k번째를 꺼내기? -> 해볼만할듯
# heap을 사용해도 다 때려넣고 k번 heappop수행?
# 최소힙 사용할지 최대힙 사용할지
# 최대힙 사용하면? 굳이?
# 그냥 dist[i]의 크기(len)을 K로 해두고 최대힙으로 heappop하면 바로 정답나옴

from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
adj_list = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    adj_list[u].append((v, w))

def dijkstra():
    dist = [[] for _ in range(n + 1)]
    pq = [(0, 1)] #시작노드, 비용0, 1번 노드
    heappush(dist[1], 0)

    while pq:
        cost, u = heappop(pq)

        for v, w in adj_list[u]:
            new_cost = cost + w

            if len(dist[v]) < k:
                heappush(dist[v], -new_cost)
                heappush(pq, (new_cost, v))

            elif new_cost < -dist[v][0]: #가장 큰 값 제거하기
                heappop(dist[v])
                heappush(dist[v], -new_cost)
                heappush(pq, (new_cost, v))

    # print(dist)
    for i in range(1, n + 1):
        if len(dist[i]) == k:
            cost = heappop(dist[i])
            print(-cost)
        else:
            print(-1)

dijkstra()