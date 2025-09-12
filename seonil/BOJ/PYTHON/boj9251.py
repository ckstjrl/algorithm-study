"""
BOJ9251. LCS
[문제]
LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.
예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

[입력]
첫째 줄과 둘째 줄에 두 문자열이 주어진다. 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.

[출력]
첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를 출력한다.
"""

import sys
input = sys.stdin.readline

# 문자열 입력
A = input().strip()
B = input().strip()

n, m = len(A), len(B)

# DP 테이블 초기화
# dp[i][j] = 문자열 A의 앞 i글자와 문자열 B의 앞 j글자의 LCS 길이
# 인덱스를 1부터 쓰기 위해 (n+1) x (m+1) 크기로 생성
dp = [[0] * (m + 1) for _ in range(n + 1)]

# 두 문자열의 각 문자를 비교하면서 테이블 채우기
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if A[i - 1] == B[j - 1]:
            # 현재 문자가 같다면, 이전 대각선 값(dp[i-1][j-1])에 +1
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            # 현재 문자가 다르다면,
            # A에서 한 글자 빼거나 B에서 한 글자 뺀 경우 중 더 큰 값 선택
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

# 최종적으로 dp[n][m]이 전체 문자열 A와 B의 LCS 길이
print(dp[n][m])