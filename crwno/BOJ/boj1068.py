# def f(E, node):
#     global cnt
#     stack = [0]
#     visited = [False] * N
#     while stack:
#         start = stack.pop()
#         for i in range(start + 1, N):
#             if start == node[i] and not visited[i]:
#                 visited[i] = True
#                 if i != E:
#                     stack.append(i)
#                 else:
#                     node[i] = -1
#         if start not in node:
#             cnt += 1
#
# N = int(input())
# node = list(map(int, input().split()))
# E = int(input())
# cnt = 0
# if E != 0:
#     f(E, node)
# print(cnt)

def f(s, E, node):
    global cnt
    stack = [s]
    visited = [False] * N
    while stack:
        start = stack.pop()
        for i in range(N):
            if start == node[i] and not visited[i]:
                visited[i] = True
                if i != E:
                    stack.append(i)
                else:
                    node[i] = -2
        if start not in node:
            cnt += 1

N = int(input())
node = list(map(int, input().split()))
E = int(input())
cnt = 0
for i in range(N):
    if node[i] == -1:
        s = i
if E == s:
    print(0)
else:
    f(s, E, node)
    print(cnt)
