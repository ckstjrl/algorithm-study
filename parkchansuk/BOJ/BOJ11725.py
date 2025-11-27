# BOJ 11725. 트리의 부모 찾기 / D2
'''
루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.

첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.
'''
import sys
N = int(sys.stdin.readline())

tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

visited = [-1] * (N+1)
stk = [1]
visited[1] = 0
while stk:
    t = stk.pop()
    for i in tree[t]:
        if visited[i] == -1:
            visited[i] = visited[t] + 1
            stk.append(i)


for j in range(2, N+1):
    for a in tree[j]:
        if visited[j] > visited[a]:
           print(a)

'''
각 트리를 다 방문하면서 1에서부터 몇번 움직여야 하는지 계산하여 visited에 넣어줌
처음 tree에 제작한 그래프 구조를 활용하여
i 노드가 a, b와 연결된 경우 a, b 중 visited가 더 작은 것이 부모 노드가 되는 로직 활용
'''