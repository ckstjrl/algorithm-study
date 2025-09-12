# BOJ1863: 스카이라인 쉬운거
import sys
input = sys.stdin.readline

n = int(input())
stack = [0] # 숫자비교를 위해 0 넣음
cnt = 0

for _ in range(n):
    x, y = map(int, input().split())

    if stack[-1] < y: # top이 y보다 작다면 push(y)
        stack.append(y)

    elif stack[-1] > y: # top이 y보다 크다면 
        while stack[-1] > y: # y보다 큰 숫자는 차례로 모두 pop()
            stack.pop()
            cnt += 1
        if stack[-1] != y:
            stack.append(y)

while stack[-1] > 0: # 끝에는 모든 stack이 남지 않도록 pop()
    stack.pop()
    cnt += 1

print(cnt)
