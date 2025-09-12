# BOJ 9251. LCS (D3, G5)
# 최장 공통 부분 수열

#--------------------------------1회차 풀이

A = input()
B = input()

# 전체에서 줄여가면서 돌기? => 지수적 시간복잡도
# DP로 풀어야 함


# dp[i][j] = A에서 i번째까지, B에서 j번째까지 lcs 길이
n, m = len(A), len(B)
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if A[i-1] == B[j-1]:  # 같으면
            dp[i][j] = dp[i-1][j-1] + 1
        else:  # 다르면
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[n][m])
