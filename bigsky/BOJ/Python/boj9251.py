# BOJ9251(D3): LCS
dp = [[0] * 1001 for _ in range(1001)]

A, B = input(), input()

for i in range(1, len(A) + 1):
    for j in range(1, len(B) + 1):
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[len(A)][len(B)])

'''
코드는 매우 간결하지만, 구현하는 방법은 잘 떠오르지 않았던 DP문제
답을 알고나니 해결 방법은 의외로 간단하다.
N*N의 2차원 배열을 만들고, 작은 단위부터 하나씩 비교해보며 해당 부분에 저장한다면,
이 문제를 쉽게 풀 수 있다.

이 문제는 길이를 출력할 것을 요구하기 때문에
길이를 저장한다.
'''