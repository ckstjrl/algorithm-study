# BOJ 1927. 최소 힙 (D2/S2)

#------------------------------------------------1회차 풀이
import sys, heapq

input = sys.stdin.readline

N = int(input())
min_heap = []

for _ in range(N):
    x = int(input())
    if x>0:
        heapq.heappush(min_heap, x)
    elif not min_heap:
        print("0")
    else:
        print(heapq.heappop(min_heap))
    