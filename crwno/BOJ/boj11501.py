import heapq

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    price = list(map(int, input().split()))
    heap = []
    for i in range(N):
        heap.append((-price[i], i))
    heapq.heapify(heap)

    res = 0
    pt = -1


    def f(value, idx):
        global res, pt
        for x in range(pt + 1, idx):
            res += value - price[x]
        pt = idx

    while heap:
        value, idx = heapq.heappop(heap)
        if pt < idx:
            f(-value, idx)

    print(res)