# BOJ7662(D3): 이중 우선순위 큐
from heapq import heappush, heappop
import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k = int(input())
    min_heap = []
    max_heap = []
    visited = [False] * k

    for i in range(k):
        char, n = input().split()
        n = int(n)
        
        if char == 'I':
            heappush(min_heap, (n, i))
            heappush(max_heap, (-n, i))

        elif char == 'D':
            if n == -1:
                while min_heap and visited[min_heap[0][1]]:
                    heappop(min_heap)
                if min_heap:
                    _, idx = heappop(min_heap)
                    visited[idx] = True
            
            elif n == 1:
                while max_heap and visited[max_heap[0][1]]:
                    heappop(max_heap)
                if max_heap:
                    _, idx = heappop(max_heap)
                    visited[idx] = True
    
    while min_heap and visited[min_heap[0][1]]:
        heappop(min_heap)
    while max_heap and visited[max_heap[0][1]]:
        heappop(max_heap)
    
    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print("EMPTY")