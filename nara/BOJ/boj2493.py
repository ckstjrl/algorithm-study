import sys
input = sys.stdin.readline

N = int(input())
tower = list(map(int, input().split()))
result = [0] * N
stack = []

for i in range(N):
    tmp = tower[i]
    while stack and tower[stack[-1]] < tmp:
        stack.pop()
    if stack:
        result[i] = stack[-1] + 1
    stack.append(i)

print(*result)