# BOJ 1202. 보석 도둑 (G2 / D3)

from heapq import heappush, heappop

N, K = map(int, input().split())

jewels = []
bags = []

# 보석 정보 리스트 만들기 
for i in range(N):
    m, v = map(int, input().split())
    jewels.append((m, v))

# 가방 리스트 만들기 
for i in range(K):
    bag = int(input())
    bags.append(bag)

# 가방을 공간 작은 순으로 정렬
bags.sort()

# 보석을 무게 순으로 정렬
jewels.sort()  # (무게, 가격) 튜플

heap = []  # 현재 가방에 넣을 수 있는 보석들 (가격 기준 최대 힙)
jewel_idx = 0

ans = 0
for bag in bags:
    # 1. 이 가방에 넣을 수 있는 모든 보석을 힙에 추가
    while jewel_idx < N and jewels[jewel_idx][0] <= bag:
        # 무게가 bag 이하인 보석들
        # 힙에 뭘 넣어야 할까? (가격을 최대 힙으로)
        heappush(heap, -jewels[jewel_idx][1])
        jewel_idx += 1
        
    
    # 2. 힙에서 가장 비싼 보석 하나를 선택
    if heap:
        # 최댓값 꺼내기
        ans += -heappop(heap)
print(ans)