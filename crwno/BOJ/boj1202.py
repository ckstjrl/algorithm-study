# N, K = map(int, input().split())
# jew = [list(map(int, input().split())) for _ in range(N)]
# bag = []
# for _ in range(K):
#     bag.append(int(input()))
#
# jew.sort(key=lambda x: x[1], reverse=True)
# bag.sort()
#
# cnt = 0
# i = 0
# j = 0
# cost = 0
# used = [False] * K
# while cnt != K and i < N:
#     if jew[i][0] <= bag[j] and not used[j]:
#         cost += jew[i][1]
#         cnt += 1
#         i += 1
#         used[j] = True
#     else:
#         j += 1
#     if j == K:
#         i += 1
#         j = 0
# print(cost)
#
# import heapq
#
# N, K = map(int, input().split())
# jew = [list(map(int, input().split())) for _ in range(N)]
# jews = [(-v, w) for w, v in jew]
# bag = []
# heapq.heapify(bag)
# heapq.heapify(jews)
#
#
# for _ in range(K):
#     heapq.heappush(bag, int(input()))
#
#
# def f(mx_v, cnt):
#     if cnt == K:
#         print(mx_v)
#         return
#     bag_w = heapq.heappop(bag)
#     stack = []
#     while jews:
#         jews_v, jews_w = heapq.heappop(jews)
#         if bag_w >= jews_w:
#             f(mx_v - jews_v, cnt + 1)
#             for i in stack:
#                 heapq.heappush(jews, i)
#             return
#         else:
#             stack.append((jews_v, jews_w))
#     else:
#         for i in stack:
#             heapq.heappush(jews, i)
#
# f(0, 0)

# import heapq
#
# N, K = map(int, input().split())
# jew = [list(map(int, input().split())) for _ in range(N)]
# jews = [(-v, w) for w, v in jew]
# bag = []
# heapq.heapify(bag)
# heapq.heapify(jews)
#
#
# for _ in range(K):
#     heapq.heappush(bag, int(input()))
#
#
# def f(mx_v, cnt):
#     if cnt == K:
#         print(mx_v)
#         return
#
#     jews_v, jews_w = heapq.heappop(jews)
#     stack = []
#     while bag:
#         bag_w = heapq.heappop(bag)
#         if bag_w >= jews_w:
#             for i in stack:
#                 heapq.heappush(bag, i)
#             f(mx_v - jews_v, cnt + 1)
#             break
#         else:
#             stack.append(bag_w)
#     else:
#         for i in stack:
#             heapq.heappush(bag, i)
#         f(mx_v, cnt)
#
# f(0, 0)


import heapq

N, K = map(int, input().split())
jewels = [tuple(map(int, input().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]

jewels.sort()
bags.sort()
heap = []
ans = 0
i = 0

for bag in bags:

    while i < N and jewels[i][0] <= bag:
        heapq.heappush(heap, -jewels[i][1])
        i += 1
    if heap:
        ans -= heapq.heappop(heap)

print(ans)