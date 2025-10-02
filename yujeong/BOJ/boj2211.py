# 2211. 네트워크 복구
import sys
input = sys.stdin.readline
from heapq import heappop, heappush
INF = float('inf')  # 다익스트라로 최소비용 구할 때 초깃값으로 담을 임의의 큰 값 

# 다익스트라 알고리즘으로 각 컴퓨터까지 최소비용 거리 계산해 반환할 함수 dijkstra()
def dijkstra(pos):
    pq = [(0, pos)]     # (걸리는 시간, 컴퓨터 번호)
    node_info = [[INF, 0] for _ in range(N+1)]  # 각 노드별로 (걸리는 시간, 이어지는 노드) 정보 저장
    node_info[1][0] = 0

    while pq:
        cost, curr = heappop(pq)
        if cost > node_info[curr][0]:
            continue
        for nxt, w in network[curr]:
            new_cost = w + cost
            if new_cost < node_info[nxt][0]:    # 새 비용이 더 작은 경우
                node_info[nxt][0] = new_cost    # 비용 갱신
                node_info[nxt][1] = curr        # 연결된 노드 갱신
                heappush(pq, (new_cost, nxt))
    return node_info


N, M = map(int, input().split())    # N개의 컴퓨터, M개 회선

network = [[] for _ in range(N+1)]      # 양방향 그래프로 간선과 가중치(통신에 걸리는 시간) 정보 담기
for _ in range(M):
    a, b, c = map(int, input().split())
    network[a].append((b, c))
    network[b].append((a, c))

# 1번 컴퓨터가 보안 시스템이 설치된 슈퍼컴퓨터이므로, 
# 1번에서부터 각 컴퓨터들에 연결되기 위해 필요한 최소 시간과 이어져야 할 노드를 찾기
ans = dijkstra(1)

print(N-1)      # 최소 개수 간선으로 모든 노드에 연결할 때 간선 횟수는 N-1
for x in range(2, N+1): 
    print(x, ans[x][1])     # 최소 비용으로 각 노드에 연결된 노드 정보 출력