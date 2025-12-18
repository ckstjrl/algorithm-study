# BOJ 9251. LCS
'''
LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때,
모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

첫째 줄과 둘째 줄에 두 문자열이 주어진다. 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.

첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를 출력한다.
'''
import sys
A = sys.stdin.readline().strip()
B = sys.stdin.readline()

dp = [[0]*(len(A)+1) for _ in range(len(B)+1)]

for i in range(len(B)):
    for j in range(len(A)):
        if B[i] == A[j]:
            dp[i+1][j+1] = dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

max_v = 0
for x in range(len(B)+1):
    for y in range(len(A)+1):
        if dp[x][y] > max_v:
            max_v = dp[x][y]

print(max_v)

'''
LCS 알고리즘 활용
dp를 통해서 문제 풀이 진행
dp를 이차원 배열로 제작, 행은 B의 길이 + 1 열은 A의 길이 + 1 로 만들어서 진행
예시로 ABCD , ACDFE로 진행
| dp | - | A | B | C | D |
| --- | --- | --- | --- | --- | --- |
| - | 0 | 0 | 0 | 0 | 0 |
| A | 0 | 1 | 1 | 1 | 1 |
| C | 0 | 1 | 1 | 2 | 2 |
| D | 0 | 1 | 1 | 2 | 3 |
| F | 0 | 1 | 1 | 2 | 3 |
| E | 0 | 1 | 1 | 2 | 3 |
이런식으로 나오게 됨.

여기서 최댓값을 찾으면 그게 LCS 길이가 되는 것.
'''