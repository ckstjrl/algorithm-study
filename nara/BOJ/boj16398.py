import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
edges = []
for i in range(N):
    for j in range(N):
        if i != j:
            edges.append((i, j, graph[i][j]))
edges.sort(key=lambda x: x[2])

parent = [i for i in range(N+1)]


def get_parent(x):
    if parent[x] == x:
        return x
    parent[x] = get_parent(parent[x])
    return parent[x]


def union_parent(a, b):
    a = get_parent(a)
    b = get_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def same_parent(a, b):
    return get_parent(a) == get_parent(b)


answer = 0
for a, b, cost in edges:
    if not same_parent(a, b):
        union_parent(a, b)
        answer += cost
print(answer)