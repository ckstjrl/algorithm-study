# BOJ1991(D2): 트리 순회
import sys

def preorder(n):
    if n != '.':
        print(n, end='')
        preorder(tree[n][0])
        preorder(tree[n][1])

def inorder(n):
    if n != '.':
        inorder(tree[n][0])
        print(n, end='')
        inorder(tree[n][1])

def postorder(n):
    if n != '.':
        postorder(tree[n][0])
        postorder(tree[n][1])
        print(n, end='')

N = int(sys.stdin.readline())
tree = {}

for _ in range(N):
    root, left, right = sys.stdin.readline().split()
    tree[root] = [left, right]

preorder('A')
print()
inorder('A')
print()
postorder('A')