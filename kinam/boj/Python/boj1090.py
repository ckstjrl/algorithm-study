'''boj1090 - 체커
N개의 체커가 엄청 큰 보드 위에 있다. i번 체커는 (xi, yi)에 있다. 같은 칸에 여러 체커가 있을 수도 있다. 
체커를 한 번 움직이는 것은 그 체커를 위, 왼쪽, 오른쪽, 아래 중의 한 방향으로 한 칸 움직이는 것이다.

첫째 줄에 N이 주어진다. N은 50보다 작거나 같은 자연수이다. 
둘째 줄부터 N개의 줄에 각 체커의 x좌표와 y좌표가 주어진다. 
이 값은 1,000,000보다 작거나 같은 자연수이다.

첫째 줄에 수 N개를 출력한다. 
k번째 수는 적어도 k개의 체커가 같은 칸에 모이도록 체커를 이동해야 하는 최소 횟수이다.
'''

# 최소 횟수? -> 다익스트라?
# 체커를 중앙으로 모이게 하면 될듯
# 중앙 = x y 좌표 합의 평균? 중앙값?
# dist에 힙을 이용해서 저장해두기?

# k =2 : 2개의 체커 같은 칸? N개중 2개의 체커 사이 거리가 가장 짧아야함...
# k = 3 : 3개 체커 사이 거리가 가장 짧아야함.... -> 3개 체커가 가장 적게 움직이도록 -> 평균 or 중앙값 구해야할듯
# k = 4 : 반복 

'''
평균 / 중앙값 
if k = 3 , k1 = 1, k2 = 4, k3 = 12

i) 평균
(1 + 4 + 12) / 3 = 17 / 3 = 5.67 ... 평균
거리의 합 = (5.67 - 1) + (5.67 - 4) + (12 - 5.67) = 12.67

ii) 중앙값
4... 중앙값
거리의 합 = (4 - 1) + (4 - 4) + (12 - 4) = 11

중앙값으로 고고혓

중앙값을 구하고 각 지점까지의 거리 구해서 리스트에 넣고 sort해서 k번째까지 더하고
최소이동 배열에 최솟값 갱신해가며 넣기
'''

import sys
input = sys.stdin.readline
from heapq import heappop, heappush

N = int(input().strip())
checker = []
x_list = []
y_list = []
for _ in range(N):
    y, x = map(int, input().split())
    checker.append((x, y))
    x_list.append(x)
    y_list.append(y)

ans = [float('inf')] * N

for y in y_list:
    for x in x_list: # 중앙값은 입력받은 x 좌표중 하나이고, 입력받은 y좌표중 하나임. 완탐 돌리기
        distances = []
        for cx, cy in checker:
            dist = abs(cx - x) + abs(cy - y) #cx cy에 있는 체커가 중앙값(x y)으로 이동하는데 이동하는 칸 수
            distances.append(dist)

        distances.sort() # 정렬해서 k번째 까지의 합 : k개의 체커가 이동하는 최소 횟수

        cost_sum = 0
        for k in range(N):
            cost_sum += distances[k]
            ans[k] = min(ans[k], cost_sum) # 더 최소 횟수로 이동하면 최소 횟수 갱신

print(*ans)