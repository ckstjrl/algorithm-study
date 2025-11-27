"""
BOJ1774 - 우주신과의 교감

로직 정의
1. 혼자만 떨어진 애들을 대상
2. 계속해서 Union-Find 로 떨어진 애들 찾기
3. 모든 거리 계산한 뒤 짧은 통로부터 시도
4. Union-Find로 연결

"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
maps = [tuple(map(float, input().split())) for _ in range(N)]
parent = [i for i in range(N)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    # 루트가 다른 애가 나오면 더해버려
    if a != b:
        parent[b] = a

for _ in range(M):
    a, b = map(int, input().split())
    # 선 연결은 1-based 이므로 -1 연산 후 union
    union(a-1, b-1)

edges = []
# a모든 정점에 대해 L2거리 edge에 넣기
for i in range(N):
    for j in range(i+1, N):
        x1, y1 = maps[i]
        x2, y2 = maps[j]
        dist = ((x1-x2)**2 + (y1-y2)**2)**0.5
        edges.append((dist, i, j))
# 크루스칼을 위해 dist 기준 오름차순 정렬
edges.sort()

total = 0
for dist, a, b in edges:
    # a -> b가 이미 연결되어 있지 않다면
    if find(a) != find(b):
        union(a, b)
        # 연결하고, 거리 추가
        total += dist
print(f"{total:.2f}")