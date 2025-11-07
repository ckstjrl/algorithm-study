"""
문제 정의
1. N 자리 숫자(첫 자리에 0은 안들어감)
2. K 개의 숫자를 지워 남은 값이 최대가 되도록

로직 생각
1. 카운터로 하나하나 없애는게 가능할까?
-> 어차피 작은 수 2132 라면 132 vs 213이라는 가정이 나올 수 없음
-> 이미 1이 먼저 지워졌을 테니까
-> 그냥 위치에 상관 없이 가장 작은 수부터 차례대로 지우는게 맞지 않을까
-> 물론 0을 가장 먼저!


2. 리스트 잘라쓰기
    - 


"""


import sys
input = sys.stdin.readline
N, K = map(int, input().split())
nums = list(map(int, input().strip()))
stack = []
for num in nums:
    while stack and K > 0 and stack[-1] < num:
        stack.pop()
        K -= 1
    stack.append(num)

if K > 0:
    stack = stack[:-K]
print(''.join(map(str, stack)))



"""
# 3번 생각
import sys
from collections import Counter, deque
input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(map(int, input().strip()))
here = nums[:K+1]
max_idx = here.index(max(here))
new = nums[max_idx:]
K -= max_idx
pin = 0
while K>0 and pin+2<=len(new):
    prev = pin
    cur = pin + 1
    next = pin + 2
    if new[prev] > new[cur] and new[cur] < new[next]:
        new.pop(cur)
        K -= 1
    pin +=1
print(new)
"""








"""
# 첫 로직 풀이
# -> 3 1 
# -> 671
# 위 예제에서 반례
import sys
from collections import Counter, deque
input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(map(int, input().strip()))
counter = Counter(nums)
cnt = 0
for i in range(10):
    if cnt == K:
        break
    while counter[i] >= 1:
        counter[i] -= 1
        cnt += 1
        if cnt == K:
            break

q = deque([])

while nums:
    cur = nums.pop()
    if counter[cur] >= 1:
        q.appendleft(str(cur))
        counter[cur] -= 1

print(''.join(q))"""


"""
# 두 번째 풀이
import sys
from collections import Counter, deque
input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(map(int, input().strip()))
here = nums[:K+1]
max_idx = here.index(max(here))
new = nums[max_idx:]
K -= max_idx
counter = Counter(new)
cnt = 0
for i in range(10):
    if cnt == K:
        break
    while counter[i] >= 1:
        counter[i] -= 1
        cnt += 1
        if cnt == K:
            break

q = deque([])

while new:
    cur = new.pop()
    if counter[cur] >= 1:
        q.appendleft(str(cur))
        counter[cur] -= 1

print(''.join(q))


"""