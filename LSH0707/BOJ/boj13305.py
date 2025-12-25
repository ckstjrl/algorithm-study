import sys
input = sys.stdin.readline
N = int(input())
r = list(map(int, input().split()))  # 거리
g = list(map(int, input().split()))  # 가격
cost = 0  # 비용
min_g = float('inf')  # 기름 최솟값
for i in range(N - 1):
    if g[i] < min_g:  # 기름 최솟값 기록
        min_g = g[i]
    cost = cost + min_g * r[i]  # +(기름 최솟값 * 거리)

print(cost)
