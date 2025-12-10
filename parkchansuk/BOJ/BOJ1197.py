# BOJ 1197. 최소 스패닝 트리 / D3
'''
문제
그래프가 주어졌을 때, 그 그래프의 최소 스패닝 트리를 구하는 프로그램을 작성하시오.

최소 스패닝 트리는, 주어진 그래프의 모든 정점들을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리를 말한다.

입력
첫째 줄에 정점의 개수 V(1 ≤ V ≤ 10,000)와 간선의 개수 E(1 ≤ E ≤ 100,000)가 주어진다. 다음 E개의 줄에는 각 간선에 대한 정보를 나타내는 세 정수 A, B, C가 주어진다. 이는 A번 정점과 B번 정점이 가중치 C인 간선으로 연결되어 있다는 의미이다. C는 음수일 수도 있으며, 절댓값이 1,000,000을 넘지 않는다.

그래프의 정점은 1번부터 V번까지 번호가 매겨져 있고, 임의의 두 정점 사이에 경로가 있다. 최소 스패닝 트리의 가중치가 -2,147,483,648보다 크거나 같고, 2,147,483,647보다 작거나 같은 데이터만 입력으로 주어진다.

출력
첫째 줄에 최소 스패닝 트리의 가중치를 출력한다.
'''
import sys

input = sys.stdin.readline

V, E = map(int, input().split())
graph = []
for _ in range(E):
    s, e, w = map(int, input().split())
    graph.append((s, e, w))

# 노드 x의 부모노드를 저장하는 리스트, 초기값은 자기 자신으로 자신이 루트인 상태
parents = [i for i in range(V+1)]
# 루트 노드 x가 대표하는 트리의 대략적인 깊이를 저장하는 리스트, 어느 쪽이 더 깊은지 확인하는 데 사용
rank = [0] * (V+1)

# 부모 찾기, 경로 압축
def find_set(x):
    if parents[x] == x:
        return x

    # 경로 압축 과정
    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    nx = find_set(x) # x노드의 루트
    ny = find_set(y) # y노드의 루트

    if nx == ny: # 두 르츠가 동일하면 이미 연결되어 있음
        return False

    # nx가 루트인 트리가 ny가 루트인 트리보다 깊이가 낮다면 낮은 쪽을 깊은 쪽 밑으로 붙이는 과정
    if rank[nx] < rank[ny]:
        parents[nx] = ny

    # 그 외의 경우
    else:
        # 똑같이 깊이가 낮은 ny 트리를 nx 밑에 붙인다
        parents[ny] = nx
        # 만약 둘의 깊이가 동일하다면 nx가 더 깊어졌으므로 1추가
        if rank[nx] == rank[ny]:
            rank[nx] += 1

    return True

# 가중치 중심으로 sort
graph.sort(key=lambda x: x[2])

# 총비용
cost = 0
# 간선의 개수
cnt = 0

for s, e, w in graph:
    if union(s, e):
        cost += w
        cnt += 1
        if cnt == V-1:
            break

print(cost)

'''
kruskal 알고리즘 사용
문제 이름이 낯설었는데 최소 스패닝 트리가 MST와 동일한 말임
일반적인 union-find를 사용했는데
'런타임 에러 (RecursionError)' 발생
find_set함수의 깊이가 너무 깊어져서 문제가 발생함(재귀를 너무 많이 호출함)
그래서 rank 리스트를 통하여 경로 압축 -> 깊이가 길어지는 것을 방지
'''