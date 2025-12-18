# BOJ 1202. 보석 도둑 / D3
'''
문제
세계적인 도둑 상덕이는 보석점을 털기로 결심했다.

상덕이가 털 보석점에는 보석이 총 N개 있다. 각 보석은 무게 Mi와 가격 Vi를 가지고 있다.
상덕이는 가방을 K개 가지고 있고, 각 가방에 담을 수 있는 최대 무게는 Ci이다. 가방에는 최대 한 개의 보석만 넣을 수 있다.

상덕이가 훔칠 수 있는 보석의 최대 가격을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 K가 주어진다. (1 ≤ N, K ≤ 300,000)
다음 N개 줄에는 각 보석의 정보 Mi와 Vi가 주어진다. (0 ≤ Mi, Vi ≤ 1,000,000)
다음 K개 줄에는 가방에 담을 수 있는 최대 무게 Ci가 주어진다. (1 ≤ Ci ≤ 100,000,000)
모든 숫자는 양의 정수이다.

출력
첫째 줄에 상덕이가 훔칠 수 있는 보석 가격의 합의 최댓값을 출력한다.
'''
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

N, K = map(int, input().split())
dia = []
for _ in range(N):
    w, p = map(int, input().split())
    dia.append((w, p))

bag = []
for _ in range(K):
    w_b = int(input())
    bag.append(w_b)

# 보석 무게에 따라 오름차순 정령
dia.sort(key=lambda x: x[0])
# 가방 가능 무게로 오름차순 정렬
bag.sort()

possible = []
j = 0
total = 0
for w in bag:
    # 가방 가능 무게보다 작으면서 dia list 내부에 있는 경우 while 반복문
    while j < N and dia[j][0] <= w:
        # possible에 보석 무게 (음수) 로 넣어줌(max힙 구하기 위해) 
        heappush(possible, -dia[j][1])
        # 다음 보석확인
        j += 1
    
    # possible이 비어있지 않은 경우
    if possible:
        # max를 뽑아냄 (음수로 total에 더해줘야함)
        total += -heappop(possible)
print(total)
'''
dia = [0]*1000001
for _ in range(N):
    w, p = map(int, input().split())
    dia[w] = p
bag = []
for _ in range(K):
    w_b = int(input())
    bag.append(w_b)

total = 0
for i in range(K):
    possible = dia[:bag[i]+1]
    stool = max(possible)
    total += stool
    dia[dia.find(stool)] = 0

print(total)
아무생각없이 그냥 구현
-> 시간초과
'''

'''
보석무게, 가방 가능 무게를 오름차순으로 정리한 후
max 힙을 활용하여 문제 풀이 진행
'''
