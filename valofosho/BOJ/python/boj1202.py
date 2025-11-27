"""
BOJ1202 - 보석 도둑

문제 정의
1. 보석점에는 N개의 보석, 보석의 무게 Mi, 가격 Vi
2. 가방은 총 K개, 가방에 담을 수 있는 최대 무게는 Ci
3. 담을 수 있는 보석의 최대 가격을 구하라

로직 생각
가방에 물건을 담는 유형의 문제
생각해야 될 지점은 크게 2가지
1. 가방의 최대 무게는 동일하지 않다.
2. 보석은 무게와 가격 모두를 고려해서 담아야 한다.
    -> 담을 수 있는 아이 중에 가장 비싼 애를 담아야 한다.
    -> 다만, 보석의 무게가 1인 애가 비싸다면 담을 수 있는 가장 작은 가방에 담는 것이 효율적
    -> 보석의 무게를 견딜 수 있는 가방 중에 가장 작은 가방에 우선순위 큐에서 애를 빼서 넣어주는 형식

추가 사항
우선순위 큐를 활용하려면 어떤 정보를 최우선으로 활용할 지에 대한 로직을 세워야 함
-> sorting을 걸 때, 비싸면서 가벼운 돌 우선?
-> 가방 리스트의 경우 오름차순으로 sorting
-> 우선순위 큐의 경우 가격 내림, 무게 오름 순으로 정리


로직 정의
로직 1번 (시간초과)
1. 우선순위 큐를 활용해서 보석의 무게, 가격을 담아준다.
    -> 보석 무게(asc), 보석 가격(desc)로 sort
2. 가방 리스트를 asc 로 sort
3. 가방 리스트를 순회하면서 하나하나 보석을 담는다.

로직 2번 (통과)
1. 보석의 무게, 가격을 리스트에 담아 보석 무게(asc), 보석 가격(desc) 로 정렬
2. 가방 무게별로 asc로 정렬
3. 가방별로 순회하면서 보석을 담을 최대 힙을 선언 후, 무게가 넘치지 않는 선에서 heappush
4. 힙이 비어있지 않다면 보석을 하나 꺼내고 그 값을 total에 더해준다.
    -> max heap이므로 -total로 출력

"""

import heapq
import sys
input = sys.stdin.readline

N, K = map(int,input().split())
jewels = []
# pq에 보석 무게, 가격 담기
for _ in range(N):
    w, p = map(int,input().split())
    jewels.append((w,p))

# 가방 리스트에 담기
bags= []
for _ in range(K):
    bags.append(int(input().strip()))

bags.sort()
# 무게는 asc, 가격은 desc
jewels.sort(key = lambda x: (x[0], -x[1]))

pq = []
i = 0
total = 0
for bag in bags:
    # bag이 오름차순이므로 필터링 무게만 견디면 pq를 초기화하지 않아도 된다.
    while i < N and bag >= jewels[i][0]:
        heapq.heappush(pq, -jewels[i][1])
        i += 1
    if pq:
        total += heapq.heappop(pq)

print(-total)



# 1차 제출 코드 -> 시간초과
# import heapq
# import sys
# input = sys.stdin.readline

# N, K = map(int,input().split())
# pq = []
# # pq에 보석 무게, 가격 담기
# for _ in range(N):
#     w, p = map(int,input().split())
#     heapq.heappush(pq, (p,w))

# # 가방 리스트에 담기
# bags= []
# for _ in range(K):
#     bags.append(int(input().strip()))

# bags.sort()
# pq.sort(key = lambda x: (x[0], -x[1]), reverse=True)

# total = 0

# for bag in bags:
#     for i in range(len(pq)):
#         jewel = pq[i]
#         if jewel[1] <= bag:
#             total += jewel[0]
#             heapq.heappop(pq,i)
#             break
#         else:
#             continue
# print(total)

