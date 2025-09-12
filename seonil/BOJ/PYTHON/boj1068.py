"""
BOJ1068. 트리

[문제]
트리에서 리프 노드란, 자식의 개수가 0인 노드를 말한다.
트리가 주어졌을 때, 노드 하나를 지울 것이다. 그 때, 남은 트리에서 리프 노드의 개수를 구하는 프로그램을 작성하시오. 노드를 지우면 그 노드와 노드의 모든 자손이 트리에서 제거된다.
참고로, 지운 하나의 노드가 부모 노드인 경우 그 자식 노드들도 전부 지워진다.

[입력]
첫째 줄에 트리의 노드의 개수 N이 주어진다. N은 50보다 작거나 같은 자연수이다. 둘째 줄에는 0번 노드부터 N-1번 노드까지, 각 노드의 부모가 주어진다. 만약 부모가 없다면 (루트) -1이 주어진다. 셋째 줄에는 지울 노드의 번호가 주어진다.

[출력]
첫째 줄에 입력으로 주어진 트리에서 입력으로 주어진 노드를 지웠을 때, 리프 노드의 개수를 출력한다.
"""
import sys
input = sys.stdin.readline

from collections import deque

def remove_node(target):    # target 노드와 그 자식들을 모두 제거하는 함수

    # BFS(큐)를 이용해 target의 모든 자손을 탐색하며 제거
    q = deque([target])
    while q:
        rm = q.popleft()  # 현재 제거할 노드 dequeue
        if tree[rm]:
            # 자식이 있다면 큐에 모두 enqueue(자식도 함께 제거해야 함)
            for nrm in tree[rm]:
                q.append(nrm)
            # 제거 후 트리에 'removed'로 표시
            tree[rm] = ['removed']
        else:
            # 자식이 없다면 그냥 트리에 'removed'로 표시
            tree[rm] = ['removed']

    # 부모 노드가 target을 가리키는 경우, 그 연결도 끊어줘야 하므로, 부모의 자식 목록에서 target 제거
    for child_info in tree:
        for child in child_info:
            if child == target:
                child_info.remove(child)    # deque(value) → deque에서 value값을 가진 요소 제거


def count_leafs(tree):  # 리프 노드(자식이 없는 노드)의 개수를 세는 함수
    cnt_leafs = 0
    for child_info in tree:
        # 자식 리스트가 비어 있다면 리프 노드 ('removed'는 세지 않는다)
        if child_info == []:
            cnt_leafs += 1
    return cnt_leafs

# main
N = int(input())  # 트리의 노드 개수
parent_nodes = list(map(int, input().split()))  # 각 노드의 부모 정보
tree = [[] for _ in range(N)]  # 트리 구조 (부모-자식 연결 정보 저장용)

# 부모 정보를 바탕으로 트리 생성
for c, p in enumerate(parent_nodes):
    if p >= 0:             # 루트 노드(-1)의 부모 정보를 제외하고
        tree[p].append(c)  # 부모 p의 자식 목록에 현재 노드 c 추가

target = int(input())   # 제거할 노드 번호 입력
remove_node(target)     # 해당 노드와 자식들 제거
cnt = count_leafs(tree) # 리프 노드 개수 세기
print(cnt)  # 리프 노드 개수 출력
