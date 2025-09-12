# N = int(input())
# def f(x):
#
#     if x == 0:
#         return 1
#     return 6*x + f(x - 1)
#
# n = 0
#
# while True:
#
#     if N <= f(n):
#         print(n + 1)
#         break
#     n += 1
# 시간복잡도: O(N)
# f(x)를 호출시 깊이 x까지 재귀 호출, N이 커질수록 반복 호출 증가.

# 시간초과늪이야
# N = int(input())
#
# if N == 1:
#     print(1)
#
# layer = 1
# k = 1
# while True:
#     if 1 < N <= k + (6 * layer):
#         print(layer + 1)
#         break
#     else:
#         k += (6 * layer)
#         layer += 1
# 시간복잡도: O(√N)
# layer가 1씩 증가 6*layer씩 누적, 반복 횟수√N 수준
N = int(input())

if N == 1:
    print(1)
else:
    layer = 0
    k = 1
    while k < N:
        layer += 1
        k += 6 * layer
    print(layer + 1)
# 시간복잡도: O(√N)
# k가 6n씩 증가, k >= N이 될 때까지 반복 횟수 √N 수준.
# 반복에 if문이 없어서 조건 검사를 안해도됨. 연산량 적음.