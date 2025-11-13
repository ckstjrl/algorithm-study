import heapq

N = int(input())
heap = []

for _ in range(N):
    nums = list(map(int, input().split()))
    for num in nums:
        if len(heap) < N:
            heapq.heappush(heap, num)
        else:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)

print(heap[0])