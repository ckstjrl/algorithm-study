# BOJ1202(D3): 보석 도둑
from heapq import heappush, heappop
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

gems = []
for _ in range(N):
    m, v = map(int, input().split())
    gems.append((m, v))

bags = []
for _ in range(K):
    bags.append(int(input()))

gems.sort()
bags.sort()

total = 0
possible_gems_value = []
gem_idx = 0

for bag in bags:
    while gem_idx < N and gems[gem_idx][0] <= bag:
        heappush(possible_gems_value, -gems[gem_idx][1])
        gem_idx += 1
    
    if possible_gems_value:
        max_value = heappop(possible_gems_value)
        total -= max_value

print(total)

# 시간초과...
# N, K = map(int, input().split())

# gems = []
# for _ in range(N):
#     m, v = map(int, input().split())
#     heappush(gems, (-v, m))

# bags = []
# for _ in range(K):
#     bags.append(int(input()))
# bags.sort()

# total = 0
# bag_used = [False] * (K + 1)
# while bags and gems:
#     cv, cm = heappop(gems)
#     for i in range(len(bags)):
#         if not bag_used[i] and bags[i] >= cm:
#             total -= cv
#             bag_used[i] = True
#             break

# print(total)
