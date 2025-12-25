"""
BOJ11404 - 플로이드

문제 정의
1. N개의 도시 -> M 개의 버스(단방향, cost 다름)
2. 모든 도시의 쌍에 대해 도시 A-> B로 가는데 필요한 비용의 최솟값을 구하라

로직 정의
1. 단방향 코스트가 있는 최단거리 문제 > 플로이드 워셜 알고리즘
2. 플로이드 워셜은 거쳐가는 정점을 중심으로 진행

"""

import sys
input = sys.stdin.readline

N = int(input().strip())
M = int(input().strip())

INF = float('inf')
# maps 배열 초기화
maps = [[INF] * (N) for _ in range(N)]

# 배열에 i to j 값 넣어주기
for _ in range(M):
    i, j, cost = map(int, input().split())
    # 값 중에 동일 경로 다른 비용이 들어옴
    maps[i-1][j-1] = min(cost, maps[i-1][j-1])

# 본인 to 본인 은 0으로!
for i in range(N):
    maps[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            # 각 정점에 대해서 다른 한 지점을 돌아서 가는 값이 더 싸면 갱신
            if maps[i][j] > maps[i][k] + maps[k][j]:
                maps[i][j] = maps[i][k] + maps[k][j]
# 모든 정점을 다 돌아가는 것이 아니므로 0으로 INF 초기화
for i in range(N):
    for j in range(N):
        if maps[i][j] == INF:
            maps[i][j] = 0
for row in maps:
    print(*row)