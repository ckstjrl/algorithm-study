# BOJ 1919. 애너그램 만들기 (D1 / B2):
# https://www.acmicpc.net/problem/1919
# 두 문자열이 주어졌을 때, 한 문자열을 다른 문자열의 애너그램으로 만들기 위해
# 삭제해야 하는 문자 개수의 최솟값을 구하는 문제

import sys
input = lambda: sys.stdin.readline().rstrip()

fir = input()
sec = input()

# 알파벳 개수 세기
cnt = [0] * 26

# 첫 번째 문자열에서 개수 더하기
for c in fir:
    cnt[ord(c) - ord('a')] += 1

# 두 번째 문자열에서 개수 빼기
for c in sec:
    cnt[ord(c) - ord('a')] -= 1
    
# 절댓값의 합 계산
print(sum(abs(x) for x in cnt))