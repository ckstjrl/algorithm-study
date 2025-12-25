# BOJ2504(D3): 괄호의 값
import sys

s = sys.stdin.readline().rstrip()

stack = []
temp = 1
answer = 0

for i in range(len(s)):
    char = s[i]

    if char == '(':
        stack.append(char)
        temp *= 2

    elif char == '[':
        stack.append(char)
        temp *= 3

    elif char == ')':
        if not stack or stack[-1] != '(':
            answer = 0
            break

        if s[i-1] == '(':
            answer += temp

        stack.pop()
        temp //= 2

    elif char == ']':
        if not stack or stack[-1] != '[':
            answer = 0
            break

        if s[i-1] == '[':
            answer += temp

        stack.pop()
        temp //= 3

if stack:
    print(0)
else:
    print(answer)