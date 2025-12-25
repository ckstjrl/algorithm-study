# BOJ 12605. 단어순서 뒤집기 (D1 /B2)
# https://www.acmicpc.net/problem/12605

import sys
input = lambda:sys.stdin.readline().rstrip()

n = int(input())

for i in range(1, n+1):
    # 단어 거꾸로 리스트
    reverse = list(input().split())[::-1]

    # 압축 풀어서 출력
    print(f"Case #{i}:", end=' ')
    print(*reverse)
