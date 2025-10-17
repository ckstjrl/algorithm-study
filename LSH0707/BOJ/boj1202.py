import sys
input = sys.stdin.readline
import heapq
N, K = map(int, input().split())
arr = []
for _ in range(N):
    a, b = map(int, input().split())  # (무게, 가격)
    arr.append((a, b))
heapq.heapify(arr)  # 무게 기준 힙큐
bag = []
for _ in range(K):
    x = int(input())
    bag.append(x)
bag.sort()  # 가방 무게 기준 오름차순
ans = 0
jewel = []  # 가방에 담을 수 있는 보석 대기줄
for i in bag:  # 용량 가장 작은 가방부터 순회
    while arr and arr[0][0] <= i:  # 보석이 있고, 그 보석무게가 가방용량보다 작거나 같은경우
        a, b = heapq.heappop(arr)  # pop하고
        heapq.heappush(jewel, -b)  # 보석 대기줄에 push(최대힙)
    if jewel:  # 대기줄에 보석이 있으면
        ans = ans + (-heapq.heappop(jewel))
        # 담을 수 있는 보석 중 가장 무게가 큰 보석 대기줄에서 pop하고 ans에 더하기
print(ans)