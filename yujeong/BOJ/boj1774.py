# 1774. 우주신과의 교감

from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())    # 우주신 개수 N, 이미 연결된 통로 개수 M
coords = [list(map(int, input().split())) for _ in range(N)]    # 우주신 좌표들
connected = [list(map(int, input().split())) for _ in range(M)] # 이미 연결된 우주신들 번호 쌍 

# 서로 다른 두 우주신들 a, b 잇는 간선 정보 (직선거리, a, b)
edges = []
for a, b in combinations(range(N), 2):  # 1~N까지의 수 중 2개 조합
    ax, ay = coords[a][0], coords[a][1] # a의 좌표 (ax, ay)
    bx, by = coords[b][0], coords[b][1] # b의 좌표 (bx, by)
    dist = ((ax - bx)**2 + (ay - by)**2)**0.5   # 두 좌표 간 거리 
    edges.append((dist, a+1, b+1))
edges.sort()    # 거리 기준 전체 간선 정보 정렬

parents = [i for i in range(N+1)]   # union find 적용하기 위한 대표자 정보 배열

# 각 번호별 대표자 찾기 
def find_set(x):
    if x == parents[x]:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]

# 두 번호 합치기 (연결하기)
def union(x, y):
    rx = find_set(x)
    ry = find_set(y)
    if rx == ry:
        return
    if rx < ry:
        parents[ry] = rx
    else:
        parents[rx] = ry

# 원래 연결되어 있는 우주신들 union()으로 연결되었다고 나타내기
for a, b in connected:
    union(a, b)

mst_w = 0   # 비용 (거리)
for w, u, v in edges:   # 거리가 작은 순으로 선택한 두 번호 u, v에 대해
    if find_set(u) != find_set(v):  # 같은 집합에 속하지 않는(연결되지 않은) 쌍이면
        union(u, v)                 # 연결하고
        mst_w += w                  # 거리 추가 

print(f'{mst_w:.2f}')   # 형식에 맞게 출력