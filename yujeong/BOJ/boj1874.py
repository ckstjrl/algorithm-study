# 1874. 스택 수열

import sys
input = sys.stdin.readline 
from collections import deque

n = int(input().strip())
nums = deque(range(1, n+1))
stack = deque()
result = deque()

'''
가능불가능 판단 전략: 
1부터 N까지 숫자 중 이번 차례에 남은 가장 작은 수를 i,
이번 차례에 입력받은, 수열을 이루는 정수를 x라 하면

i가 x보다 작으면 스택에 push
i가 x와 같으면 push 하고 바로 pop
그 외 경우에는 스택의 top이 x면 스택으로 수열 만들기 가능, 아니면 불가능
'''

check = True
for _ in range(n):
    x = int(input().strip())

    if nums and nums[0] < x:
        while True:
            stack.append(nums.popleft())
            result.append('+')
            if not nums or nums[0] > x:
                break
        stack.pop()
        result.append('-')
    elif nums and nums[0] == x:
        result.append('+')
        result.append('-')
        nums.popleft()
    else:
        if stack[-1] == x:
            stack.pop()
            result.append('-')
        else:
            ans = 'NO'
            check = False            

if not check:
    print(ans)
else:
    for r in result:
        print(r)