# BOJ 1068. 트리
'''
트리에서 리프 노드란, 자식의 개수가 0인 노드를 말한다.

트리가 주어졌을 때, 노드 하나를 지울 것이다. 그 때, 남은 트리에서 리프 노드의 개수를 구하는 프로그램을 작성하시오.
노드를 지우면 그 노드와 노드의 모든 자손이 트리에서 제거된다.

첫째 줄에 트리의 노드의 개수 N이 주어진다. N은 50보다 작거나 같은 자연수이다.
둘째 줄에는 0번 노드부터 N-1번 노드까지, 각 노드의 부모가 주어진다.
만약 부모가 없다면 (루트) -1이 주어진다.
셋째 줄에는 지울 노드의 번호가 주어진다.

첫째 줄에 입력으로 주어진 트리에서 입력으로 주어진 노드를 지웠을 때, 리프 노드의 개수를 출력한다.
'''
import sys

N = int(sys.stdin.readline().strip())
parent = list(map(int, sys.stdin.readline().split()))
K = int(sys.stdin.readline().strip())

# 자식 인접 리스트 구성, 루트 찾기
children = [[] for _ in range(N)]
root = -1
for i, p in enumerate(parent):
    if p == -1:
        root = i
    else:
        children[p].append(i)

# 루트를 지우면 남는 트리가 없음
if K == root:
    print(0)
    sys.exit(0)

# 부모의 자식 목록에서 K 제거 (K 서브트리 전체가 단절됨)
pk = parent[K]
if pk != -1:
    # pk의 자식 리스트에서 K를 제거하면,
    # pk가 새롭게 리프가 될 수 있음
    children[pk] = [c for c in children[pk] if c != K]

# 루트부터 DFS하며 리프 개수 카운트
cnt = 0
def dfs(u: int):
    global cnt
    # 남은 자식이 없으면 리프
    if len(children[u]) == 0:
        cnt = cnt + 1
        return
    for v in children[u]:
        dfs(v)

dfs(root)
print(cnt)



# def del_node(idx):
#     if idx >= N:
#         return
#     else:
#         node[idx] = '' # if node[E_i]: 이런식으로 하면 False로 처리되어 if절 pass
#         return del_node(idx*2+1), del_node(idx*2+2)
#
# import sys
# N = int(sys.stdin.readline())
# node = list(map(int, input().split()))
# E_i = int(sys.stdin.readline())
# del_node(E_i)
# print(node)
# cnt = 0
# for i in range(1, N):
#     if 0<=2*i+1<N and 0<=2*i+2<N and (node[2*i+1] == True or node[2*i+2] == True):
#         continue
#     else:
#         if node[i] != '':
#             cnt += 1
#             print(i)
#
# print(cnt)
'''
이진트리인줄 알고 이진트리로 짠 코드...

인접리스트를 사용하여 자식 리스트를 만듦,
루트를 삭제할 경우 모든 트리가 삭제되게 만듦
DFS를 사용하여 리프 노드 갯수 세기
'''