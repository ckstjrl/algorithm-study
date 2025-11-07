"""
BOJ1655 - 가운데를 말해요

문제 정의
1. 총 숫자의 개수 N개를 먼저 입력
2. 입력된 N 만큼 숫자를 인풋으로 제공
3. 숫자가 입력될 때 마다 전체 입력에서의 중앙값을 출력
-> 만약 입력된 숫자들의 개수가 짝수인 경우 중앙값 2개 중 더 작은 값을 반환

로직 생각
1. 단순하게 중앙값을 정렬하며 찾는 경우는 시간 초과
2. 정렬을 가장 빠르게 할 수 있는 방법은 heap 자료구조를 활용
3. 하나의 힙에서 중앙값을 찾을 수 있는 방법은 X
4. 두 개의 힙을 함께 활용하면 만들 수 있다

로직 정의
1. max heap과 min heap을 나란히 놓으면 좌-> 우로 이어지는 정렬 리스트가 만들어진다

"""

import sys
import heapq
input = sys.stdin.readline

N = int(input().strip())
# 어차피 첫 값은 이미 그 자체로 mid
mid = int(input().strip())
print(mid)
# left는 max, right는 min 
left, right = [], []
heapq.heappush(left, -mid)

for i in range(2, N+1):
    # 값을 받으면
    num = int(input().strip())
    # 왼쪽이 길 때만 오른쪽에 heappush
    if len(left) > len(right):
        # 들어갈 값이 left의 max보다 작은 경우
        max_cur = -left[0]
        if max_cur > num:
            cur = heapq.heappop(left)
            heapq.heappush(right, -cur)
            heapq.heappush(left, -num)
        # 들어갈 값이 left의 max보다 큰 경우
        else:
            heapq.heappush(right, num)    
    else:
        min_cur = right[0]
        if min_cur < num:
            cur = heapq.heappop(right)
            heapq.heappush(left, -cur)
            heapq.heappush(right, num)
        else:
            heapq.heappush(left, -num)
    print(-left[0])