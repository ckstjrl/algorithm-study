# BOJ 1673. 치킨 쿠폰 (D1 / B2)
import sys
input = sys.stdin.readlines # 한 번에 받자

txt = input()

# 각 줄마다 처리
for line in txt:
    n, k = map(int, line.split())

    print(n + (n-1) // (k-1))