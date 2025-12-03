# boj1904(D2): 01타일
n = int(input())
dp = [0] * 1000001
dp[1], dp[2] = 1, 2
for i in range(3, n + 1):
    dp[i] = (dp[i-2] + dp[i-1]) % 15746
print(dp[n])




# 팩토리얼로 푸는 건 시간초과 -> dp로 풀어야함
# import math
#
# n = int(input())
# result = 0
# for i in range(n//2 + 1):
#     d_zero = i
#     one = n - i * 2
#
#     total = math.factorial(d_zero + one) // (math.factorial(d_zero) * math.factorial(one))
#     result += total
#
# print(result % 15746)