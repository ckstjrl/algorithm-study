# N = int(input())
# gr = [list(map(int, input().split())) for _ in range(N)]
# cost = [[0] * N for _ in range(N)]
# for i in range(1, N - 1):
#     for j in range(1, N - 1):
#         for di, dj in (0, 0), (1, 0), (0, 1), (-1, 0), (0, -1):
#             ni, nj = i + di, j + dj
#             cost[i][j] += gr[ni][nj]
#
# cost_li = []
# for i in range(1, N - 1):
#     for j in range(1, N - 1):
#         cost_li.append((cost[i][j], i, j))
#
# cost_li.sort()
# adj = [
#     (0, 0),
#     (1, 0),
#     (0, 1),
#     (-1, 0),
#     (0, -1),
#     (2, 0),
#     (1, 1),
#     (0, 2),
#     (-1, 1),
#     (-2, 0),
#     (-1, -1),
#     (0, -2),
#     (1, -1)
# ]
# used = [[False] * N for _ in range(N)]
# res = 0
# cnt = 0
#
#
# l = len(cost_li)



# N = int(input())
# gr = [list(map(int, input().split())) for _ in range(N)]
# cost = [[0] * N for _ in range(N)]
# for i in range(1, N - 1):
#     for j in range(1, N - 1):
#         for di, dj in (0, 0), (1, 0), (0, 1), (-1, 0), (0, -1):
#             ni, nj = i + di, j + dj
#             cost[i][j] += gr[ni][nj]
#
# cost_li = []
# for i in range(1, N - 1):
#     for j in range(1, N - 1):
#         cost_li.append((cost[i][j], i, j))
#
# cost_li.sort()
# adj = [
#     (0, 0),
#     (1, 0),
#     (0, 1),
#     (-1, 0),
#     (0, -1),
#     (2, 0),
#     (1, 1),
#     (0, 2),
#     (-1, 1),
#     (-2, 0),
#     (-1, -1),
#     (0, -2),
#     (1, -1)
# ]
#
#
# def f(s):
#     flag = False
#     ans = 0
#     used = [[False] * N for _ in range(N)]
#     cnt = 0
#     while s < (N - 2) ** 2:
#         if cnt == 3:
#             flag = True
#             break
#         cst, x, y = cost_li[s]
#         if not used[x][y]:
#             for dx, dy in adj:
#                 nx, ny = x + dx, y + dy
#                 if 0 <= nx < N and 0 <= ny < N:
#                     used[nx][ny] = True
#             ans += cst
#             cnt += 1
#         s += 1
#     if flag:
#         return ans
#     else:
#         f(s + 1)
#
# print(f(0))

N = int(input())
gr = [list(map(int, input().split())) for _ in range(N)]
cost = [[0] * N for _ in range(N)]
for i in range(1, N - 1):
    for j in range(1, N - 1):
        for di, dj in (0, 0), (1, 0), (0, 1), (-1, 0), (0, -1):
            ni, nj = i + di, j + dj
            cost[i][j] += gr[ni][nj]

adj = [
    (0, 0),
    (1, 0),
    (2, 0),
    (0, 1),
    (0, 2),
    (-1, 0),
    (-2, 0),
    (0, -1),
    (0, -2),
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1)
]


used = [[-1] * N for _ in range(N)]
visited = [[False] * N for _ in range(N)]
min_cst = float('inf')


def f(cst, cnt):
    global min_cst
    if cnt == 3:
        min_cst = min(cst, min_cst)
        return

    for i in range(1, N - 1):
        for j in range(1, N - 1):
            if used[i][j] == -1 and not visited[i][j]:
                visited[i][j] = True
                for di, dj in adj:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < N and used[ni][nj] == -1:
                        used[ni][nj] = cnt
                f(cst + cost[i][j], cnt + 1)
                visited[i][j] = False
                for di, dj in adj:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < N and used[ni][nj] == cnt:
                        used[ni][nj] = -1
f(0, 0)

print(min_cst)
