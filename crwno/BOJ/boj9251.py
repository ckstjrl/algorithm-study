# l1 = input()
# l2 = input()
# if len(l1) >= len(l2):
#     list_1 = l2
#     list_2 = l1
# else:
#     list_1 = l1
#     list_2 = l2
#
# mx_cnt = 0
# cnt = 0
# stack = [(0, 0)]
# v = []
# def f(idx_i, idx_j):
#     global mx_cnt, cnt, stack, v
#
#     if idx_i == len(list_1) or idx_j == len(list_2):
#         return
#
#     if list_1[idx_i] not in list_2[idx_j:]:
#         n_idx_i = idx_i
#         n_idx_j = idx_j
#         f(n_idx_i + 1, n_idx_j)
#     else:
#         for j in range(idx_j, len(list_2)):
#             if list_1[idx_i] == list_2[j]:
#                 if (idx_i, j) not in v:
#                     n_idx_i = idx_i
#                     n_idx_j = j
#                     stack.append((idx_i, j))
#                     v.append((idx_i, j))
#                     break
#                 else:
#                     n_idx_i = idx_i
#                     n_idx_j = j + 1
#                     break
#         cnt += 1
#
#         if mx_cnt < cnt:
#             mx_cnt = cnt
#         print(n_idx_i, n_idx_j, list_1[n_idx_i])
#         f(n_idx_i + 1, n_idx_j + 1)
#
#
#
# while stack:
#     n_list = stack.pop()
#     cnt = 0
#     f(n_list[0], n_list[1] + 1)
#     print(stack)
# print(mx_cnt)

# l1 = input()
# l2 = input()
# if len(l1) >= len(l2):
#     list_1 = l1
#     list_2 = l2
# else:
#     list_1 = l2
#     list_2 = l1
#
# mx_cnt = 0
# cnt = 0
# def f(idx_i, idx_j):
#     global mx_cnt, cnt
#
#     if idx_i == len(list_1) or idx_j == len(list_2):
#         return
#
#     if list_1[idx_i] not in list_2[idx_j:]:
#         n_idx_i = idx_i
#         n_idx_j = idx_j
#         print(n_idx_i, n_idx_j, list_1[n_idx_i], 'pass')
#         f(n_idx_i + 1, n_idx_j)
#     else:
#         for j in range(idx_j, len(list_2)):
#             if list_1[idx_i] == list_2[j]:
#                 n_idx_i = idx_i
#                 n_idx_j = j
#                 break
#         cnt += 1
#
#         if mx_cnt < cnt:
#             mx_cnt = cnt
#         print(n_idx_i, n_idx_j, list_1[n_idx_i])
#         f(n_idx_i + 1, n_idx_j + 1)
#
#
# f(0, 0)
# print(mx_cnt)
#
# mx_cnt = 0
# v = []
# v2 = [(0, 0, 0)]
# def f(idx_i, idx_j, cnt):
#     global mx_cnt, v
#     if idx_i >= len(l1) or idx_j >= len(l2):
#         if mx_cnt < cnt:
#             mx_cnt = cnt
#         return
#
#     if l1[idx_i] not in l2[idx_j:]:
#         n_idx_i = idx_i
#         n_idx_j = idx_j
#         print(n_idx_i, n_idx_j, l1[n_idx_i], cnt, 'pass')
#         f(n_idx_i + 1, n_idx_j, cnt)
#     else:
#         for j in range(idx_j, len(l2)):
#             if l1[idx_i] == l2[j] and (idx_i, j, cnt) not in v2:
#                 n_idx_i = idx_i
#                 n_idx_j = j
#                 v.append((n_idx_i, n_idx_j, cnt + 1))
#                 print(n_idx_i, n_idx_j, l1[n_idx_i], cnt + 1)
#                 f(n_idx_i + 1, n_idx_j + 1, cnt + 1)
# f(1, 0, 0)
# while len(v) >= 2:
#     print(v)
#     nl = v.pop()
#     v2.append((v[-1][0], v[-1][1], v[-1][2] - 1))
#     f(v[-1][0], v[-1][1], v[-1][2] - 1)
# print(mx_cnt)
#
# mx_cnt = 0
# cnt = 0
# v = []
# stack = []
# def f(idx_i, idx_j, cnt):
#     global mx_cnt, v
#
#     if idx_i == len(l1) and idx_j == len(l2):
#         return
#
#     if l1[idx_i] not in l2[idx_j:]:
#         n_idx_i = idx_i
#         n_idx_j = idx_j
#         print(n_idx_i, n_idx_j, l1[n_idx_i], 'pass')
#         f(n_idx_i + 1, n_idx_j, cnt)
#     else:
#         for j in range(idx_j, len(l2)):
#             if l1[idx_i] == l2[j] and (idx_i, j) not in v:
#                 n_idx_i = idx_i
#                 n_idx_j = j
#                 v.append((n_idx_i, n_idx_j))
#                 break
#
#         if mx_cnt < cnt:
#             mx_cnt = cnt
#         print(n_idx_i, n_idx_j, l1[n_idx_i])
#         f(n_idx_i + 1, n_idx_j + 1, cnt + 1)
#
#
# f(0, 0, 1)
# while v:
#     ls = v.pop()
#     f(ls[0], ls[1] + 1, cnt - 1)
#
#
#
# #
# #
# # print(mx_cnt)
# # print(v)
#
# dict = {
#     'A': 0,
#     'B': 1,
#     'C': 2,
#     'D': 3,
#     'E': 4,
#     'F': 5,
#     'G': 6,
#     'H': 7,
#     'I': 8,
#     'J': 9,
#     'K': 10,
#     'L': 11,
#     'M': 12,
#     'N': 13,
#     'O': 14,
#     'P': 15,
#     'Q': 16,
#     'R': 17,
#     'S': 18,
#     'T': 19,
#     'U': 20,
#     'V': 21,
#     'W': 22,
#     'X': 23,
#     'Y': 24,
#     'Z': 25
# }
# check = [False] * 26
# n = 0
#
# list_1 = input()
# list_2 = input()
#
# if len(list_1) >= len(list_2):
#     l1 = list_1
#     l2 = list_2
# else:
#     l1 = list_2
#     l2 = list_1
#
# for i in range(len(l1)):
#     if not check[dict[l1[i]]]:
#         check[dict[l1[i]]] = True
#
# mx_cnt = 0
# v = []
# ck = [False] * len(l2)
#
# def pair(x, y, cnt):
#     global mx_cnt
#     if x == len(l1):
#         if mx_cnt < cnt:
#             mx_cnt = cnt
#         return
#     for j in range(y, len(l2)):
#         if l1[x] not in l2[j:]:
#             pair(x + 1, y, cnt)
#         elif l1[x] == l2[j]:
#             v.append((x, j))
#             pair(x + 1, y + 1, cnt + 1)
#             break
#
# pair(0, 0, 0)
# print(v)


