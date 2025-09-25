# BOJ1543(D2): 문서 검색
import sys
input = lambda: sys.stdin.readline().rstrip()

sentence = input()
S = input()
top = 0
len_S = len(S)

ans = 0

while top <= len(sentence) - len_S:
    if sentence[top:top + len_S] == S:
        ans += 1
        top += len_S
    else:
        top += 1

print(ans)

# 허무했던 빠르고 효율적인 답...
# print(input().count(input()))