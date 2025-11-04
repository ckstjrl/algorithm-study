# BOJ1068(D3): 트리

# 나무 안깎고 pass하면서 리프 세기
def count_leaves(n):
    global cnt
    if n == pass_node:
        parent_node = parents[pass_node]
        if parent_node != -1 and len(tree[parent_node]) == 1:
            cnt += 1
        return

    if not tree[n]:
        cnt += 1
        return

    for child in tree[n]:
        count_leaves(child)

# Main
N = int(input())
parents = list(map(int, input().split()))
pass_node = int(input())

tree = [[] for _ in range(N)]
for i in range(N):
    if parents[i] == -1:
        root = i
    else:
        tree[parents[i]].append(i)

cnt = 0
count_leaves(root)
print(cnt)

# 나무 깎기
# def ree_trim(n):
#     global tree
#     if not tree[n]:
#         return
#     for child in tree[n]:
#         tree_trim(child)
#     tree[n].clear()
#
# def count_leaves(n):
#     global cnt
#     if not tree[n]:
#         cnt += 1
#         return
#     for child in tree[n]:
#         count_leaves(child)
#
# # Main
# N = int(input())
# tree = [[] for _ in range(N)]
#
# nodes = list(map(int, input().split()))
# for i in range(N):
#     if nodes[i] != -1:
#         tree[nodes[i]].append(i)
#     else:
#         root = i
#
# x = int(input())
# tree_trim(x)
# for node in tree:
#     if x in node:
#         node.remove(x)
#
# cnt = 0
# count_leaves(root)
#
# if x != root:
#     print(cnt)
# else:
#     print(0)