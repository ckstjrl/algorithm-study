# 1655. 가운데를 말해요

from heapq import heappop, heappush
import sys
input = sys.stdin.readline

N = int(input())

# --- 시간 초과로 실패: 가운데 값이 될 때까지 heappop 반복하기
# nums = []
# for i in range(1, N+1):
#     number = int(input())
#     heappush(nums, number)
#     temp = nums[:]
#     l = i//2 if i%2==0 else i//2+1
#     for _ in range(l):
#         x = heappop(temp)
#     print(x)

left = []   # 가운데 값보다 작은 수들을 저장할 우선순위 큐 (최대 힙)
right = []  # 가운데 값보다 큰 수들을 저장할 우선순위 큐 (최소 힙)

for i in range(N):
    num = int(input())  # 이번 차례에 외친 수 
    # left가 비었거나 left의 최댓값보다 작으면 left로 push
    if not left or num <= -left[0]:     
        heappush(left, -num)
    # 그 외는 right로 push
    else:       
        heappush(right, num)

    # 좌우 힙 길이 맞추기
    if len(left) > len(right) + 1:
        heappush(right, -heappop(left))
    elif len(right) > len(left):
        heappush(left, -heappop(right))

    print(-left[0])     # left의 최댓값 = 지금까지 있는 수 중 가운데 값