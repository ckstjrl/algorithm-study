# BOJ 1753. 최단경로 (D3 / G4)
import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()

# 1~V번 노드
V, E = map(int, input().split()) 
li = [[] for _ in range(V+1)]
K = int(input())

# 인접리스트
for _ in range(E):
    u, v, w = map(int, input().split())
    li[u].append((v, w))

# 디스탠스 배열 초기화
distance = [float('inf')] * (V+1)
distance[K] = 0

# pq 초기화
heap = [(0, K)]  # 거리, 정점

# 다익 구현
while heap:
    cur_dist, cur_node = heapq.heappop(heap)
    
    if cur_dist > distance[cur_node]:
        continue
    
    for neighbor, weight in li[cur_node]:
        new_dist = cur_dist + weight
        
        if new_dist < distance[neighbor]:
            distance[neighbor] = new_dist
            heapq.heappush(heap, (new_dist, neighbor))
            
for i in range(1, V+1):
    if distance[i] == float('inf'):
        print("INF")
    else:
        print(distance[i])        