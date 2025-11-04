"""
BOJ10844. 쉬운 계단 수

[문제]
45656이란 수를 보자.
이 수는 인접한 모든 자리의 차이가 1이다. 이런 수를 계단 수라고 한다.
N이 주어질 때, 길이가 N인 계단 수가 총 몇 개 있는지 구해보자. 0으로 시작하는 수는 계단수가 아니다.

[입력]
첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 100보다 작거나 같은 자연수이다.

[출력]
첫째 줄에 정답을 1,000,000,000으로 나눈 나머지를 출력한다.
"""

def count_stair_numbers(N):

    # dp[n][last] : 길이가 n이고 마지막 숫자가 last인 계단수 개수
    dp = [[0] * 10 for _ in range(N + 1)]

    # 초기값 (n = 1에서 0은 불가능하므로 숫자는 1~9만 가능)
    for last in range(1, 10):
        dp[1][last] = 1

    # 점화식으로 채우기
    for n in range(2, N + 1):   # n = 2, 3, 4, ... , (N-1), N
        for last in range(10):  # 0 ~ 9를 새로 추가할 마지막 숫자로 순회
            # 점화식 : 길이가 n이고 마지막 숫자가 last인 계단수 개수 = 길이가 (n-1)이고 마지막 숫자가 (last-1)인 계단수 개수 + 길이가 (n-1)이고 마지막 숫자가 (last+1)인 계단수 개수
            if last > 0:
                dp[n][last] += dp[n-1][last-1]
            if last < 9:
                dp[n][last] += dp[n-1][last+1]

    # 길이가 N인 계단수 개수를 모두 더하여 출력
    return sum(dp[N])

# main
N = int(input())
ans = count_stair_numbers(N) % 10**9
print(ans)