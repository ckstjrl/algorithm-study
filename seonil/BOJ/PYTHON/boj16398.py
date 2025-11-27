"""
BOJ16398. 행성 연결

[문제]
홍익 제국의 중심은 행성 T이다. 제국의 황제 윤석이는 행성 T에서 제국을 효과적으로 통치하기 위해서, N개의 행성 간에 플로우를 설치하려고 한다.
두 행성 간에 플로우를 설치하면 제국의 함선과 무역선들은 한 행성에서 다른 행성으로 무시할 수 있을 만큼 짧은 시간만에 이동할 수 있다. 하지만, 치안을 유지하기 위해서 플로우 내에 제국군을 주둔시켜야 한다.
모든 행성 간에 플로우를 설치하고 플로우 내에 제국군을 주둔하면, 제국의 제정이 악화되기 때문에 황제 윤석이는 제국의 모든 행성을 연결하면서 플로우 관리 비용을 최소한으로 하려 한다.
N개의 행성은 정수 1,…,N으로 표시하고, 행성 i와 행성 j사이의 플로우 관리비용은 Cij이며, i = j인 경우 항상 0이다.
제국의 참모인 당신은 제국의 황제 윤석이를 도와 제국 내 모든 행성을 연결하고, 그 유지비용을 최소화하자. 이때 플로우의 설치비용은 무시하기로 한다.

[입력]
입력으로 첫 줄에 행성의 수 N (1 ≤ N ≤ 1000)이 주어진다.
두 번째 줄부터 N+1줄까지 각 행성간의 플로우 관리 비용이 N x N 행렬 (Cij), (1 ≤ i, j ≤ N, 1 ≤ Cij ≤ 100,000,000, Cij = Cji, Cii = 0) 로 주어진다.

[출력]
모든 행성을 연결했을 때, 최소 플로우의 관리비용을 출력한다.
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

# 노드 x의 대표를 찾는 함수(Union-Find 함수)
def find_set(x):
    if x == parents[x]:
        return x
    parents[x] = find_set(parents[x])   # 경로 압축
    return parents[x]

# 두 노드가 속한 집합을 합치는 함수(Union-Find 함수)
def union(x, y):
    rx = find_set(x)
    ry = find_set(y)

    if rx == ry:
        return
    elif rx < ry:
        parents[ry] = rx
    else:
        parents[rx] = ry

# 간선 정보를 이용해 최소 신장 트리(MST)를 구성하고 가중치 합을 반환하는 함수
def sum_weight_of_MST(edges):
    cnt, sum_weight = 0, 0

    # kruskal 알고리즘으로 MST 찾기
    # 1) 모든 간선을 가중치에 따라 오름차순 정렬
    edges.sort(key=lambda x: x[2])

    # 2) 가중치가 가장 작은 간선부터 하나씩 선택
    for n1, n2, w in edges:

        # cycle이 존재하지 않는 경우
        if find_set(n1) != find_set(n2):
            union(n1, n2)   # 두 노드 합치기
            cnt += 1        # MST 간선 수 증가
            sum_weight += w # 가중치 누적

        # 노드가 N개(1~N)이므로 (N-1)개 간선 선택 완료 시 종료
        if cnt == N - 1:
            break

    return sum_weight   # MST의 가중치 합 반환

# main
N = int(input())    # N: 행성의 수 (= 노드의 수) 입력
costs = [list(map(int, input().split())) for _ in range(N)] # 행성 간 비용 정보 입력

# 간선 정보 생성(비용 행렬은 대칭이므로 절반(대각선 왼쪽 아래 삼각형)만 사용)
edges = []
for i in range(N):
    for j in range(i):
        edges.append((i, j, costs[i][j]))    # (행성 i, 행성 j, 비용)

parents = [i for i in range(N + 1)] # Union-find 부모 배열 초기화
min_cost = sum_weight_of_MST(edges) # MST 구성하고 가중치 합을 min_cost에 저장
print(min_cost) # 결과 출력
