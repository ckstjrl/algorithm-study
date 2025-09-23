# T = int(input())
# for tc in range(1, T + 1):
#     V, E = map(int, input().split())
#     info = [list(map(int, input().split())) for _ in range(E)]
#
#     graph = [[] for _ in range(V + 1)]
#     for u, v in info:
#         graph[u].append(v)
#         graph[v].append(u)
#
#     visited = [False] * (V + 1)
#     visited[1] = True
#     stack = []
#     pal = [0] * (V + 1)
#     cnt = 0
#     flag = -1
#
#     def color(s):
#         global cnt, flag
#         cnt += 1
#         for i in graph[s]:
#             if not visited[i]:
#                 visited[i] = True
#                 stack.append(i)
#                 color(i)
#                 s = stack.pop()
#                 if cnt % 2 == 1:
#                     if pal[s] == 1:
#                         flag = 1
#                         break
#                     pal[s] = 1
#                 elif cnt % 2 == 0:
#                     if pal[s] == -1:
#                         flag = 1
#                         break
#                     pal[s] = -1
#     color(1)
#     if flag == -1:
#         print('YES')
#     else:
#         print('NO')

# from collections import deque
#
#
# def color(s):
#     global flag
#     q = deque()
#     q.append(s)
#     while q:
#         start = q.popleft()
#         visited[start] = True
#         for i in graph[start]:
#             if not visited[i]:
#                 if pal[i] == 0:
#                     pal[i] = -pal[start]
#                 else:
#                     if pal[i] == pal[start]:
#                         flag = 1
#                         break
#                 q.append(i)
#
# T = int(input())
#
# for tc in range(1, T + 1):
#     V, E = map(int, input().split())
#     info = [list(map(int, input().split())) for _ in range(E)]
#
#     graph = [[] for _ in range(V + 1)]
#     for u, v in info:
#         graph[u].append(v)
#         graph[v].append(u)
#
#     visited = [False] * (V + 1)
#     pal = [0] * (V + 1)
#
#     for i in range(1, V + 1):
#         if len(graph) != 0:
#             s = i
#             break
#
#     visited[s] = True
#     pal[s] = 1
#     flag = -1
#     color(s)
#
#     if flag == -1:
#         print('YES')
#     else:
#         print('NO')

# 한 점만 검사하면 안됨 -> 아예 그래프가 여러개일지도?
from collections import deque


def color(s):
    global flag
    q = deque()
    q.append(s)
    while q:
        start = q.popleft()
        visited[start] = True
        for i in graph[start]:
            if not visited[i]:
                pal[i] = -pal[start]
                q.append(i)
            else:
                if pal[i] == pal[start]:
                    flag = 1
                    return

T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(E)]

    graph = [[] for _ in range(V + 1)]
    for u, v in info:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * (V + 1)
    pal = [0] * (V + 1)
    flag = -1

    for i in range(1, V + 1):
        if not visited[i]:
            if pal[i] == 0:
                pal[i] = 1
            color(i)
            if flag == 1:
                break

    if flag == -1:
        print('YES')
    else:
        print('NO')