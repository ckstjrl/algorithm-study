'''
BOJ2812 / D3): 크게 만들기

해결 방법 : 
1. for문 돌면서 같거나 크면, stack에 넣기? -> 그러면 뒤에 K가 남았는데, 리스트가 딱 맞게 남았을 경우, 넘기는 방법이 안 됨
2. stack으로 pop한건 다 ans에 넣고, 그 나머지 중에 max값들만 남은 숫자만큼 넣기. 지우는거라 순서는 동일해야함...? -> 순서가 뒤죽박죽 됨
3. 스택에 숫자를 하나씩 넣으면서, 스택의 마지막 숫자가 현재 숫자보다 작으면, 마지막 숫자를 제거하고, 제거 횟수를 감소한 다음, 현재 숫자를 스택에 추가
    - 왼쪽에서부터 큰 숫자를 남겨놓는 방법
    - 만약 제거할 횟수가 남아있다면, 숫자의 길이를 채우기 위해, N-K만큼 뒤에서부터 꺼내서 숫자로 넣기
'''

import sys

N, K = map(int, sys.stdin.readline().split())
num_str = sys.stdin.readline().strip()

stack = []
removals = K # K가 바뀌지 않게 임시 숫자

for digit in num_str:
    # 1. 스택이 비어있지 않고,
    # 2. 아직 제거할 횟수(removals)가 남아있고,
    # 3. 스택의 마지막 숫자(stack[-1])가 현재 숫자(digit)보다 작으면
    while stack and removals > 0 and stack[-1] < digit:
        stack.pop()
        removals -= 1
    stack.append(digit)

# 숫자의 길이를 채우기 위해, N-K만큼 뒤에서부터 꺼내서 숫자로 넣기
final_result = "".join(stack[:N-K])

print(final_result)