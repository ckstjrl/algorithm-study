# 2812. 크게 만들기
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
num = list(input().rstrip())

stack = []  # 숫자를 만들어 담을 스택

for n in num:
    # 앞자리에 더 작은 숫자가 있으면 제거
    while K and stack and stack[-1] < n:
        stack.pop()
        K -= 1
    stack.append(n)

# 기존 숫자를 끝까지 탐색했는데도 K가 아직 남았다면
# 이제는 내림차순으로 정렬된 상태이므로 뒤에서 잘라내는 게 최선
if K:
    stack = stack[:-K]

print(''.join(stack))