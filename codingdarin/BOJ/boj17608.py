# BOJ 17608. 막대기 (D1 /B2)
# https://www.acmicpc.net/problem/17608
import sys
input = lambda: sys.stdin.readline().rstrip()


n = int(input())

#스택으로 풀이, 첫 값은 미리 넣어주기
stack = [int(input())]

# 새 입력줄에 대하여 기존 보이는 막대들보다 작은지 검사
for i in range(1, n):
    x = int(input())
    
    # 크면 작은 것들은 다 뺌
    while stack and stack[-1] <= x:
        stack.pop()
    
    # 작으면 집어넣기
    else:
        stack.append(x)

print(len(stack))

