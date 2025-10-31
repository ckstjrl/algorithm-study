"""
BOJ11403. 경로 찾기

[문제]
가중치 없는 방향 그래프 G가 주어졌을 때, 모든 정점 (i, j)에 대해서, i에서 j로 가는 길이가 양수인 경로가 있는지 없는지 구하는 프로그램을 작성하시오.

[입력]
첫째 줄에 정점의 개수 N (1 ≤ N ≤ 100)이 주어진다.
둘째 줄부터 N개 줄에는 그래프의 인접 행렬이 주어진다.
i번째 줄의 j번째 숫자가 1인 경우에는 i에서 j로 가는 간선이 존재한다는 뜻이고, 0인 경우는 없다는 뜻이다. i번째 줄의 i번째 숫자는 항상 0이다.

[출력]
총 N개의 줄에 걸쳐서 문제의 정답을 인접행렬 형식으로 출력한다.
정점 i에서 j로 가는 길이가 양수인 경로가 있으면 i번째 줄의 j번째 숫자를 1로, 없으면 0으로 출력해야 한다.
"""

from collections import deque

# x에서 y로 가는 길이가 양수인 경로가 존재하면 1, 존재하지 않으면 0을 반환하는 함수 
def path_exists(x, y):

    # BFS 준비
    q = deque([x])
    visited = [False] * N
    visited[x] = 0

    # BFS 수행
    while q:
        cur_node = q.popleft()
        
        for next_node in range(N):  # 0번부터 N-1번 노드를 순회하면서,
            if adj_matrix[cur_node][next_node] == 1 and not visited[next_node]:  # 현재 노드부터 다음 노드로의 간선이 존재하고, 다음 노드가 방문하지 않은 노드라면,
                q.append(next_node)  # 다음 노드를 큐에 enqueue
                visited[next_node] = True  # 다음 노드 방문 체크
                if next_node == y:  # 다음 노드가 목적지 노드 y라면,
                    return 1  # 길이가 0이 아닌 노드가 존재하는 것이므로 1 반환
    
    return 0  # BFS로 y에 도달할 수 없다면 경로가 없는 것이므로 0 반환 

# 모든 정점 (i, j)에 대해서, i에서 j로 가는 길이가 양수인 경로가 있는지 없는지 인접행렬로 결과를 출력하는 함수
def print_reachability_matrix():
    result = [[0] * N for _ in range(N)]  # 경로 존재 여부를 저장할 행렬을 0으로 초기화 
    for i in range(N):
        for j in range(N):
            result[i][j] = path_exists(i, j)  # 각 정점 (i, j)에 대해서, i에서 j로 가는 길이가 양수인 경로가 있는지 없는지를 저장
    
    for i in range(N):
        print(" ".join(map(str, result[i])))  # 결과 출력


# main
N = int(input())  # N: 정점의 개수
adj_matrix = [list(map(int, input().split())) for _ in range(N)]  # adj_matrix: 그래프의 인접 행렬

print_reachability_matrix()  # 경로 존재 여부를 나타내는 인접행렬 출력
