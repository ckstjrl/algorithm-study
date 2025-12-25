'''boj1068 트리
트리에서 리프 노드란, 자식의 개수가 0인 노드를 말한다.

트리가 주어졌을 때, 노드 하나를 지울 것이다. 그 때, 남은 트리에서 리프 노드의 개수를 구하는 프로그램을 작성하시오. 
노드를 지우면 그 노드와 노드의 모든 자손이 트리에서 제거된다.
'''

N = int(input()) # 트리의 노드 개수
parent = list(map(int, input().split()))
cut = int(input())

tree = [[] for _ in range(N)]
leaf = 0


for idx, p in enumerate(parent):
    if p == -1:
        continue
    else:
        tree[p].append(idx)

# print(f"tree {tree}")

for i in range(len(parent)):
    if len(tree[i]) == 0:
        leaf += 1

# print(f"leaf {leaf}")


def check_leaf(p):
    '''지울 노드를 넣으면 자식노드 갯수를 체크한다.
    자식노드가 있으면 각 자식노드에 대해서 check한다.
    자식 노드 없으면 leaf노드인 것.
    처음 leaf를 세어주었고, 이제 없어지는 노드를 입력받을 것이니
    leaf를 줄여준다.
    '''
    global leaf
    if len(tree[p]) == 2:
        c1, c2 = tree[p][0], tree[p][1]
        check_leaf(c1)
        check_leaf(c2)

    
    elif len(tree[p]) == 1:
        c = tree[p][0]
        check_leaf(c)

    #자식노드가 없으면? 리프노드인거임
    else:
        leaf -= 1
        return

check_leaf(cut)

#노드를 지웠는데 자식노드가 하나인 부모노드는 리프 노드가 됨
if len(tree[parent[cut]]) == 1:
    leaf += 1
# print(f"ans {leaf}")
print(leaf)
    
