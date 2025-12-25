'''
BOJ1781 : 컵라면 (S2)

해결 방법 :
1. sort를 통해 데드라인이 빠른 문제부터 처리하기
2. 이전까지 푼 문제 중 컵라면 수가 가장 적었던 문제와 현재 문제를 비교하기
3. 현재 문제의 컵라면 수가 더 많다면 이전에 푼 문제를 해당 문제로 heapq를 사용해서 대체하기 
'''

import heapq
n = int(input())
array = []
for _ in range(n):
    deadline, cupnoodle = map(int, input().split())
    array.append((deadline, cupnoodle))

array.sort()

queue = []

for i in array:
    heapq.heappush(queue, i[1])
    if i[0] < len(queue):
        heapq.heappop(queue)
    
print(sum(queue))
