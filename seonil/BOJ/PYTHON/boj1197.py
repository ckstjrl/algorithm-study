"""
BOJ1197. 최소 스패닝 트리

[문제]
그래프가 주어졌을 때, 그 그래프의 최소 스패닝 트리를 구하는 프로그램을 작성하시오.
최소 스패닝 트리는, 주어진 그래프의 모든 정점들을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리를 말한다.

[입력]
첫째 줄에 정점의 개수 V(1 ≤ V ≤ 10,000)와 간선의 개수 E(1 ≤ E ≤ 100,000)가 주어진다.
다음 E개의 줄에는 각 간선에 대한 정보를 나타내는 세 정수 A, B, C가 주어진다. 이는 A번 정점과 B번 정점이 가중치 C인 간선으로 연결되어 있다는 의미이다. C는 음수일 수도 있으며, 절댓값이 1,000,000을 넘지 않는다.
그래프의 정점은 1번부터 V번까지 번호가 매겨져 있고, 임의의 두 정점 사이에 경로가 있다. 최소 스패닝 트리의 가중치가 -2,147,483,648보다 크거나 같고, 2,147,483,647보다 작거나 같은 데이터만 입력으로 주어진다.

[출력]
첫째 줄에 최소 스패닝 트리의 가중치를 출력한다.
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

# 반복문과 경로 단축을 이용하여 대표 노드를 찾는 함수
# 재귀 대신 while을 사용하여 RecursionError 방지!(이번 문제에서 배운 것)
def find_set(x):
    while x != parents[x]:  # 자기 자신이 부모가 아니라면 다음을 반복 수행
        # 경로 단축 기법: 상위 부모 노드를 부모로 설정
        parents[x] = parents[parents[x]]
        x = parents[x]
    return x

# 두 집합을 하나로 합치는 함수
def union(x, y):

    # 각 노드의 대표 찾기
    rx = find_set(x)
    ry = find_set(y)

    # 이미 서로 같은 집합이면, 합칠 필요가 없으므로 종료
    if rx == ry:
        return
    
    # 서로 다른 집합이면, 번호가 작은 root쪽에 합치도록 구현
    elif rx < ry:
        parents[ry] = rx
    else:
        parents[rx] = ry

# Kruskal 알고리즘으로 MST 가중치를 계산하는 함수
def sum_weight_of_MST(edges):

    cnt, sum_weight = 0, 0

    # 1. 모든 간선을 가중치 기준으로 오름차순으로 정렬
    edges.sort(key=lambda x: x[2])

    # 가중치가 작은 간선부터 차례대로 선택:
    for n1, n2, w in edges:
        if find_set(n1) != find_set(n2):    # cycle이 존재하지 않는 경우,
            union(n1, n2)   # 가중치가 가장 낮은 간선부터 선택하며 트리 증가
            cnt += 1
            sum_weight += w
        if cnt == V - 1:    # 노드가 V개(1~V)이므로 (V-1)개 간선 선택 완료 시 종료
            break
    return sum_weight

# main
V, E = map(int, input().split())    # V: 정점의 개수, E: 간선의 개수

edges = []
for _ in range(E):  # E개의 줄에 걸쳐서 입력 받기
    A, B, C = map(int, input().split()) # A: 간선의 한 정점, B, 간선의 다른 한 정점, C: 가중치
    edges.append((A, B, C)) # 간선 정보를 edges에 저장

parents = [i for i in range(V + 1)] # parents 배열 초기화: 처음에는 각 노드가 자기 자신이 root
answer = sum_weight_of_MST(edges)   # MST의 가중치 합을 구하여 answer에 저장
print(answer)   # 결과 반환

"""
처음에 아래 코드와 같이 알고리즘 수업 때 배웠던 대로 풀었는데, RecursionError가 발생했다.
원인을 찾아보니 ... 재귀 기반 find_set 때문에 스택이 깊어져 RecursionError이 발생한 것이라고 한다.
union 로직이 rank나 size를 고려하지 않고 단순히 작은 번호를 부모로 삼도록 작성되었기 때문에,
만약 부모들이 10000 → 9999 → 9998 → ... → 1 와 같이 연결되어 있다면, 한쪽으로만 깊게 합쳐지면서 편향 트리(Linear Tree)가 생성된다.
따라서 이런 경우에 호출 깊이 ≒ 10,000이 넘어가서 파이썬 기본 재귀 한도(약 1,000)를 초과하기 때문에 터지는 것!!
해결 방법은 while문을 이용하여 경로 단축을 하는 것이었다. 나중에 참고해야지...
"""
"""
import sys
input = lambda: sys.stdin.readline().rstrip()

def find_set(x):
    if x == parents[x]:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    
    rx = find_set(x)
    ry = find_set(y)

    if rx == ry:
        return    
    elif rx < ry:
        parents[ry] = rx
    else:
        parents[rx] = ry

def sum_weight_of_MST(edges):

    cnt, sum_weight = 0, 0

    edges.sort(key=lambda x: x[2])
    for n1, n2, w in edges:
        if find_set(n1) != find_set(n2):
            union(n1, n2)
            cnt += 1
            sum_weight += w
        if cnt == V - 1:
            break
    return sum_weight

# main
V, E = map(int, input().split())
edges = []
for _ in range(E):
    A, B, C = map(int, input().split())
    edges.append((A, B, C))

parents = [i for i in range(V + 1)]
answer = sum_weight_of_MST(edges)
print(answer)
"""