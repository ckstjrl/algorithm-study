# def make_set(x):
#     p[x] = x
#     rank[x] = 0
#
# def find_set(x):
#     if x != p[x]:
#         p[x] = find_set(x)
#     return p[x]
#
# def union(x, y):
#     link(find_set(x), find_set(y))
#
# def link(x, y):
#     if rank[x] > rank[y]:
#         p[y] = x
#     elif rank[x] < rank[y]:
#         p[x] = y
#     else:
#         p[y] = x
#         rank[x] += 1
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     n = int(input())
#     k = int(input())
#     pair = [list(map(int, input().split())) for _ in range(k)]
#     m = int(input())
#     check = [list(map(int, input().split())) for _ in range(m)]
#
#     p = [0] * n
#     rank = [0] * n
#     for i in range(n):
#         make_set(i)
#     for i, j in pair:
#         union(i, j)
#     print(f'Scenario {tc}')
#     for i, j in check:
#         if find_set(i) != find_set(j):
#             print(0)
#         else:
#             print(1)

# def make_set(x):
#     p[x] = x
#     rank[x] = 0
#
# def find_set(x):
#     if x != p[x]:
#         p[x] = find_set(p[x])
#     return p[x]
#
# def union(x, y):
#     link(find_set(x), find_set(y))
#
# def link(x, y):
#     if rank[x] > rank[y]:
#         p[y] = x
#     elif rank[x] < rank[y]:
#         p[x] = y
#     else:
#         p[y] = x
#         rank[x] += 1
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     n = int(input())
#     k = int(input())
#     pair = [list(map(int, input().split())) for _ in range(k)]
#     m = int(input())
#     check = [list(map(int, input().split())) for _ in range(m)]
#
#     p = [0] * n
#     rank = [0] * n
#     for i in range(n):
#         make_set(i)
#     for i, j in pair:
#         union(i, j)
#     print(f'Scenario {tc}')
#     for i, j in check:
#         if p[i] != p[j]:
#             print(0)
#         else:
#             print(1)

def make_set(x):
    p[x] = x

def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]

def union(x, y):
    rootx = find_set(x)
    rooty = find_set(y)
    if rootx != rooty:
        p[rooty] = rootx

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    k = int(input())
    pair = [list(map(int, input().split())) for _ in range(k)]
    m = int(input())
    check = [list(map(int, input().split())) for _ in range(m)]

    p = [0] * n
    for i in range(n):
        make_set(i)

    for i, j in pair:
        union(i, j)
    print(f"Scenario {tc}:")
    for i, j in check:
        if find_set(i) == find_set(j):
            print(1)
        else:
            print(0)
    print()
