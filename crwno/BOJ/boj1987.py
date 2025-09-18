# 또간초과

# R, C = map(int, input().split())
# board = [str(input()) for _ in range(R)]
# visited = [[False] * C for _ in range(R)]
#
# visited[0][0] = True
# stack = [board[0][0]]
# mx_cnt = 1
# def f(x, y, cnt):
#     global stack, mx_cnt
#     if mx_cnt < cnt:
#         mx_cnt = cnt
#     for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
#         nx, ny = x + dx, y + dy
#         if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and board[nx][ny] not in stack:
#             visited[nx][ny] = True
#             stack.append(board[nx][ny])
#             f(nx, ny, cnt + 1)
#             visited[nx][ny] = False
#             stack.pop()
#
# f(0, 0, 1)
# print(mx_cnt)

# visited는 필요없네

# R, C = map(int, input().split())
# board = [str(input()) for _ in range(R)]
#
# stack = [board[0][0]]
# mx_cnt = 1
# def f(x, y, cnt):
#     global stack, mx_cnt
#     if mx_cnt < cnt:
#         mx_cnt = cnt
#     for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
#         nx, ny = x + dx, y + dy
#         if 0 <= nx < R and 0 <= ny < C and board[nx][ny] not in stack:
#             stack.append(board[nx][ny])
#             f(nx, ny, cnt + 1)
#             stack.pop()
#
# f(0, 0, 1)
# print(mx_cnt)

# 멤ㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁ모리초과
# from collections import deque
#
# R, C = map(int, input().split())
# board = [str(input()) for _ in range(R)]
#
# q = deque()
# q.append((0, 0, board[0][0]))
# cnt = 1
#
# while q:
#     x, y, used = q.popleft()
#     if cnt < len(used):
#         cnt = len(used)
#     for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
#         nx, ny = x + dx, y + dy
#         if 0 <= nx < R and 0 <= ny < C and board[nx][ny] not in used:
#             q.append((nx, ny, used + board[nx][ny]))
#
# print(cnt)

# 왜 어째서 파이썬은 안되고 pypy는 되는거야
R, C = map(int, input().split())
board = [input().strip() for _ in range(R)]
start_bit = 1 << (ord(board[0][0]) - ord('A'))
visited = [[False] * C for _ in range(R)]
mx_cnt = 1


def f(x, y, bitmask, cnt):
    global mx_cnt
    if cnt > mx_cnt:
        mx_cnt = cnt
    visited[x][y] = True
    for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]:
            next_bit = 1 << (ord(board[nx][ny]) - ord('A'))
            if not (bitmask & next_bit):
                f(nx, ny, bitmask | next_bit, cnt + 1)
    visited[x][y] = False
f(0, 0, start_bit, 1)

print(mx_cnt)



