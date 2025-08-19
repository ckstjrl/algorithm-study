# 10773. 제로

import sys
input = sys.stdin.readline

T = int(input().strip())
stack = []
for _ in range(T):
    n = int(input().strip())

    # 입력이 0이 아니면 append
    if n != 0:
        stack.append(n)
    
    # 입력이 0이면 가장 마지막으로 append한 요소를 제거
    else:
        stack.pop()

print(sum(stack))