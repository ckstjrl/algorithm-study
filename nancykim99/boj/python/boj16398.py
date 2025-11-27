'''
BOJ16398 : 행성 연결 (G4)

해결 방법 : 모든 노드를 다 연결하면서 최소 비용을 구하는 문제 -> MST
노드가 많지 않기에, 크루스칼로 해결

메모 : 
모든 간선을 넣었다가, 테케는 다 나오는데 틀려서 다시 보니, 간선을 반만 넣었어야 했음
'''

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
fee_arr = [list(map(int, input().split())) for _ in range(n)]
edges = [] # 간선 정보 담기
edges_num = int((n * (n-1)) / 2) # 간선의 수
total_cost = 0

# 간선 정보 구하기
for i in range(n):
    for j in range(i+1, n):
        if i != j:
            a, b, cost = i, j, fee_arr[i][j]
            edges.append((cost, a, b))

# 비용을 기준으로 정렬하기
edges.sort()

parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

for i in range(edges_num):
    cost, a, b = edges[i]
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        total_cost += cost

print(total_cost)