"""
BOJ18352. 특정 거리의 도시 찾기

[문제]
어떤 나라에는 1번부터 N번까지의 도시와 M개의 단방향 도로가 존재한다.
모든 도로의 거리는 1이다.
이 때 특정한 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중에서,
최단 거리가 정확히 K인 모든 도시들의 번호를 출력하는 프로그램을 작성하시오.
또한 출발 도시 X에서 출발 도시 X로 가는 최단 거리는 항상 0이라고 가정한다.

예를 들어 N=4, K=2, X=1일 때 다음과 같이 그래프가 구성되어 있다고 가정하자.
이 때 1번 도시에서 출발하여 도달할 수 있는 도시 중에서, 최단 거리가 2인 도시는 4번 도시 뿐이다.
2번과 3번 도시의 경우, 최단 거리가 1이기 때문에 출력하지 않는다.

[입력]
첫째 줄에 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X가 주어진다.
(2 ≤ N ≤ 300,000, 1 ≤ M ≤ 1,000,000, 1 ≤ K ≤ 300,000, 1 ≤ X ≤ N)
둘째 줄부터 M개의 줄에 걸쳐서 두 개의 자연수 A, B가 공백을 기준으로 구분되어 주어진다.
이는 A번 도시에서 B번 도시로 이동하는 단방향 도로가 존재한다는 의미다. (1 ≤ A, B ≤ N) 단, A와 B는 서로 다른 자연수이다.

[출력]
X로부터 출발하여 도달할 수 있는 도시 중에서, 최단 거리가 K인 모든 도시의 번호를 한 줄에 하나씩 오름차순으로 출력한다.
이 때 도달할 수 있는 도시 중에서, 최단 거리가 K인 도시가 하나도 존재하지 않으면 -1을 출력한다.
"""
import sys
input = sys.stdin.readline
from collections import deque

def find_cities_at_distance_k(start, K):

    # bfs 준비
    visited = [-1] * (N + 1)
    q = deque([start])
    visited[start] = 0

    # bfs
    while q:
        current = q.popleft()
        for next in graph[current]:
            if visited[next] == -1:
                q.append(next)
                visited[next] = visited[current] + 1

    # visited 배열을 체크
    cities_at_distance_k = []   # 거리가 k인 도시들을 담을 빈 리스트 초기화
    for city in range(1, N + 1):    # visited 배열의 도시들(1, 2, ... , N)을 오름차순으로 순회하면서
        if visited[city] == K:  # 거리가 K인 도시가 있다면
            cities_at_distance_k.append(city)   # 리스트에 그대로 append(도시 번호 오름차순이 그대로 유지)

    return cities_at_distance_k # 결과 배열을 반환

# main
N, M, K, X = map(int, input().split())  # N: 도시 개수, M: 단방향 도로 개수, K: 최단 거리, X: 출발 도시
graph = [[] for _ in range(N + 1)]  # 인접 리스트 형식으로 그래프 저장
for _ in range(M):  # 간선의 개수 M번만큼
    A, B = map(int, input().split())    # 간선의 시작점 A, 간선의 끝점 B를 입력받아
    graph[A].append(B)  # 인접 리스트 형식으로 저장
cities_at_distance_k = find_cities_at_distance_k(X, K)  # BFS를 통해 최단거리 K만큼 떨어진 도시 리스트를 구하여 저장
if cities_at_distance_k == []:  # 탐색 결과가 빈 리스트이면 -1 출력
    print(-1)
else:   # 탐색 결과가 빈 리스트가 아니라면,
    for city in cities_at_distance_k:   # 리스트에 담긴 각 도시 번호를 오름차순으로 출력
        print(city)
