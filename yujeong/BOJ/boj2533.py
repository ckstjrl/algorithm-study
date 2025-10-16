# 2533. 얼리어답터
# 얼리어답터 수가 최소이려면 리프 노드들은 얼리어답터면 안 되고,
# 그러기 위해서는 리프 노드의 부모는 얼리어답터여야 함

import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
graph = [[] for _ in range(N+1)]    # 인접 그래프 만들기
for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
early = [False] * (N+1)     # early[i]: i번 노드가 얼리어답터인지
leafs = [i for i in range(1, N+1) if len(graph[i])==1]      # 리프 노드만 담은 리스트
leafs = deque(leafs)

# 리프 -> 부모 방향으로 탐색하며
# 리프 노드가 얼리어답터가 아니면 -> 그 부모를 얼리어답터로 만들기를 반복하기
while leafs:
    curr = leafs.popleft()
    if not graph[curr]:     # 연결된 노드 중 처리 안 된 노드 없음; 끝
        break
    p = graph[curr][0]      # 리프 노드의 부모
    if not early[curr]:     # 자식이 얼리어답터가 아니면 부모를 얼리어답터로
        early[p] = True
    graph[p].remove(curr)   # 부모 노드에서 이 자식 노드와 연결 제거 (처리 완료)
    if len(graph[p])==1:    # 이렇게 처리하다 보면 부모 노드의 자식이 없어짐 -> 이걸 리프 노드로 본다. 반복
        leafs.append(p)     # 큐에 넣기

print(sum(early))   # 얼리어답터인 노드들 개수 출력

