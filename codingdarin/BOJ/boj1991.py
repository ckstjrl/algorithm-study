# BOJ 1991. 트리순회 (D2 / S1)

n = int(input())
tree = {}
for _ in range(n):
	v, l, r = input().split()
	tree[v] = [l, r]

def preorder(node):
	if node == '.':
		return
	print(node, end='')
	preorder(tree[node][0])
	preorder(tree[node][1])

def inorder(node):
	if node == '.':
		return
	inorder(tree[node][0])
	print(node, end='')
	inorder(tree[node][1])

def postorder(node):
	if node == '.':
		return
	postorder(tree[node][0])
	postorder(tree[node][1])
	print(node, end='')

#1  전위순회 VLR
preorder('A')
print()

#2 중위순회 LVR
inorder('A')
print()

#3 후위순회 LRV
postorder('A')
print()
