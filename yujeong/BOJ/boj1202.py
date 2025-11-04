# 1202. 보석 도둑
import sys
input = sys.stdin.readline
from heapq import heappop, heappush

N, K = map(int, input().split())    # 보석 개수 N, 가방 개수 K
# 보석 정보
gems = []
for _ in range(N):
    m, v = map(int, input().split())
    gems.append((m, v))

# 가방 정보
bags = []
for _ in range(K):
    c = int(input())
    bags.append(c)

# 그리디한 접근을 위해 보석과 가방 정렬
gems.sort()     # 보석: 무게가 가벼운 순으로 정렬됨
bags.sort()     # 가방: 용량이 작은 순으로 정렬됨

candidates = []     # 가져갈 수 있는 보석들 후보 (우선순위 큐)
total = 0           # 훔치는 보석의 최대 가격
gem_idx = 0         # 보석 탐색을 위한 인덱스 

# 작은 가방부터 보며, 이 가방에 담을 수 있는 보석들을 후보로 저장
# 후보 중 가장 비싼 보석을 가방에 넣기
for size in bags:
    while gem_idx < N and gems[gem_idx][0] <= size:
        weight, price = gems[gem_idx]               # 가방에 담을 수 있는 보석이면 
        heappush(candidates, (-price, weight))      # 담기 (price 큰 순으로 정렬되도록)
        gem_idx += 1    # 다음 가방에서 다시 이 보석을 담지 않도록 범위 조절
    if candidates:                      # 담을 수 있는 보석 있음
        best = heappop(candidates)[0]   
        total += -best                  # 최대 힙 구현을 위해 음수로 저장한 가격 값에 다시 -

print(total)
