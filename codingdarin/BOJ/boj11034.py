# BOJ 11034. 캥거루 세마리2 (D1 / B3)
# https://www.acmicpc.net/problem/11034

import sys

for line in sys.stdin:
    a, b, c = map(int, line.split())
    ans = max(b - a - 1, c - b - 1)
    print(ans)