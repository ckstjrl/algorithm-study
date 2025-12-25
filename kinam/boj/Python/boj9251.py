'''boj9251 LCS
LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 
모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

입력
첫째 줄과 둘째 줄에 두 문자열이 주어진다. 문자열은 알파벳 대문자로만 이루어져 있으며, 
최대 1000글자로 이루어져 있다.

출력
첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를 출력한다.
'''

'''
ACAYKP / CAPCAK
A  / C  : LCS -> 0
A  / CA : LCS -> 1
AC / C  : LCS -> 1
AC / CA : LCS -> 1

AC  / CAP : LCS -> 1
ACA / C   : LCS -> 1
ACA / CA  : LCS -> 2
ACA / CAP : LCS -> 2
ACAY / C   : LCS -> 1
ACAY / CA   : LCS -> 2
ACAY / CAP   : LCS -> 2
ACAY / CAPC   : LCS -> 2

ACAYK / CAPCA : LCS -> 3


  C A P C A K
A 0 1 1 1 1 1  >> [1][2] A == A 일 때 1올라갔음 str1[0] == str2[1] 지점
C 1 1 1 2 2 2  >> [4][2] C == C 일 때 1 올라감 str1[1] == str2[3] 지점
A 1 2 2 2 3 3
Y 1 2 2 2 3 3
K 1 2 2 2 3 4
P 1 2 3 3 3 4


dp[i][j] = dp[i-1][j-1] + 1
i < j일때랑
i > j일때랑 조금 다른가?

i j 순회하며 str1[i] == str2[j]면 1증가

다르면?
dp[i][j] = max(dp[i-1][j], dp[i][j-1]) 둘중에 큰 값
'''

str1 = input()
str2 = input()

N = len(str1)
M = len(str2)

dp = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])


print(dp[N][M])