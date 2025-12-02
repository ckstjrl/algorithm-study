"""
BOJ1325. 효율적인 해킹

[문제]
해커 김지민은 잘 알려진 어느 회사를 해킹하려고 한다.
이 회사는 N개의 컴퓨터로 이루어져 있다.
김지민은 귀찮기 때문에, 한 번의 해킹으로 여러 개의 컴퓨터를 해킹 할 수 있는 컴퓨터를 해킹하려고 한다.
이 회사의 컴퓨터는 신뢰하는 관계와, 신뢰하지 않는 관계로 이루어져 있는데, A가 B를 신뢰하는 경우에는 B를 해킹하면, A도 해킹할 수 있다는 소리다.
이 회사의 컴퓨터의 신뢰하는 관계가 주어졌을 때, 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 출력하는 프로그램을 작성하시오.

[입력]
첫째 줄에, N과 M이 들어온다. N은 10,000보다 작거나 같은 자연수, M은 100,000보다 작거나 같은 자연수이다.
둘째 줄부터 M개의 줄에 신뢰하는 관계가 A B와 같은 형식으로 들어오며, "A가 B를 신뢰한다"를 의미한다. 컴퓨터는 1번부터 N번까지 번호가 하나씩 매겨져 있다.

[출력]
첫째 줄에, 김지민이 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 오름차순으로 출력한다.
"""

from collections import deque

import sys
input = lambda: sys.stdin.readline().rstrip()

# BFS로 연결된 모든 컴퓨터들을 해킹하고, 해킹한 컴퓨터(노드)의 수를 반환하는 함수
def bfs(start):

    # BFS 준비
    visited = [False] * (N + 1)
    q = deque([start])
    visited[start] = True
    cnt = 1     # 해킹한 컴퓨터의 개수를 시작 노드를 세서 1로 초기화

    # BFS
    while q:
        cur_node = q.popleft()
        for next_node in graph[cur_node]:   # 연결된 모든 노드를 순회
            if not visited[next_node]:  # 방문한 노드가 아니라면
                visited[next_node] = True   # 방문 체크
                q.append(next_node) # 큐에 추가
                cnt += 1    # 해킹한 컴퓨터 개수 세기

    return cnt  # 해킹한 컴퓨터 수의 총합 반환

# main
N, M = map(int, input().split())    # N: 컴퓨터의 수, M: 신뢰 관계의 수
graph = [[] for _ in range(N + 1)]  # 인접 노드 리스트
for _ in range(M):
    A, B = map(int, input().split())
    graph[B].append(A)  # B → A 방향 간선 정보 저장

hack_count = [0] * (N + 1)  # bfs 결과를 저장하는 배열
for node in range(N + 1):
    cnt = bfs(node)
    hack_count[node] = cnt # bfs 결과 저장

max_count = max(hack_count) # 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터 개수를 max_count에 저장
for node, cnt in enumerate(hack_count):
    if cnt == max_count:
        print(node, end=' ')    # 최대 개수의 컴퓨터를 해킹할 수 있는 노드 번호들을 오름차순으로 출력


"""
탐구: 문제를 다 풀어놓고도 시간 초과 걸릴거 같은 느낌이 들어서 싸했는데... 어쨌든 통과되었다! (이게 왜 되는거지??)
그런데 딱히 메모리 혹은 시간 복잡도 측면에서 보았을 때 그리 좋은 코드는 아닌 것 같았다.
뭔가 개선할 방법을 이것저것 찾아 봤는데... visited 배열을 전역에 두고 재사용하는 방법이 있었다.
핵심 아이디어는 각 BFS에서만 의미가 있는 태그(tag)를 값으로 쓰는 것이다! 예) BFS(1)에서 방문했던 노드는 visited 값이 1, BFS(2)에서 방문한 노드는 visited 값이 2, ...
엄청나게 빨라지지는 않았지만, 그래도 유의미한 개선을 이루었으니 나중에 참고하면 좋을듯!

from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[B].append(A)

visited = [0] * (N + 1)
hack_count = [0] * (N + 1)

for start in range(1, N + 1):
    q = deque([start])
    visited[start] = start  # visited를 start 번호로 표시
    cnt = 1

    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if visited[nxt] != start:   # start의 BFS에서 방문한 적 없음
                visited[nxt] = start
                q.append(nxt)
                cnt += 1

    hack_count[start] = cnt

max_cnt = max(hack_count)
for i in range(1, N + 1):
    if hack_count[i] == max_cnt:
        print(i, end=' ')

"""