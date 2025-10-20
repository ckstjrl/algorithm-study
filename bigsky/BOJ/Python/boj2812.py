# BOJ2812(D3): 크게 만들기
import sys

N, K = map(int, sys.stdin.readline().split())
nums = list(sys.stdin.readline().rstrip())

stack = []
for num in nums:
    while K > 0 and stack and stack[-1] < num:
        stack.pop()
        K -= 1
    stack.append(num)

if K > 0:
    stack = stack[:-K]

print(''.join(stack))