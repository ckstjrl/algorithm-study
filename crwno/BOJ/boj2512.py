# N = int(input())
# budget = list(map(int, input().split()))
# M = int(input())
#
# # sum = 0
# ans = 0
# k = M // N
# for i in budget:
#     sum += i
# if sum <= M:
#     print(max(budget))
# else:
#     while M - ans > 0:
#         k += 1
#         ans = 0
#         for i in budget:
#             if i < k:
#                 ans += i
#             else:
#                 ans += k
#     else:
#         print(k - 1)

# sum = 0
# ans = 0
# k = M // N
# h = 0
# for i in budget:
#     sum += i
# if sum <= M:
#     print(max(budget))
# else:
#     while (M - ans) // N > 0:
#         k += h
#         ans = 0
#         for i in budget:
#             if i < k:
#                 ans += i
#             else:
#                 ans += k
#         h = (M - ans) // N
#
# while M - ans > 0:
#     k += 1
#     ans = 0
#     for i in budget:
#         if i < k:
#             ans += i
#         else:
#             ans += k
# else:
#     print(k - 1)

N = int(input())
budget = list(map(int, input().split()))
M = int(input())

sum1 = sum(budget)
if sum1 <= M:
    print(max(budget))
else:
    low, high = 0, M
    result = 0

    while low <= high:
        mid = (low + high) // 2
        total = 0

        for i in budget:
            total += min(i, mid)

        if total <= M:
            result = mid
            low = mid + 1
        else:
            high = mid - 1

    print(result)