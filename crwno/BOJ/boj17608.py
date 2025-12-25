# N = int(input())
#
#
# height = [int(input()) for _ in range(N)]
#
# cnt = 0
# i = N - 1
# mx = 0
# while i >= 0:
#     if mx < height[i]:
#         mx = height[i]
#         cnt += 1
#     i -= 1
# print(cnt)

import sys
input = sys.stdin.readline

N = int(input())
height = [int(input()) for _ in range(N)]

cnt = 0
i = N - 1
mx = 0

while i >= 0:
    if mx < height[i]:
        mx = height[i]
        cnt += 1
    i -= 1

print(cnt)
