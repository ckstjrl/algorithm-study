import heapq

score = [int(input()) for _ in range(8)]
heap = []
for i in range(8):
    if score[i] != 0:
        heapq.heappush(heap, (score[i], i + 1))
while len(heap) > 5:
    heapq.heappop(heap)
res_s = 0
res_i = []
for i in range(5):
    sc, idx = heapq.heappop(heap)
    res_s += sc
    res_i.append(idx)
res_i.sort()
print(res_s)
for i in range(5):
    print(res_i[i], end=' ')