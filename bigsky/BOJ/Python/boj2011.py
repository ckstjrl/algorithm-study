# BOJ2011(D3): 암호코드
pw = input()
n = len(pw)
MOD = 100_0000

# 암호가 0으로 시작하면 바로 종료
if pw[0] == '0':
    print(0)
else:
    dp = [0] * (n + 1)
    dp[0] = 1 # 빈 문자열
    dp[1] = 1

    for i in range(2, n + 1):
        # 한 자리 숫자로 해석하는 경우 (1~9)
        if pw[i-1] != '0':
            dp[i] += dp[i-1]
        # 두 자리 숫자로 해석하는 경우 (10~26)
        if 10 <= int(pw[i-2:i]) <= 26:
            dp[i] += dp[i-2]
    
    print(dp[n] % MOD)
    