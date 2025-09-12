# BOJ1927. 최소 힙

import sys
import heapq

N = int(input())

heap = []
for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if not heap:
            ans = 0
        else:
            ans = heapq.heappop(heap)
    else:
        ans = heapq.heappush(heap, x)

    if ans == None:
        continue
    else:
        print(ans)