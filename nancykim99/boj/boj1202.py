'''
BOJ1202 / D3): 보석 도둑

해결 방법 : 
시도 1. 그냥 그리디로 풀었더니 계속 에러. 
시도 2. 보석 : 작은 순, 가방 : 작은 순으로 sort.
큐에 일단 가방보다 더 작은 보석 넣고, 거기서 가장 큰것만 빼기 (maxheap).  -> max 구할때는 음수로 

* max heap 까먹어서 swea 보면서 풀었다.
'''

from heapq import heappop, heappush

N, K = map(int, input().split())
jewelry = []
bag = []

for _ in range(N):
    M, V = map(int, input().split())
    jewelry.append((M, V))

jewelry.sort()

for _ in range(K):
    n = int(input())
    bag.append(n)

bag.sort()

stealed = 0
smaller_jew = [] # 가방보다 더 작은 보석 줍줍
for i in range(K):
    while jewelry:
        if bag[i] >= jewelry[0][0]:
            heappush(smaller_jew, -jewelry[0][1]) # 큐에 거꾸로 넣기 (maxheap이니까)
            heappop(jewelry) # 보석함에서 훔침~
        else:
            break # 더이상 보석이 없음 그만~
    if smaller_jew: # 줍줍한 보석 중에서
        stealed += -heappop(smaller_jew) # 큰거만 가방에 남기기
    else:
        if not jewelry: 
            break


print(stealed)