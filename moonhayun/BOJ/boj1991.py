"""
[문제]
이진 트리를 입력받아 전위 순회(preorder traversal), 중위 순회(inorder traversal), 후위 순회(postorder traversal)한 결과를 출력하는 프로그램을 작성하시오.

예를 들어 위와 같은 이진 트리가 입력되면,

전위 순회한 결과 : ABDCEFG // (루트) (왼쪽 자식) (오른쪽 자식)
중위 순회한 결과 : DBAECFG // (왼쪽 자식) (루트) (오른쪽 자식)
후위 순회한 결과 : DBEGFCA // (왼쪽 자식) (오른쪽 자식) (루트)
가 된다.

[입력]
첫째 줄에는 이진 트리의 노드의 개수 N(1 ≤ N ≤ 26)이 주어진다. 둘째 줄부터 N개의 줄에 걸쳐 각 노드와 그의 왼쪽 자식 노드, 오른쪽 자식 노드가 주어진다. 노드의 이름은 A부터 차례대로 알파벳 대문자로 매겨지며, 항상 A가 루트 노드가 된다. 자식 노드가 없는 경우에는 .으로 표현한다.

[출력]
첫째 줄에 전위 순회, 둘째 줄에 중위 순회, 셋째 줄에 후위 순회한 결과를 출력한다. 각 줄에 N개의 알파벳을 공백 없이 출력하면 된다.
"""
# def preorder_traverse(T): # 전위순회
#   if T: # T is not None
#     visit(T)  # print(T.item)
#     preorder_traverse(T.left)
#     preorder_traverse(T.right)

# def inorder_traverse(T):    # 중위순회
#   if T: # T is not none
#     inorder_traverse(T.left)
#     visit(T)  # print(T.item)
#     inorder_traverse(T.right)

# def postorder_traverse(T):  # 후위순회
#   if T:
#     postorder_traverse(T.left)
#     postorder_traverse(T.right)
#     visit(T)

import sys
input = sys.stdin.readline

def preorder_traverse(node):  # 전위순회
  if node == '.' or node not in tree:
    return ''
  l, r = tree[node]
  return node + preorder_traverse(l) + preorder_traverse(r)

def inorder_traverse(node):   # 중위순회
  if node == '.' or node not in tree:
    return ''
  l, r = tree[node]
  return inorder_traverse(l) + node + inorder_traverse(r)

def postorder_traverse(node):   # 후위순회
  if node == '.' or node not in tree:
    return ''
  l, r = tree[node]
  return postorder_traverse(l) + postorder_traverse(r) + node

N = int(input())
tree = {}
for _ in range(N):
  p, l, r = input().split()
  tree[p] = (l, r)

print(preorder_traverse('A'))
print(inorder_traverse('A'))
print(postorder_traverse('A'))