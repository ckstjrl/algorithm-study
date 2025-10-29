'''
BOJ1149 : RGB거리

해결 방법 : 
각각 칠했을 때의 최소 누적 비용을 계산해서 넣고, 최소비용 중 가장 작은 값 구하기
'''

import sys
input = sys.stdin.readline 


N = int(input()) 

cost = []
for _ in range(N):
    cost.append(list(map(int, input().split())))

for i in range(1, N):
    cost[i][0] += min(cost[i-1][1], cost[i-1][2]) # Red
    cost[i][1] += min(cost[i-1][0], cost[i-1][2]) # Green
    cost[i][2] += min(cost[i-1][0], cost[i-1][1]) # Blue

print(min(cost[N-1]))