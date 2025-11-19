'''boj2225 - 합분해
0부터 N까지의 정수 K개를 더해서 그 합이 N이 되는 경우의 수를 구하는 프로그램을 작성하시오.

덧셈의 순서가 바뀐 경우는 다른 경우로 센다(1+2와 2+1은 서로 다른 경우). 또한 한 개의 수를 여러 번 쓸 수도 있다.
'''
# dp[i][j]를 i개 더해서 합 j를 만드는 경우의 수 라고 하면
# dp[i][j] = dp[i-1][0] + dp[i-1][1] + ... + dp[i-1][j]
# dp[i][j-1] = dp[i-1][0] + dp[i-1][1] + ... + dp[i-1][j-1]
# dp[i][j] = dp[i][j-1] + dp[i-1][j]

N, K = map(int, input().split())
#i개 더해서 합 j를 만드는 경우의 수 
dp = [[0] * (N + 1) for _ in range(K + 1)]
A = 1000000000

# i개의 수로 0을 만드는 경우? -> 0만 가능 -> 1가지
for i in range(K + 1):
    dp[i][0] = 1

for i in range(1, K + 1):
    for j in range(1, N + 1):
        dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % A

print(dp[K][N])