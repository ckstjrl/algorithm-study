# BOJ9935(D3): 문자열 폭발
import sys

s = sys.stdin.readline().rstrip()
bomb = list(sys.stdin.readline().rstrip())
m = len(bomb)
last = bomb[-1]


stack = []
for ch in s:
    stack.append(ch)
    if ch == last and len(stack) >= m:
        match = True
        for i in range(m):
            if stack[-1 - i] != bomb[-1 - i]:
                match = False
                break
        if match:
            del stack[-m:]

print(''.join(stack) if stack else 'FRULA')
