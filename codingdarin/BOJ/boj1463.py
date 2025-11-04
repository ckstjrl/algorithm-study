# BOJ 1463 - 1로 만들기 (D3, S3)
# 1을 만드는 최소횟수
# 최적부분구조

N = int(input())
dp = [0] * (N+1)

# 초기값
dp[1] = 0

for i in range(2,N+1):
    # 1 빼기
    dp[i] = dp[i-1] +1

    # 2 나누기
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)

    # 3 나누기
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[N])