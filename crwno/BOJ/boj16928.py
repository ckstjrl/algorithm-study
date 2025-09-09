# N, M = map(int, input().split())
# up_lad = [list(map(int, input().split())) for _ in range(N)]
# dwn_lad = [list(map(int, input().split())) for _ in range(M)]
# board = [0] * 106
#
# for i in range(N):
#     board[up_lad[i][0]] = up_lad[i][1]
# for i in range(M):
#     board[dwn_lad[i][0]] = -1
# 그리디
# position = 1
# cnt = 0
# while position < 100:
#     s = 0
#     for i in range(1, 7):
#         if 0 < board[position + i] and s < board[position + i]:
#             s = board[position + i]
#
#     for i in range(1, 7):
#         if s < position + i:
#             s = position + i
#
#     position = s
#     cnt += 1
#
# print(cnt)

# 런타임에러라니
# def dice(s, k):
#     global position, cnt
#     position = s
#     while position <= k:
#         s = 0
#         for i in range(1, 7):
#             if 0 < board[position + i] and s < board[position + i]:
#                 s = board[position + i]
#
#         for i in range(1, 7):
#             if s < position + i:
#                 s = position + i
#
#         position = s
#         cnt += 1
#     position = jump[mx_idx] + stack[mx_idx]
# stack = []
# jump = []
# for i in range(len(board)):
#     if board[i] != 0 and board[i] - i > 0:
#         jump.append((board[i]) - i)
#         stack.append(i)
#     elif board[i] != 0 and board[i] - i < 0:
#         board[i] = -1
#
# mx = 0
# mx_idx = -1
# for i in range(len(jump)):
#     if mx < jump[i]:
#         mx = jump[i]
#         mx_idx = i
#
# cnt = 0
# dice(1, stack[mx_idx])
# if position < jump[i] and mx < jump[i]:
#     for i in range(len(jump)):
#         mx = jump[i]
#         mx_idx = i
#     dice(position, stack[mx_idx])
# dice(position, 100)
# print(cnt)

# 뱀 무시하면 안되는 예외가 있네
# N, M = map(int, input().split())
# up_lad = [list(map(int, input().split())) for _ in range(N)]
# dwn_lad = [list(map(int, input().split())) for _ in range(M)]
# board = [0] * 106
#
# for i in range(N):
#     board[up_lad[i][0]] = up_lad[i][1]
# for i in range(M):
#     board[dwn_lad[i][0]] = -1
#
# stack = []
# p_stack = []
# cnt_stack = []
# cnt = 0
# def dice(s):
#     global cnt
#     for i in range(6, 0, -1):
#         if board[s + i] != -1 and board[s + i] == 0:
#             stack.append(s + i)
#             break
#     for i in range(1, 7):
#         if board[s + i] != -1 and board[s + i] != 0:
#             stack.append(board[s + i])
#
# pos = 1
# while pos < 100:
#
#     cnt += 1
#     dice(pos)
#
#     if len(stack) == 1:
#         pos = stack.pop()
#         stack = []
#     else:
#         pos = stack.pop()
#         for i in range(len(stack)):
#             p_stack.append(stack[i])
#             cnt_stack.append(cnt)
#         stack = []
# mn_cnt = cnt
# while p_stack:
#     pos = p_stack.pop()
#     cnt = cnt_stack.pop()
#     while pos < 100:
#
#         cnt += 1
#         dice(pos)
#
#         if len(stack) == 1:
#             pos = stack.pop()
#             stack = []
#         else:
#             pos = stack.pop()
#             for i in range(len(stack)):
#                 p_stack.append(stack[i])
#                 cnt_stack.append(cnt)
#             stack = []
#
#     if mn_cnt > cnt:
#         mn_cnt = cnt
#
# print(mn_cnt)

from collections import deque


def bfs(ladders, snakes):

    move = {**ladders, **snakes}

    visited = [False] * 101
    q = deque([(1, 0)])
    visited[1] = True

    while q:
        pos, cnt = q.popleft()
        if pos == 100:
            return cnt

        for dice in range(1, 7):
            nxt = pos + dice
            if nxt > 100:
                continue

            if nxt in move:
                nxt = move[nxt]
            if not visited[nxt]:
                visited[nxt] = True
                q.append((nxt, cnt + 1))



N, M = map(int, input().split())
ladders = {}
snakes = {}

for _ in range(N):
    x, y = map(int, input().split())
    ladders[x] = y
for _ in range(M):
    u, v = map(int, input().split())
    snakes[u] = v

print(bfs(ladders, snakes))


