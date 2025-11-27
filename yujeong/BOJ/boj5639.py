# 5639. 이진 검색 트리 
# 전위순회한 결과가 주어졌을 때, 후위순회한 결과 출력하기 

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)    
'''
RecursionError 관련
BOJ 채점 서버에서 Python의 최대 재귀 깊이는 1,000으로 지정되어 있음. 
이 문제 채점에서 RecursionError를 발생시키지 않기 위해선 이 값을 늘려줘야 함...
'''

# 전위순회 결과 입력받아 후위순회 결과로 출력하는 함수 make_tree
def make_tree(arr):
    # 받은 subtree가 비어있는 경우(없는 경우) 아무 작업 수행 x 리턴 
    if not arr:
        return
    
    ltree, rtree = [], []   # 루트 기준 왼쪽/오른쪽 subtree 
    m = arr[0]              # 전위순회 결과이므로 루트 노드는 입력받은 subtree의 가장 앞 노드 

    for i in range(len(arr)):
        if arr[i] > m:          # 루트 노드보다 큰 값 등장하면 여기부터 오른쪽 subtree
            ltree = arr[1:i]
            rtree = arr[i:]
            break
    else:               # 모든 노드가 루트보다 값 작은 경우 전부 왼쪽 subtree
        ltree = arr[1:]
    
    # 후위순회 
    make_tree(ltree)
    make_tree(rtree)
    print(m)

tree = []

# 입력받아 배열에 저장 
while True:
    try:
        n = int(input())
        tree.append(n)

    # 더 이상 입력 없을 때까지 
    except:
        break   

make_tree(tree)
