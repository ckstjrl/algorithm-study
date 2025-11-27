# 1149. RGB거리

import sys
input = sys.stdin.readline

N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]

# dp[i]: i번째 집을 r/g/b 색으로 칠했을 때, 0~i번 집까지 칠한 비용의 최솟값
dp = [[0, 0, 0] for _ in range(N)]
dp[0] = [cost[0][0], cost[0][1], cost[0][2]]    # 0번 집 (1번 집)

# 1~N-1 범위에 대해, i번 집을 r/g/b 색으로 칠하는 최소 비용은
# i-1번 집을 i번 집 색과 다른 색으로 칠했을 때 비용의 최솟값 + i번 집을 그 색으로 칠했을 때 비용
for i in range(1, N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + cost[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + cost[i][2]

# 마지막 집의 3개 경우 중 최솟값 출력
print(min(dp[N-1]))