# 9251. LCS
import sys
input = sys.stdin.readline

str1 = input().strip()
str2 = input().strip()

n, m = len(str1), len(str2)

# dp[i][j]: str1의 ~i자리까지, str2의 ~j자리까지 비교했을 때의 LCS 길이
# 비교하기 전 값은 모두 0으로 초기화
dp = [[0]*(m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        # 비교한 자리 글자 같으면: LCS 길이 연장, +1
        if str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        # 비교한 자리 글자 다르면: 
        # str1, str2 각각에서 한 자리씩 뺐을 때의 LCS 길이 중 더 큰 값으로
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

# 두 문자열 모두 끝까지 비교했을 때의 LCS 길이는 dp[len(str1)][len(str2)]에 있음
print(dp[n][m])