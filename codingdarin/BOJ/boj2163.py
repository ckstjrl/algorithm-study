# boj 2163. 초콜릿 자르기 (D1, B1)

import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())

# 초콜릿을 모두 1x1로 자르기 위한 최소 자르기 횟수
result = n * m - 1
print(result)
