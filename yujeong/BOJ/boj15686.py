# 15686. 치킨 배달

import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
house = []          # 집 위치
chicken = []        # 치킨집 위치
min_dist = 13000    # 도시의 치킨 거리 (가능한 큰 값으로 초기화)

# 집, 치킨집 위치들 저장 
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 1:
            house.append((i, j))
        elif row[j] == 2:
            chicken.append((i, j))

# 최대 M개 고르면서 도시의 치킨 거리를 최소화하려면 = 치킨집 M개 있어야 함
# 치킨집들 중 M개 순서없이 고르는 경우를 구해서 그때 치킨 거리들 중 최솟값 구하기
for prob in combinations(range(len(chicken)), M):   # prob: 운영할 치킨집 M개 인덱스들
    curr_dist = 0       # 이번 경우 도시의 치킨 거리
    for h in house:     # 각 집들에 대해 운영중인 치킨집과의 거리 구하기
        h_dist = 100    # 이번 집에서 운영중인 치킨집들과 거리 중 최솟값 = 가장 가까운 치킨집과의 거리
        for x in prob:
            temp_dist = abs(h[0] - chicken[x][0]) + abs(h[1] - chicken[x][1])
            h_dist = min(h_dist, temp_dist)
        curr_dist += h_dist
    min_dist = min(min_dist, curr_dist)     # min_dist 갱신 

## --- 백트래킹으로 접근 (시간 초과) ---
# visited = [False] * len(chicken)

# def backtracking(cnt):
#     global visited, min_dist
#     if cnt > M:
#         return
#     if cnt == M:
#         curr_dist = 0
#         for h in house:
#             h_dist = 100
#             for x in range(len(chicken)):
#                 if visited[x]:
#                     temp_dist = abs(h[0] - chicken[x][0]) + abs(h[1] - chicken[x][1])
#                     h_dist = min(h_dist, temp_dist)
#             curr_dist += h_dist
#             if curr_dist > min_dist:
#                 return 
#         min_dist = min(min_dist, curr_dist)
#         return
#     else:
#         for c in range(len(chicken)):
#             if not visited[c]:
#                 visited[c] = True
#                 backtracking(cnt + 1)
#                 visited[c] = False
#     return

# backtracking(0)

print(min_dist)
