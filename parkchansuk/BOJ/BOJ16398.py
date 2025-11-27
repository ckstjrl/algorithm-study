# BOJ 16398. 행성 연결 / D3
'''
문제
홍익 제국의 중심은 행성 T이다. 제국의 황제 윤석이는 행성 T에서 제국을 효과적으로 통치하기 위해서, N개의 행성 간에 플로우를 설치하려고 한다.

두 행성 간에 플로우를 설치하면 제국의 함선과 무역선들은 한 행성에서 다른 행성으로 무시할 수 있을 만큼 짧은 시간만에 이동할 수 있다. 하지만, 치안을 유지하기 위해서 플로우 내에 제국군을 주둔시켜야 한다.

모든 행성 간에 플로우를 설치하고 플로우 내에 제국군을 주둔하면, 제국의 제정이 악화되기 때문에 황제 윤석이는 제국의 모든 행성을 연결하면서 플로우 관리 비용을 최소한으로 하려 한다.

N개의 행성은 정수 1,…,N으로 표시하고, 행성 i와 행성 j사이의 플로우 관리비용은 Cij이며, i = j인 경우 항상 0이다.

제국의 참모인 당신은 제국의 황제 윤석이를 도와 제국 내 모든 행성을 연결하고, 그 유지비용을 최소화하자. 이때 플로우의 설치비용은 무시하기로 한다.

입력
입력으로 첫 줄에 행성의 수 N (1 ≤ N ≤ 1000)이 주어진다.

두 번째 줄부터 N+1줄까지 각 행성간의 플로우 관리 비용이 N x N 행렬 (Cij), (1 ≤ i, j ≤ N, 1 ≤ Cij ≤ 100,000,000, Cij = Cji, Cii = 0) 로 주어진다.

출력
모든 행성을 연결했을 때, 최소 플로우의 관리비용을 출력한다.
'''
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

N = int(input().strip())
flow_fee = [list(map(int, input().split())) for _ in range(N)]

# prim
def prim(start_node):
    pq = [(0, start_node)]
    min_weight = 0
    MST = [0] * (N)
    MST[start_node] = 0

    while pq:
        
        weight, node = heappop(pq)
        
        if MST[node] == 1: # 이미 연결된 경우 무시
            continue

        MST[node] = 1
        min_weight += weight

        for nxt_node in range(N):
            if MST[nxt_node] == 1: # 이미 연결된 경우 무시
                continue
            if flow_fee[node][nxt_node] == 0: # 간선이 없는 경우 무시
                continue

            heappush(pq, (flow_fee[node][nxt_node], nxt_node)) # (노드 가중치, 다음 노드)
            
    return min_weight

print(prim(0))

'''
krusal과 prim 고민하다
숫자가 많고, input이 행렬이므로 prim으로 풀이
'''