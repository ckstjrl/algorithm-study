# M = int(input())
# S = []
# for _ in range(M):
#     calc = input().split()
#     if calc[0] == 'add':
#         S.append(calc[1])
#     elif calc[0] == 'remove':
#         if calc[1] in S:
#             S.remove(calc[1])
#     elif calc[0] == 'check':
#         if calc[1] in S:
#             print(1)
#         else:
#             print(0)
#     elif calc[0] == 'toggle':
#         if calc[1] in S:
#             S.remove(calc[1])
#         else:
#             S.append(calc[1])
#     elif calc[0] == 'all':
#         S = [str(i) for i in range(1, 21)]
#     elif calc[0] == 'empty':
#         S = []

import sys
input = sys.stdin.readline

M = int(input())
S = set()

for _ in range(M):
    calc = input().split()
    method = calc[0]

    if method == 'add':
        x = int(calc[1])
        S.add(x)
    elif method == 'remove':
        x = int(calc[1])
        S.discard(x)
    elif method == 'check':
        x = int(calc[1])
        print(1 if x in S else 0)
    elif method == 'toggle':
        x = int(calc[1])
        if x in S:
            S.remove(x)
        else:
            S.add(x)
    elif method == 'all':
        S = set(range(1, 21))
    elif method == 'empty':
        S.clear()