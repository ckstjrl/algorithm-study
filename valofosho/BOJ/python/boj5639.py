"""
전위 순회한 결과가 주어지면
이를 통해 그래프를 먼저 그린다
이후 그래프를 후위순회하며 값을 출력한다
"""
import sys
input = sys.stdin.readline
# 재귀 깊이를 더 깊게 반복해도 에러가 나지 않게!!!
sys.setrecursionlimit(10**6)  
def postorder(node):
    if node > 0:
        postorder(left[node])
        postorder(right[node])
        print(node)
    return

def make_tree(child):
    parent = node
    while True:
        # 부모 노드보다 작으면
        if child < parent:    
            # 부모의 자식 노드가 비어있으면 삽입                                              
            if left[parent] == 0:
                left[parent] = child
                parent = child
                break
            # 아니면 부모의 자식노드를 부모로 변경
            else:
                parent = left[parent]
        # 부모 노드보다 크면
        elif child > parent:
            # 오른쪽 자식 노드가 비어있으면 삽입
            if right[parent] == 0:
                right[parent] = child
                parent = child
                break
            # 그렇지 않다면 부모노드의 자식을 부모로 재할당
            else:
                parent = right[parent]
    return 

node = int(input())
left = [0] * 1000001
right = [0] * 1000001

while True:
    try:
        num = int(input())
        make_tree(num)
    except:
        break


postorder(node)