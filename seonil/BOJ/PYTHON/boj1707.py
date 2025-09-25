"""
BOJ1707. 이분 그래프
[문제]
그래프의 정점의 집합을 둘로 분할하여, 각 집합에 속한 정점끼리는 서로 인접하지 않도록 분할할 수 있을 때, 그러한 그래프를 특별히 이분 그래프 (Bipartite Graph) 라 부른다.
그래프가 입력으로 주어졌을 때, 이 그래프가 이분 그래프인지 아닌지 판별하는 프로그램을 작성하시오.

[입력]
입력은 여러 개의 테스트 케이스로 구성되어 있는데, 첫째 줄에 테스트 케이스의 개수 K가 주어진다. 각 테스트 케이스의 첫째 줄에는 그래프의 정점의 개수 V와 간선의 개수 E가 빈 칸을 사이에 두고 순서대로 주어진다. 각 정점에는 1부터 V까지 차례로 번호가 붙어 있다. 이어서 둘째 줄부터 E개의 줄에 걸쳐 간선에 대한 정보가 주어지는데, 각 줄에 인접한 두 정점의 번호 u, v (u ≠ v)가 빈 칸을 사이에 두고 주어진다.

[출력]
K개의 줄에 걸쳐 입력으로 주어진 그래프가 이분 그래프이면 YES, 아니면 NO를 순서대로 출력한다.

[제한]
2 ≤ K ≤ 5
1 ≤ V ≤ 20,000
1 ≤ E ≤ 200,000
"""
import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

def check_bipartite(start):

    q = deque([(start, 1)]) # 시작 정점을 그룹 '1'로 두고 BFS 시작
    visited[start] = 1  # visited에 정점의 그룹 기록

    while q:
        node, group = q.popleft()
        # 현재 정점과 연결된 이웃 노드들을 확인하며,
        for nbr in graph[node]:
            if visited[nbr] == 0:
                # 아직 방문하지 않은 정점이면 현재 그룹의 반대 그룹 '-1'으로 기록하고 큐에 enqueue
                visited[nbr] = -group
                q.append((nbr, -group))
            else:
                # 이미 방문한 정점인데 같은 그룹이라면 이분 그래프가 아니므로 False 반환 후 종료
                if visited[nbr] == group:
                    return False
    # 모순 없이 모든 이웃 탐색을 끝내면 이분 그래프 조건 만족하므로 True 반환 후 종료
    return True

# main
K = int(input())  # 테스트 케이스 개수
for _ in range(K):
    V, E = map(int, input().split())  # 정점 수, 간선 수
    graph = [[] for _ in range(V + 1)]  # 인접 리스트로 그래프 표현
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)  # 무방향 그래프이므로 양쪽에 모두 추가

    visited = [0] * (V + 1)  # 방문 및 그룹 정보 (0 = 미방문, 1 = 그룹 A, -1 = 그룹 B)
    is_bipartite = True # default : 이분 그래프라고 가정
    # 그래프가 여러 연결 요소로 나눠질 수 있으므로 모든 정점에서 검사
    for node in range(1, V + 1):
        if visited[node] == 0:  # 아직 방문 안 한 연결 요소의 노드라면
            if not check_bipartite(node):  # BFS로 그룹을 구분하고, 모순을 발견하면
                is_bipartite = False    # 이분 그래프 아닌거 확인 후 검사 종료
                break

    # 최종 판정 출력
    print("YES" if is_bipartite else "NO")

"""
# 실패 코드 - 시간 초과(TLE)
# 실패 이유 : main 함수의 다음 코드 라인에서
# for node in range(1, V + 1):
#        is_bipartite_graph *= check_bipartite(node)
# 각 노드의 개수인 V번만큼 bfs를 수행하게 하면서 검사하게 했는데,
# V번의 검사 동안 check_bipartite 내부의 visited 배열을 계속 0으로 초기화하면서 bfs를 수행하므로
# 이때 시간 복잡도가 크게 증가함(왜냐면 V는 최대 20,000)
# 통과 코드에서는 visited 배열 밖으로 빼서 해결함. ^_^

import sys
input = lambda: sys.stdin.readline().rstrip()

from collections import deque

def check_bipartite(start):
    q = deque([(start, 1)])
    visited = [0] * (V + 1) # TLE 원인
    visited[start] = 1

    while q:
        node, group = q.popleft()
        for nbr in graph[node]:
            if visited[nbr] == 0:
                visited[nbr] = -group
                q.append((nbr, -group))
            else:
                if visited[nbr] != -group:
                    return 0

    return 1

# main
K = int(input())
for tc in range(1, K + 1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    is_bipartite_graph = 1
    for node in range(1, V + 1):
        is_bipartite_graph *= check_bipartite(node) # TLE 원인
    print('YES' if is_bipartite_graph else 'NO')
"""