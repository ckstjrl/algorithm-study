# BOJ10844. 쉬운 계단 수

N = int(input())

dp = [[0]*10 for _ in range(N+1)]

for i in range(1, 10):
    dp[1][i] = 1

pre_ans = 1000000000

for i in range(2, N+1):

    for j in range(10):
        # 마지막 숫자가 0인 경우, 앞 숫자 == 1
        if j == 0:
            dp[i][j] = dp[i-1][1]
        
        # 마지막 숫자가 9인 경우, 앞 숫자 == 8
        elif j == 9:
            dp[i][j] = dp[i-1][8]

        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

        dp[i][j] %= pre_ans

print(sum(dp[N]) % pre_ans)