# 런타임에러....
# l1 = input()
# l2 = input()
#
# mx_cnt = 0
#
# def pair(x, y, cnt):
#     global mx_cnt
#
#     if x == len(l1) or y == len(l2):
#         if cnt > mx_cnt:
#             mx_cnt = cnt
#         return
#
#     if l1[x] == l2[y]:
#         pair(x + 1, y + 1, cnt + 1)
#     else:
#         pair(x + 1, y, cnt)
#         pair(x, y + 1, cnt)
#
# pair(0, 0, 0)
# print(mx_cnt)

# 글러먹었고
# dict_a = {
#     'A': 0,
#     'B': 1,
#     'C': 2,
#     'D': 3,
#     'E': 4,
#     'F': 5,
#     'G': 6,
#     'H': 7,
#     'I': 8,
#     'J': 9,
#     'K': 10,
#     'L': 11,
#     'M': 12,
#     'N': 13,
#     'O': 14,
#     'P': 15,
#     'Q': 16,
#     'R': 17,
#     'S': 18,
#     'T': 19,
#     'U': 20,
#     'V': 21,
#     'W': 22,
#     'X': 23,
#     'Y': 24,
#     'Z': 25
# }
#
# list_1 = input()
# list_2 = input()
#
# if len(list_1) >= len(list_2):
#     l1 = list_1
#     l2 = list_2
# else:
#     l1 = list_2
#     l2 = list_1
# check_i = [False] * 26
# check_j = [False] * 26
# for i in range(len(l1)):
#     if not check_i[dict_a[l1[i]]]:
#         check_i[dict_a[l1[i]]] = True
# for i in range(len(l1)):
#     if not check_j[dict_a[l1[i]]]:
#         check_j[dict_a[l1[i]]] = True
# mx_cnt = 0
# v = dict()
# def pair(x, y, cnt):
#     global mx_cnt
#
#     if cnt == 0 and not check_i[dict_a[l1[x]]]:
#         return
#     if not check_j[dict_a[l1[y]]]:
#         return
#     if (x, y, cnt) in v:
#         if v[(x, y, cnt)] >= cnt:
#             return
#     v[(x, y, cnt)] = cnt
#
#     if x == len(l1) or y == len(l2):
#         if cnt > mx_cnt:
#             mx_cnt = cnt
#         return
#     if check_i[dict_a[l2[y]]]:
#         if l1[x] == l2[y]:
#             pair(x + 1, y + 1, cnt + 1)
#         else:
#             pair(x + 1, y, cnt)
#             pair(x, y + 1, cnt)
#     else:
#         pair(x, y + 1, cnt)
#
# pair(0, 0, 0)
# print(mx_cnt)
# 따로 1안만들어도될듯
# l1 = input()
# l2 = input()
# N = len(l1)
# M = len(l2)
# dp = [[0] * (M + 1) for _ in range(N + 1)]
#
# for i in range(N):
#     for j in range(M):
#         if l1[i] == l2[j]:
#             dp[i + 1][j + 1] = 1
# for i in range(1, N + 1):
#     for j in range(1, M + 1):
#         if l1[i - 1] != l2[j - 1]:
#             dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
#         else:
#             dp[i][j] += max(dp[i - 1][j], dp[i][j - 1])
# print(dp[N][M])

l1 = input()
l2 = input()
N = len(l1)
M = len(l2)

dp = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if l1[i - 1] == l2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[N][M])