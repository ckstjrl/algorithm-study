"""
BOJ1149. RGB거리

[문제]
RGB거리에는 집이 N개 있다. 거리는 선분으로 나타낼 수 있고, 1번 집부터 N번 집이 순서대로 있다.
집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다.
각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때, 아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.

* 1번 집의 색은 2번 집의 색과 같지 않아야 한다.
* N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
* i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.

[입력]
첫째 줄에 집의 수 N(2 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 각 집을 빨강, 초록, 파랑으로 칠하는 비용이 1번 집부터 한 줄에 하나씩 주어진다. 집을 칠하는 비용은 1,000보다 작거나 같은 자연수이다.

[출력]
첫째 줄에 모든 집을 칠하는 비용의 최솟값을 출력한다.
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

# main
N = int(input())    # N: 집의 개수
cost = [list(map(int, input().split())) for _ in range(N)]  # cost: 각 집을 빨강(0), 초록(1), 파랑(2)으로 칠하는 비용

dp = [[0]*3 for _ in range(N)]

# 초기값: 0번째 인덱스 집을 색상 c(0=빨강, 1=초록, 2=파랑)으로 칠할 때의 비용
dp[0][0], dp[0][1], dp[0][2] = cost[0]

# 점화식: dp[i][c] = i번째 인덱스 집을 색상 c(0=빨강, 1=초록, 2=파랑)으로 칠했을 때까지의 최소 총비용
#                 = (i-1)번째 집을 c가 아닌 색상으로 칠했을 때까지의 최소 총비용 중 더 작은 것
#                   + i번째 인덱스 집을 색상 c로 칠할 때의 비용
for i in range(1, N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]

print(min(dp[N-1])) # (N-1)번째 인덱스 집을 색상 c(0=빨강, 1=초록, 2=파랑)으로 칠했을 때까지의 최소 총비용 중 제일 작은 것을 출력

"""
* 실패한 코드: 시간 초과(TLE)
* 실패 이유 분석: 이 코드는 완전 탐색 (DFS + 백트래킹) 방식이라, 최악의 경우 3^N (≈ 3¹⁰⁰⁰) 가지를 모두 탐색해야 하기 때문에 error.

# 각각의 집을 규칙을 만족하면서 칠하는 비용의 최솟값을 계산하는 함수
def cal_min_cost(idx, total):
    
    global min_cost

    # 가지치기 1 : 이미 현재까지의 비용이 최소 비용을 넘었으면 더 계산할 필요 없으므로 종료
    if total >= min_cost:
        return

    # 모든 집을 전부 칠한 경우
    if idx == N:
        min_cost = min(total, min_cost) # 현재까지의 비용과 최소 비용을 비교하여 전역 최솟값 갱신
        return
    
    forbidden = -1  # forbidden(금지된 색상)을 -1로 초기화
    for c in range(3):  # 각각의 색상(빨강(0), 초록(1), 파랑(2))을 순회하면서,
        if idx > 0:                                     # 만약 첫 번째 집이 아니라면,
            forbidden = colored[idx - 1]                # 이전 번째의 집 색깔을 금지 색상으로 저장
        if c != forbidden:                              # 금지 색상이 아니라면,
            colored[idx] = c                            # 해당 순번의 집을 색상으로 칠함
            cal_min_cost(idx + 1, total + cost[idx][c])     # 색상을 칠한 비용을 total에 누적하고 다음 집으로 이동
            colored[idx] = -1                           # 백트래킹

# main
N = int(input())    # N: 집의 개수
cost = [list(map(int, input().split())) for _ in range(N)]  # cost: 각 집을 빨강(0), 초록(1), 파랑(2)으로 칠하는 비용
colored = [-1] * N  # 집 색상 배열

min_cost = 1000 * N # 최소 비용을 (1000 * N)으로 초기화
cal_min_cost(0, 0)  # 각각의 집을 규칙을 만족하면서 칠하는 비용의 최솟값을 계산하여 min_cost에 갱신

print(min_cost)     # 계산된 최소 비용을 출력
"""
