"""
BOJ2644. 촌수계산

[문제]
우리 나라는 가족 혹은 친척들 사이의 관계를 촌수라는 단위로 표현하는 독특한 문화를 가지고 있다. 이러한 촌수는 다음과 같은 방식으로 계산된다.
기본적으로 부모와 자식 사이를 1촌으로 정의하고 이로부터 사람들 간의 촌수를 계산한다.
예를 들면 나와 아버지, 아버지와 할아버지는 각각 1촌으로 나와 할아버지는 2촌이 되고, 아버지 형제들과 할아버지는 1촌, 나와 아버지 형제들과는 3촌이 된다.
여러 사람들에 대한 부모 자식들 간의 관계가 주어졌을 때, 주어진 두 사람의 촌수를 계산하는 프로그램을 작성하시오.

[입력]
사람들은 1, 2, 3, …, n (1 ≤ n ≤ 100)의 연속된 번호로 각각 표시된다.
입력 파일의 첫째 줄에는 전체 사람의 수 n이 주어지고,
둘째 줄에는 촌수를 계산해야 하는 서로 다른 두 사람의 번호가 주어진다.
그리고 셋째 줄에는 부모 자식들 간의 관계의 개수 m이 주어진다.
넷째 줄부터는 부모 자식간의 관계를 나타내는 두 번호 x,y가 각 줄에 나온다. 이때 앞에 나오는 번호 x는 뒤에 나오는 정수 y의 부모 번호를 나타낸다.
각 사람의 부모는 최대 한 명만 주어진다.

[출력]
입력에서 요구한 두 사람의 촌수를 나타내는 정수를 출력한다. 어떤 경우에는 두 사람의 친척 관계가 전혀 없어 촌수를 계산할 수 없을 때가 있다. 이때에는 -1을 출력해야 한다.
"""

from collections import deque

# a, b의 촌수를 BFS로 구하여 반환하는 함수
def find_relationship_distance(a, b):

    # BFS 준비
    q = deque([a])  # 시작 노드: a
    visited = [-1] * (n + 1)    # a로부터 각각의 사람(노드)들의 촌수를 저장할 배열을 -1로 초기화
    visited[a] = 0  # 시작 노드의 촌수는 자기 자신이므로 0

    # BFS
    while q:
        cur_p = q.popleft()
        if cur_p == b:  # 목적지 노드 b에 도착하면 BFS 종료
            break
        for next_p in relationship[cur_p]:  # 연결된 노드들을 순회하면서,
            if visited[next_p] == -1:   # 다음 노드가 방문하지 않은 노드이면,
                q.append(next_p)    # 큐에 enqueue
                visited[next_p] = visited[cur_p] + 1    # visited에 (현재 촌수) + 1로 거리를 계산하여 저장
    
    return visited[b]   # 목적지 노드의 시작 노드로부터의 촌수 출력(관계 없으면 -1 출력됨)

# main
n = int(input())    # n: 전체 사람 수 
a, b = map(int, input().split())    # a, b: 촌수를 계산해야 하는 서로 다른 두 사람의 번호
m = int(input())    # m: 부모 자식들 간의 관계 개수
relationship = [[] for _ in range(n + 1)]  # 가족 관계 그래프(인접 리스트)
for _ in range(m):
    p, c = map(int, input().split())    # 부모, 자식 입력 받기
    relationship[p].append(c)
    relationship[c].append(p)   # 부모-자식 무방향 간선으로 연결

relation_dist = find_relationship_distance(a, b)    # a, b의 촌수를 구하여 relation_dist에 저장
print(relation_dist)    # 구한 촌수 결과를 출력