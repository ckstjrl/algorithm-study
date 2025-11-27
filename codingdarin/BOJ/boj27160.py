# BOJ 27160. 할리갈리
# https://www.acmicpc.net/problem/27160



# -----------------------------2회차 풀이

import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict

pair = defaultdict(int)

for _ in range(int(input())):
    fruit, cnt = input().split()
    pair[fruit] += int(cnt)

print('YES' if 5 in pair.values() else 'NO')


# # -----------------------------1회차 풀이
# import sys
# input = lambda: sys.stdin.readline().rstrip()

# ans = 'NO'
# pair = {
#         'STRAWBERRY': 0,
#         'BANANA': 0, 
#         'LIME': 0, 
#         'PLUM':0
#         }

# n = int(input())
# for i in range(n):
#     fruit, cnt = input().split()
#     pair[fruit] += int(cnt)

# for k, v in pair.items():
#     if v == 5:
#         ans = 'YES'
#         break

# print(ans)